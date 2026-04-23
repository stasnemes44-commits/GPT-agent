from __future__ import annotations

from .models import Finding


def deduplicate_findings(findings: list[Finding]) -> list[Finding]:
    seen: dict[str, Finding] = {}
    for finding in findings:
        key = finding.url.strip().lower() or finding.title.strip().lower()
        if key not in seen:
            seen[key] = finding
            continue

        existing = seen[key]
        merged_sources = list(dict.fromkeys(existing.supporting_sources + finding.supporting_sources))
        merged_topics = sorted(set(existing.topics + finding.topics))
        existing.supporting_sources = merged_sources
        existing.topics = merged_topics
    return list(seen.values())
