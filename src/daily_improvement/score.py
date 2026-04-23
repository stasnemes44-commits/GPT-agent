from __future__ import annotations

from .models import Assessment, Finding, ScoreCard


def score_finding(finding: Finding) -> Assessment:
    topics = set(finding.topics)

    relevance_openclaw = 5 if {"agents", "memory", "workflow", "browser_agent", "voice"} & topics else 2
    relevance_airys = 5 if {"medical_logic", "workflow", "business_metrics", "voice"} & topics else 2
    practical_value = 4 if len(finding.summary) > 40 else 2
    integration_effort = 2 if {"workflow", "ux", "reminders"} & topics else 3
    maturity = 4 if finding.evidence_strength == "official" else 2
    risk = 2 if finding.evidence_strength == "official" else 3
    partial_adoptability = 5
    business_impact = 4 if {"business_metrics", "workflow", "medical_logic"} & topics else 2
    novelty = 3
    evidence_strength = 5 if finding.evidence_strength == "official" else 3

    scores = ScoreCard(
        relevance_openclaw=relevance_openclaw,
        relevance_airys=relevance_airys,
        practical_value=practical_value,
        integration_effort=integration_effort,
        maturity=maturity,
        risk=risk,
        partial_adoptability=partial_adoptability,
        business_impact=business_impact,
        novelty=novelty,
        evidence_strength=evidence_strength,
        total_score=0.0,
    )
    scores.total_score = round(_weighted_total(scores), 2)

    verdict = _classify_verdict(scores.total_score)
    confidence = "high" if finding.evidence_strength == "official" else "medium"
    time_horizon = "now" if scores.total_score >= 3.8 else "next" if scores.total_score >= 3.0 else "later"
    rationale = (
        f"Finding scored {scores.total_score} based on topic relevance, evidence strength, practical value, and estimated integration effort."
    )

    return Assessment(
        finding_id=finding.id,
        scores=scores,
        verdict=verdict,
        confidence=confidence,
        time_horizon=time_horizon,
        rationale=rationale,
    )


def score_many(findings: list[Finding]) -> list[Assessment]:
    return [score_finding(finding) for finding in findings]


def _weighted_total(scores: ScoreCard) -> float:
    return (
        0.20 * scores.relevance_openclaw
        + 0.20 * scores.relevance_airys
        + 0.15 * scores.practical_value
        + 0.10 * scores.business_impact
        + 0.10 * scores.maturity
        + 0.10 * scores.partial_adoptability
        + 0.05 * scores.novelty
        + 0.05 * scores.evidence_strength
        - 0.025 * scores.integration_effort
        - 0.025 * scores.risk
    )


def _classify_verdict(total_score: float) -> str:
    if total_score >= 4.0:
        return "adopt_full"
    if total_score >= 3.0:
        return "adopt_partial"
    if total_score >= 2.0:
        return "watch"
    return "ignore"
