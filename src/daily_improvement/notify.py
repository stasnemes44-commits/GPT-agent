from __future__ import annotations

from .models import PipelineResult


def format_daily_notification(result: PipelineResult) -> str:
    status = "completed with warnings" if result.errors else "completed"
    lines = [
        f"Daily Improvement Run {status}.",
        "",
        f"Date: {result.run_date}",
        f"Raw items: {result.raw_items_count}",
        f"Findings: {result.findings_count}",
        f"Backlog items added: {result.created_backlog_items}",
        f"Report: {result.report_path}",
    ]
    if result.errors:
        lines.append("")
        lines.append("Warnings:")
        for error in result.errors[:5]:
            lines.append(f"- {error}")
        if len(result.errors) > 5:
            lines.append(f"- ...and {len(result.errors) - 5} more")
    return "\n".join(lines)


def format_weekly_notification(weekly_report_path: str) -> str:
    return "\n".join(
        [
            "Weekly Improvement Synthesis is ready.",
            "",
            f"Report: {weekly_report_path}",
        ]
    )
