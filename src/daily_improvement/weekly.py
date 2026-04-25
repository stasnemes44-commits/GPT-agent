from __future__ import annotations

from collections import Counter
from pathlib import Path


def generate_weekly_synthesis(
    reports_dir: str | Path = "docs/daily-research",
    output_path: str | Path | None = None,
    week_label: str | None = None,
) -> Path:
    source_dir = Path(reports_dir)
    if not source_dir.exists():
        raise FileNotFoundError(f"Reports directory not found: {source_dir}")

    daily_reports = sorted(
        path for path in source_dir.glob("*.md")
        if path.name != "TEMPLATE.md" and not path.name.startswith("weekly-")
    )[-7:]

    label = week_label or "latest"
    target = Path(output_path) if output_path else source_dir / f"weekly-{label}.md"
    target.parent.mkdir(parents=True, exist_ok=True)

    report_texts = [(path.name, path.read_text(encoding="utf-8")) for path in daily_reports]
    topics = _collect_topic_counts(report_texts)
    verdicts = _collect_verdict_counts(report_texts)
    backlog_candidates = _collect_backlog_lines(report_texts)

    lines: list[str] = []
    lines.append(f"# Weekly Improvement Synthesis — {label}")
    lines.append("")
    lines.append("## 1. Scope")
    lines.append(f"- Daily reports reviewed: {len(report_texts)}")
    for name, _ in report_texts:
        lines.append(f"- {name}")
    lines.append("")

    lines.append("## 2. Main Signals")
    if topics:
        for topic, count in topics.most_common(10):
            lines.append(f"- {topic}: {count}")
    else:
        lines.append("- No strong topic signal found.")
    lines.append("")

    lines.append("## 3. Verdict Distribution")
    if verdicts:
        for verdict, count in verdicts.most_common():
            lines.append(f"- {verdict}: {count}")
    else:
        lines.append("- No verdicts found.")
    lines.append("")

    lines.append("## 4. Backlog Candidates Mentioned")
    if backlog_candidates:
        for item in backlog_candidates[:20]:
            lines.append(item)
    else:
        lines.append("- No backlog candidates detected.")
    lines.append("")

    lines.append("## 5. Human Review Questions")
    lines.append("- Which repeated topic deserves a real spike next week?")
    lines.append("- Which backlog candidate should be rejected to avoid noise?")
    lines.append("- Which source produced the most useful signal?")
    lines.append("- Which project benefits most: OpenClaw, AIRYS, Medical Agents, or Automations?")
    lines.append("")

    lines.append("## 6. Decision Gate")
    lines.append("No code changes should be made automatically from this synthesis.")
    lines.append("Promote only selected candidates into explicit implementation tasks.")
    lines.append("")

    target.write_text("\n".join(lines), encoding="utf-8")
    return target


def _collect_topic_counts(report_texts: list[tuple[str, str]]) -> Counter[str]:
    counter: Counter[str] = Counter()
    for _, text in report_texts:
        for line in text.splitlines():
            if line.startswith("- Topics:"):
                values = line.replace("- Topics:", "").strip()
                for topic in values.split(","):
                    topic = topic.strip()
                    if topic and topic != "none":
                        counter[topic] += 1
    return counter


def _collect_verdict_counts(report_texts: list[tuple[str, str]]) -> Counter[str]:
    counter: Counter[str] = Counter()
    for _, text in report_texts:
        for line in text.splitlines():
            if line.startswith("- Verdict:"):
                verdict = line.replace("- Verdict:", "").strip()
                if verdict:
                    counter[verdict] += 1
    return counter


def _collect_backlog_lines(report_texts: list[tuple[str, str]]) -> list[str]:
    lines: list[str] = []
    for name, text in report_texts:
        in_section = False
        for line in text.splitlines():
            if line.startswith("## 3. Backlog Candidates"):
                in_section = True
                continue
            if in_section and line.startswith("## "):
                in_section = False
            if in_section and line.startswith("- [ ]"):
                lines.append(f"- {name}: {line[6:].strip()}")
    return lines
