from __future__ import annotations

from .models import Assessment, Finding, Recommendation


def build_recommendations(findings: list[Finding], assessments: list[Assessment]) -> list[Recommendation]:
    finding_map = {finding.id: finding for finding in findings}
    recommendations: list[Recommendation] = []

    for assessment in assessments:
        if assessment.verdict not in {"adopt_full", "adopt_partial"}:
            continue

        finding = finding_map.get(assessment.finding_id)
        if finding is None:
            continue

        projects = _infer_projects(finding)
        for project in projects:
            recommendations.append(
                Recommendation(
                    project=project,
                    finding_id=finding.id,
                    what_to_take=_what_to_take(finding, project),
                    what_not_to_take="Do not copy the full solution blindly; keep only the useful pattern.",
                    minimum_spike=_minimum_spike(finding, project),
                    expected_gain=_expected_gain(finding, project),
                    risk="Wrong transfer without adaptation can add noise or unsafe complexity.",
                )
            )

    return recommendations


def _infer_projects(finding: Finding) -> list[str]:
    topics = set(finding.topics)
    projects: list[str] = []

    if {"agents", "memory", "browser_agent", "voice", "workflow"} & topics:
        projects.append("OpenClaw")
    if {"medical_logic", "workflow", "business_metrics", "voice"} & topics:
        projects.append("AIRYS")
    if "medical_logic" in topics:
        projects.append("Medical Agents")
    if "workflow" in topics:
        projects.append("Automations")

    return projects or ["OpenClaw"]


def _what_to_take(finding: Finding, project: str) -> str:
    if project == "OpenClaw":
        return f"Extract the strongest pattern from '{finding.title}' for agent memory, workflow, or interaction quality."
    if project == "AIRYS":
        return f"Adapt the useful logic from '{finding.title}' to patient/admin workflows and reminders."
    if project == "Medical Agents":
        return f"Take only the safe and auditable pattern from '{finding.title}'."
    return f"Use '{finding.title}' as a candidate improvement for orchestration or automation."


def _minimum_spike(finding: Finding, project: str) -> str:
    return f"Create a small spike note for {project} showing how one narrow pattern from '{finding.title}' could be tested in isolation."


def _expected_gain(finding: Finding, project: str) -> str:
    if project == "AIRYS":
        return "Better prioritization, reminders, workflow clarity, or business visibility."
    if project == "Medical Agents":
        return "Safer logic with clearer auditability and more useful structured memory."
    if project == "Automations":
        return "More reliable orchestration and less manual scanning of new ideas."
    return "Stronger personal agent capabilities with less chaos and better decision support."
