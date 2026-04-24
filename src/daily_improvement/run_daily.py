from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

from .backlog import update_backlog
from .dedup import deduplicate_findings
from .map_projects import build_recommendations
from .normalize import normalize_many
from .report import generate_daily_report
from .score import score_many
from .sources import SourceLoadError, ensure_sample_fixture, load_raw_items_from_json


def run_daily(source_path: str | Path | None = None) -> dict[str, object]:
    effective_source = Path(source_path) if source_path else ensure_sample_fixture()
    raw_items = load_raw_items_from_json(effective_source)
    findings = deduplicate_findings(normalize_many(raw_items))
    assessments = score_many(findings)
    recommendations = build_recommendations(findings, assessments)

    run_date = datetime.now(timezone.utc).date().isoformat()
    report_path = generate_daily_report(
        run_date=run_date,
        findings=findings,
        assessments=assessments,
        recommendations=recommendations,
    )
    backlog_added = update_backlog(
        findings=findings,
        assessments=assessments,
        report_path=str(report_path),
    )

    return {
        "run_date": run_date,
        "source_path": str(effective_source),
        "raw_items": len(raw_items),
        "findings": len(findings),
        "recommendations": len(recommendations),
        "report_path": str(report_path),
        "backlog_items_added": backlog_added,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the daily improvement pipeline.")
    parser.add_argument("--source", dest="source", help="Path to raw items JSON file", default=None)
    args = parser.parse_args()

    try:
        result = run_daily(args.source)
    except SourceLoadError as exc:
        print(f"[daily_improvement] source error: {exc}")
        return 1

    print("[daily_improvement] run complete")
    for key, value in result.items():
        print(f"- {key}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
