from __future__ import annotations

from pathlib import Path

from .models import Assessment, Finding

DEFAULT_BACKLOG_PATH = Path("docs/IMPROVEMENT_BACKLOG.md")


def update_backlog(
    findings: list[Finding],
    assessments: list[Assessment],
    backlog_path: str | Path = DEFAULT_BACKLOG_PATH,
    report_path: str | None = None,
) -> int:
    target = Path(backlog_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    if not target.exists():
        target.write_text("# Improvement Backlog\n\n## Auto-added candidates\n", encoding="utf-8")

    current = target.read_text(encoding="utf-8")
    finding_map = {item.id: item for item in findings}

    appended = 0
    lines_to_add: list[str] = []
    for assessment in assessments:
        if assessment.verdict not in {"adopt_full", "adopt_partial"}:
            continue
        finding = finding_map.get(assessment.finding_id)
        if finding is None:
            continue
        marker = f"[{assessment.finding_id}]"
        if marker in current:
            continue
        lines_to_add.extend(
            [
                f"## {marker} {finding.title}",
                "- Status: candidate",
                f"- Topics: {', '.join(finding.topics) if finding.topics else 'general'}",
                f"- Source: {finding.source}",
                f"- Report: {report_path or 'daily report'}",
                f"- Verdict: {assessment.verdict}",
                f"- Why it matters: {assessment.rationale}",
                f"- URL: {finding.url}",
                "",
            ]
        )
        appended += 1

    if lines_to_add:
        with target.open("a", encoding="utf-8") as fh:
            fh.write("\n" + "\n".join(lines_to_add))

    return appended
