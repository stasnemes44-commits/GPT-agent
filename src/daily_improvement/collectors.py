from __future__ import annotations

import json
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from typing import Iterable

from .config import ResearchConfig, SourceConfig
from .models import RawItem


@dataclass(slots=True)
class CollectionResult:
    raw_items: list[RawItem] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)


def collect_from_config(config: ResearchConfig) -> CollectionResult:
    result = CollectionResult()
    for source in config.sources:
        if not source.enabled:
            continue
        try:
            if source.type == "rss" and source.url:
                result.raw_items.extend(collect_rss(source))
            elif source.type == "github_releases":
                repos = list(_iter_repos(source))
                for repo in repos:
                    result.raw_items.extend(collect_github_releases(source, repo))
            else:
                result.errors.append(f"Unsupported or incomplete source: {source.id} ({source.type})")
        except Exception as exc:  # source failure must not kill the whole pipeline
            result.errors.append(f"{source.id}: {exc}")
    return result


def collect_rss(source: SourceConfig, limit: int = 10) -> list[RawItem]:
    if not source.url:
        return []
    payload = _fetch_url(source.url)
    root = ET.fromstring(payload)
    channel_items = root.findall(".//item")
    atom_entries = root.findall("{http://www.w3.org/2005/Atom}entry")

    raw_items: list[RawItem] = []
    for item in channel_items[:limit]:
        title = _text(item, "title")
        link = _text(item, "link")
        description = _text(item, "description") or _text(item, "summary")
        published = _normalize_date(_text(item, "pubDate") or _text(item, "published"))
        if title and link:
            raw_items.append(
                RawItem(
                    source=source.id,
                    title=title,
                    url=link,
                    published_at=published,
                    summary_raw=description,
                    topic_guess=[],
                    source_type="rss",
                    source_category=source.category,
                )
            )

    for entry in atom_entries[:limit]:
        title = _text(entry, "{http://www.w3.org/2005/Atom}title")
        link = _atom_link(entry)
        summary = _text(entry, "{http://www.w3.org/2005/Atom}summary") or _text(entry, "{http://www.w3.org/2005/Atom}content")
        published = _normalize_date(
            _text(entry, "{http://www.w3.org/2005/Atom}published")
            or _text(entry, "{http://www.w3.org/2005/Atom}updated")
        )
        if title and link:
            raw_items.append(
                RawItem(
                    source=source.id,
                    title=title,
                    url=link,
                    published_at=published,
                    summary_raw=summary,
                    topic_guess=[],
                    source_type="rss",
                    source_category=source.category,
                )
            )

    return raw_items[:limit]


def collect_github_releases(source: SourceConfig, repo: str, limit: int = 5) -> list[RawItem]:
    api_url = f"https://api.github.com/repos/{repo}/releases?per_page={limit}"
    payload = _fetch_url(api_url, accept="application/vnd.github+json")
    releases = json.loads(payload)
    if not isinstance(releases, list):
        return []

    raw_items: list[RawItem] = []
    for release in releases[:limit]:
        if not isinstance(release, dict):
            continue
        title = str(release.get("name") or release.get("tag_name") or "").strip()
        url = str(release.get("html_url") or "").strip()
        body = str(release.get("body") or "").strip()
        published_at = release.get("published_at") or release.get("created_at")
        if title and url:
            raw_items.append(
                RawItem(
                    source=source.id,
                    title=f"{repo}: {title}",
                    url=url,
                    published_at=str(published_at) if published_at else None,
                    summary_raw=body[:1200],
                    topic_guess=[],
                    source_type="github_release",
                    source_category=source.category,
                )
            )
    return raw_items


def _iter_repos(source: SourceConfig) -> Iterable[str]:
    if source.repo:
        yield source.repo
    for repo in source.repos:
        yield repo


def _fetch_url(url: str, accept: str | None = None, timeout: int = 20) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "daily-improvement-system/0.1"})
    if accept:
        request.add_header("Accept", accept)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"HTTP {exc.code} for {url}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"URL error for {url}: {exc.reason}") from exc


def _text(node: ET.Element, tag: str) -> str:
    found = node.find(tag)
    if found is None or found.text is None:
        return ""
    return " ".join(found.text.split())


def _atom_link(node: ET.Element) -> str:
    for link in node.findall("{http://www.w3.org/2005/Atom}link"):
        href = link.attrib.get("href")
        if href:
            return href
    return ""


def _normalize_date(value: str) -> str | None:
    if not value:
        return None
    try:
        parsed = parsedate_to_datetime(value)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc).isoformat()
    except Exception:
        pass
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc).isoformat()
    except Exception:
        return value
