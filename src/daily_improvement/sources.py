from __future__ import annotations

import json
from pathlib import Path

from .models import RawItem


class SourceLoadError(RuntimeError):
    """Raised when a source file cannot be loaded."""


def load_raw_items_from_json(path: str | Path) -> list[RawItem]:
    file_path = Path(path)
    if not file_path.exists():
        raise SourceLoadError(f"Source file not found: {file_path}")

    try:
        payload = json.loads(file_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SourceLoadError(f"Invalid JSON in {file_path}: {exc}") from exc

    if not isinstance(payload, list):
        raise SourceLoadError("Expected top-level JSON array of raw items")

    items: list[RawItem] = []
    for index, row in enumerate(payload):
        if not isinstance(row, dict):
            raise SourceLoadError(f"Item #{index} is not an object")
        items.append(
            RawItem(
                source=str(row.get("source", "unknown")),
                title=str(row.get("title", "")).strip(),
                url=str(row.get("url", "")).strip(),
                published_at=row.get("published_at"),
                summary_raw=str(row.get("summary_raw", "")).strip(),
                topic_guess=list(row.get("topic_guess", [])),
                source_type=str(row.get("source_type", "unknown")),
                source_category=str(row.get("source_category", "unknown")),
            )
        )
    return items
