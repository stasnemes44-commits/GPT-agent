from __future__ import annotations

import hashlib
import re
from collections.abc import Iterable

from .models import Finding, RawItem

TOPIC_KEYWORDS: dict[str, tuple[str, ...]] = {
    "agents": ("agent", "agents", "assistant", "orchestration"),
    "memory": ("memory", "recall", "engram", "knowledge"),
    "voice": ("voice", "speech", "audio"),
    "workflow": ("workflow", "automation", "n8n"),
    "browser_agent": ("browser", "web agent"),
    "medical_logic": ("medical", "clinic", "patient", "doctor"),
    "business_metrics": ("roi", "revenue", "conversion", "no-show"),
}


def normalize_raw_item(raw: RawItem) -> Finding:
    summary = _clean_text(raw.summary_raw)
    topics = sorted(set(raw.topic_guess + infer_topics(raw.title, summary)))
    entities = extract_entities(raw.title)
    stable_hash = hashlib.sha1(f"{raw.source}|{raw.title}|{raw.url}".encode("utf-8")).hexdigest()[:12]

    return Finding(
        id=stable_hash,
        source=raw.source,
        title=raw.title.strip(),
        url=raw.url.strip(),
        published_at=raw.published_at,
        summary=summary,
        topics=topics,
        entities=entities,
        evidence_strength="official" if raw.source_category == "official" else "secondary",
        raw_type=raw.source_type,
        supporting_sources=[raw.url.strip()] if raw.url.strip() else [],
    )


def normalize_many(items: Iterable[RawItem]) -> list[Finding]:
    return [normalize_raw_item(item) for item in items if item.title.strip()]


def infer_topics(*parts: str) -> list[str]:
    text = " ".join(parts).lower()
    found: list[str] = []
    for topic, keywords in TOPIC_KEYWORDS.items():
        if any(keyword in text for keyword in keywords):
            found.append(topic)
    return found


def extract_entities(text: str) -> list[str]:
    matches = re.findall(r"\b[A-Z][A-Za-z0-9_.-]{2,}\b", text)
    unique: list[str] = []
    for match in matches:
        if match not in unique:
            unique.append(match)
    return unique[:8]


def _clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()
