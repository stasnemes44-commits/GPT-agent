from __future__ import annotations

import argparse
import json
from pathlib import Path

from .pipeline import pipeline_result_to_dict, run_daily_pipeline
from .sources import SourceLoadError
from .weekly import generate_weekly_synthesis


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the daily improvement pipeline.")
    subparsers = parser.add_subparsers(dest="command")

    daily = subparsers.add_parser("daily", help="Run daily improvement analysis.")
    daily.add_argument("--source", default=None, help="Path to input JSON fixture or collected raw items file.")
    daily.add_argument("--config", default=None, help="Path to research sources config for live collection mode.")
    daily.add_argument("--output-dir", default="docs/daily-research", help="Directory for markdown reports.")
    daily.add_argument("--backlog-path", default="docs/IMPROVEMENT_BACKLOG.md", help="Path to backlog markdown file.")
    daily.add_argument("--run-date", default=None, help="Optional run date in YYYY-MM-DD format.")
    daily.add_argument("--max-items", type=int, default=None, help="Optional maximum number of raw items to process.")
    daily.add_argument("--json", action="store_true", help="Print result as JSON.")

    weekly = subparsers.add_parser("weekly", help="Generate weekly synthesis from daily reports.")
    weekly.add_argument("--reports-dir", default="docs/daily-research", help="Directory with daily markdown reports.")
    weekly.add_argument("--output-path", default=None, help="Optional output markdown path.")
    weekly.add_argument("--week-label", default=None, help="Optional week label, for example 2026-W17.")
    weekly.add_argument("--json", action="store_true", help="Print result as JSON.")

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command in {None, "daily"}:
        return _run_daily(args)
    if args.command == "weekly":
        return _run_weekly(args)

    parser.print_help()
    return 1


def _run_daily(args: argparse.Namespace) -> int:
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


def _run_weekly(args: argparse.Namespace) -> int:
    try:
        output_path = generate_weekly_synthesis(
            reports_dir=Path(args.reports_dir),
            output_path=Path(args.output_path) if args.output_path else None,
            week_label=args.week_label,
        )
    except Exception as exc:  # pragma: no cover
        print(f"[daily_improvement] weekly synthesis error: {exc}")
        return 2

    payload = {"weekly_report_path": str(output_path)}
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print("[daily_improvement] weekly synthesis complete")
        print(f"- weekly_report_path: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
