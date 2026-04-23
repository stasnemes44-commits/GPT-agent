from __future__ import annotations

from datetime import date
from pathlib import Path

from .models import Assessment, Finding, Recommendation


def generate_daily_report(
    run_date: str,
    findings: list[Finding],
    assessments: list[Assessment],
    recommendations: list[Recommendation],
    output_dir: str | Path = "docs/daily-research",
) -> Path:
    target_dir = Path(output_dir)
    target_dir.mkdir(parents=True, exist_ok=True)
    output_path = target_dir / f"{run_date}.md"

    assessment_map = {item.finding_id: item for item in assessments}
    rec_map: dict[str, list[Recommendation]] = {}
    for rec in recommendations:
        rec_map.setdefault(rec.finding_id, []).append(rec)

    lines: list[str] = []
    lines.append(f"# Daily Improvement Report — {run_date}")
    lines.append("")
    lines.append("## 1. Executive Summary")
    lines.append(f"- Findings reviewed: {len(findings)}")
    strong_items = sum(1 for item in assessments if item.verdict in {"adopt_full", "adopt_partial"})
    lines.append(f"- Strong candidates: {strong_items}")
    lines.append(f"- Generated recommendations: {len(recommendations)}")
    lines.append("")
    lines.append("## 2. Findings")
    lines.append("")

    for finding in findings:
        assessment = assessment_map.get(finding.id)
        lines.append(f"### {finding.title}")
        lines.append(f"- Source: {finding.source}")
        lines.append(f"- URL: {finding.url}")
        lines.append(f"- Published: {finding.published_at or 'unknown'}")
        lines.append(f"- Topics: {', '.join(finding.topics) if finding.topics else 'none'}")
        lines.append(f"- Summary: {finding.summary or 'No summary'}")
        if assessment:
            lines.append("")
            lines.append("#### Assessment")
            lines.append(f"- Verdict: {assessment.verdict}")
            lines.append(f"- Confidence: {assessment.confidence}")
            lines.append(f"- Time horizon: {assessment.time_horizon}")
            lines.append(f"- Total score: {assessment.scores.total_score}")
            lines.append(f"- Rationale: {assessment.rationale}")
        recommendations_for_finding = rec_map.get(finding.id, [])
        if recommendations_for_finding:
            lines.append("")
            lines.append("#### Recommended Uses")
            for rec in recommendations_for_finding:
                lines.append(f"- **{rec.project}**: {rec.what_to_take}")
                lines.append(f"  - Minimum spike: {rec.minimum_spike}")
                lines.append(f"  - Expected gain: {rec.expected_gain}")
        lines.append("")

    lines.append("## 3. Backlog Candidates")
    backlog_items = [item for item in assessments if item.verdict in {"adopt_full", "adopt_partial"}]
    for item in backlog_items:
        lines.append(f"- [ ] {item.finding_id} — {item.verdict} — {item.rationale}")
    if not backlog_items:
        lines.append("- None today")
    lines.append("")
    lines.append(f"_Generated on {date.today().isoformat()}_")

    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path
