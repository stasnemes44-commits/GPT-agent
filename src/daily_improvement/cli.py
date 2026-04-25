from __future__ import annotations

import argparse
import json
from pathlib import Path

from .pipeline import pipeline_result_to_dict, run_daily_pipeline
from .sources import SourceLoadError


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the daily improvement pipeline.")
    parser.add_argument("--source", default=None, help="Path to input JSON fixture or collected raw items file.")
    parser.add_argument("--config", default=None, help="Path to research sources config for live collection mode.")
    parser.add_argument("--output-dir", default="docs/daily-research", help="Directory for markdown reports.")
    parser.add_argument("--backlog-path", default="docs/IMPROVEMENT_BACKLOG.md", help="Path to backlog markdown file.")
    parser.add_argument("--run-date", default=None, help="Optional run date in YYYY-MM-DD format.")
    parser.add_argument("--max-items", type=int, default=None, help="Optional maximum number of raw items to process.")
    parser.add_argument("--json", action="store_true", help="Print result as JSON.")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        result = run_daily_pipeline(
            source_path=Path(args.source) if args.source else None,
            config_path=Path(args.config) if args.config else None,
            output_dir=Path(args.output_dir),
            backlog_path=Path(args.backlog_path),
            run_date=args.run_date,
            max_items=args.max_items,
        )
    except SourceLoadError as exc:
        print(f"[daily_improvement] source error: {exc}")
        return 1
    except Exception as exc:  # pragma: no cover
        print(f"[daily_improvement] unexpected error: {exc}")
        return 2

    payload = pipeline_result_to_dict(result)
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print("[daily_improvement] run complete")
        for key, value in payload.items():
            print(f"- {key}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
