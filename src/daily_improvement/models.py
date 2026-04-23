from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime
from typing import Any


@dataclass(slots=True)
class RawItem:
    source: str
    title: str
    url: str
    published_at: str | None = None
    summary_raw: str = ""
    topic_guess: list[str] = field(default_factory=list)
    source_type: str = "unknown"
    source_category: str = "unknown"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class Finding:
    id: str
    source: str
    title: str
    url: str
    published_at: str | None
    summary: str
    topics: list[str]
    entities: list[str] = field(default_factory=list)
    evidence_strength: str = "secondary"
    raw_type: str = "unknown"
    supporting_sources: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class ScoreCard:
    relevance_openclaw: int
    relevance_airys: int
    practical_value: int
    integration_effort: int
    maturity: int
    risk: int
    partial_adoptability: int
    business_impact: int
    novelty: int
    evidence_strength: int
    total_score: float

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class Assessment:
    finding_id: str
    scores: ScoreCard
    verdict: str
    confidence: str
    time_horizon: str
    rationale: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "finding_id": self.finding_id,
            "scores": self.scores.to_dict(),
            "verdict": self.verdict,
            "confidence": self.confidence,
            "time_horizon": self.time_horizon,
            "rationale": self.rationale,
        }


@dataclass(slots=True)
class Recommendation:
    project: str
    finding_id: str
    what_to_take: str
    what_not_to_take: str
    minimum_spike: str
    expected_gain: str
    risk: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class PipelineResult:
    run_date: str
    raw_items_count: int
    findings_count: int
    report_path: str
    backlog_updated: bool
    created_backlog_items: int
    errors: list[str] = field(default_factory=list)
    generated_at: str = field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
