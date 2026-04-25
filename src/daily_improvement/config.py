from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class SourceConfig:
    id: str
    type: str
    enabled: bool = True
    category: str = "secondary"
    url: str | None = None
    repo: str | None = None
    repos: list[str] = field(default_factory=list)
    weight: float = 1.0


@dataclass(slots=True)
class ResearchConfig:
    timezone: str = "Europe/Kyiv"
    daily_run_time: str = "07:30"
    max_items_per_run: int = 50
    max_findings_after_dedup: int = 15
    write_reports: bool = True
    update_backlog: bool = True
    auto_modify_code: bool = False
    include_topics: list[str] = field(default_factory=list)
    exclude_keywords: list[str] = field(default_factory=list)
    sources: list[SourceConfig] = field(default_factory=list)
    reports_dir: str = "docs/daily-research"
    backlog_file: str = "docs/IMPROVEMENT_BACKLOG.md"
    watchlist_file: str = "docs/INNOVATION_WATCHLIST.md"


def load_research_config(path: str | Path) -> ResearchConfig:
    """Load a small YAML-like config without requiring PyYAML.

    This parser intentionally supports the subset used by config/research_sources.example.yaml.
    It is not a general YAML parser. The goal is to keep Phase 2 foundation dependency-free.
    """
    config_path = Path(path)
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    text = config_path.read_text(encoding="utf-8")
    data = _parse_minimal_yaml(text)
    return _to_research_config(data)


def _to_research_config(data: dict[str, Any]) -> ResearchConfig:
    global_cfg = data.get("global", {}) if isinstance(data.get("global", {}), dict) else {}
    filters_cfg = data.get("filters", {}) if isinstance(data.get("filters", {}), dict) else {}
    output_cfg = data.get("output", {}) if isinstance(data.get("output", {}), dict) else {}
    raw_sources = data.get("sources", []) if isinstance(data.get("sources", []), list) else []

    sources: list[SourceConfig] = []
    for item in raw_sources:
        if not isinstance(item, dict):
            continue
        repos_value = item.get("repos", [])
        if isinstance(repos_value, str):
            repos = [repos_value]
        elif isinstance(repos_value, list):
            repos = [str(repo) for repo in repos_value]
        else:
            repos = []
        sources.append(
            SourceConfig(
                id=str(item.get("id", "unknown")),
                type=str(item.get("type", "unknown")),
                enabled=bool(item.get("enabled", True)),
                category=str(item.get("category", "secondary")),
                url=item.get("url"),
                repo=item.get("repo"),
                repos=repos,
                weight=float(item.get("weight", 1.0)),
            )
        )

    return ResearchConfig(
        timezone=str(global_cfg.get("timezone", "Europe/Kyiv")),
        daily_run_time=str(global_cfg.get("daily_run_time", "07:30")),
        max_items_per_run=int(global_cfg.get("max_items_per_run", 50)),
        max_findings_after_dedup=int(global_cfg.get("max_findings_after_dedup", 15)),
        write_reports=bool(global_cfg.get("write_reports", True)),
        update_backlog=bool(global_cfg.get("update_backlog", True)),
        auto_modify_code=bool(global_cfg.get("auto_modify_code", False)),
        include_topics=[str(x) for x in filters_cfg.get("include_topics", [])],
        exclude_keywords=[str(x) for x in filters_cfg.get("exclude_keywords", [])],
        sources=sources,
        reports_dir=str(output_cfg.get("reports_dir", "docs/daily-research")),
        backlog_file=str(output_cfg.get("backlog_file", "docs/IMPROVEMENT_BACKLOG.md")),
        watchlist_file=str(output_cfg.get("watchlist_file", "docs/INNOVATION_WATCHLIST.md")),
    )


def _parse_minimal_yaml(text: str) -> dict[str, Any]:
    """Very small parser for the project config shape.

    Supports:
    - top-level mappings;
    - nested mappings by indentation;
    - lists of scalars;
    - lists of dictionaries under `sources`.
    """
    result: dict[str, Any] = {}
    current_section: str | None = None
    current_subsection: str | None = None
    current_source: dict[str, Any] | None = None
    current_list_key: str | None = None

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        indent = len(line) - len(line.lstrip(" "))

        if indent == 0 and stripped.endswith(":"):
            current_section = stripped[:-1]
            result.setdefault(current_section, [] if current_section == "sources" else {})
            current_subsection = None
            current_source = None
            current_list_key = None
            continue

        if current_section is None:
            continue

        if current_section == "sources":
            if indent == 2 and stripped.startswith("- "):
                current_source = {}
                result.setdefault("sources", []).append(current_source)
                key, value = _split_key_value(stripped[2:])
                if key:
                    current_source[key] = _parse_scalar(value)
                current_list_key = None
                continue
            if current_source is not None and indent == 4:
                if stripped.endswith(":"):
                    current_list_key = stripped[:-1]
                    current_source[current_list_key] = []
                    continue
                key, value = _split_key_value(stripped)
                if key:
                    current_source[key] = _parse_scalar(value)
                continue
            if current_source is not None and indent == 6 and stripped.startswith("- ") and current_list_key:
                current_source.setdefault(current_list_key, []).append(_parse_scalar(stripped[2:]))
                continue

        section_value = result.setdefault(current_section, {})
        if not isinstance(section_value, dict):
            continue

        if indent == 2 and stripped.endswith(":"):
            current_subsection = stripped[:-1]
            section_value[current_subsection] = []
            current_list_key = current_subsection
            continue

        if indent == 2:
            key, value = _split_key_value(stripped)
            if key:
                section_value[key] = _parse_scalar(value)
                current_list_key = key if value == "" else None
            continue

        if indent == 4 and stripped.startswith("- ") and current_list_key:
            existing = section_value.setdefault(current_list_key, [])
            if isinstance(existing, list):
                existing.append(_parse_scalar(stripped[2:]))
            continue

        if indent == 4 and current_subsection:
            subsection = section_value.setdefault(current_subsection, {})
            if isinstance(subsection, dict):
                key, value = _split_key_value(stripped)
                if key:
                    subsection[key] = _parse_scalar(value)

    return result


def _split_key_value(text: str) -> tuple[str, str]:
    if ":" not in text:
        return text.strip(), ""
    key, value = text.split(":", 1)
    return key.strip(), value.strip()


def _parse_scalar(value: str) -> Any:
    value = value.strip()
    if not value:
        return ""
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1]
    lowered = value.lower()
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    try:
        if "." in value:
            return float(value)
        return int(value)
    except ValueError:
        return value
