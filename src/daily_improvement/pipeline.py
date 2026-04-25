from __future__ import annotations

from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .backlog import update_backlog
from .collectors import collect_from_config
from .config import load_research_config
from .dedup import deduplicate_findings
from .map_projects import build_recommendations
from .models import PipelineResult, RawItem
from .normalize import normalize_many
from .report import generate_daily_report
from .score import score_many
from .sources import load_raw_items_from_json

DEFAULT_SOURCE_PATH = Path("data/daily_improvement/sample_raw_items.json")
DEFAULT_CONFIG_PATH = Path("config/research_sources.example.yaml")


def run_daily_pipeline(
    source_path: str | Path | None = None,
    config_path: str | Path | None = None,
    output_dir: str | Path = "docs/daily-research",
    backlog_path: str | Path = "docs/IMPROVEMENT_BACKLOG.md",
    run_date: str | None = None,
    max_items: int | None = None,
) -> PipelineResult:
    resolved_run_date = run_date or datetime.now(timezone.utc).date().isoformat()

    raw_items, collection_errors, effective_output_dir, effective_backlog_path = _load_raw_items(
        source_path=source_path,
        config_path=config_path,
        output_dir=output_dir,
        backlog_path=backlog_path,
    )
    if max_items is not None:
        raw_items = raw_items[:max_items]

    findings = deduplicate_findings(normalize_many(raw_items))
    assessments = score_many(findings)
    recommendations = build_recommendations(findings, assessments)

    report_path = generate_daily_report(
        run_date=resolved_run_date,
        findings=findings,
        assessments=assessments,
        recommendations=recommendations,
        output_dir=effective_output_dir,
    )
    created_backlog_items = update_backlog(
        findings=findings,
        assessments=assessments,
        backlog_path=effective_backlog_path,
        report_path=str(report_path),
    )

    return PipelineResult(
        run_date=resolved_run_date,
        raw_items_count=len(raw_items),
        findings_count=len(findings),
        report_path=str(report_path),
        backlog_updated=created_backlog_items > 0,
        created_backlog_items=created_backlog_items,
        errors=collection_errors,
    )


def _load_raw_items(
    source_path: str | Path | None,
    config_path: str | Path | None,
    output_dir: str | Path,
    backlog_path: str | Path,
) -> tuple[list[RawItem], list[str], str | Path, str | Path]:
    if config_path:
        config = load_research_config(config_path)
        collected = collect_from_config(config)
        return collected.raw_items, collected.errors, config.reports_dir or output_dir, config.backlog_file or backlog_path

    effective_source = Path(source_path) if source_path else DEFAULT_SOURCE_PATH
    return load_raw_items_from_json(effective_source), [], output_dir, backlog_path


def pipeline_result_to_dict(result: PipelineResult) -> dict[str, Any]:
    return asdict(result)
