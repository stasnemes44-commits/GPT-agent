# Phase 1 Executable MVP Runbook

## What this phase gives
This phase turns the daily improvement system from planning documents into a runnable pipeline.

It can:
- load raw research items from JSON;
- normalize them into canonical findings;
- deduplicate repeated findings;
- score each finding;
- map useful findings to projects;
- generate a daily markdown report;
- update the improvement backlog.

---

## Install

```bash
python -m pip install -e .[dev]
```

---

## Run with the sample fixture

```bash
daily-improvement --source data/daily_improvement/sample_raw_items.json --run-date 2026-04-25 --json
```

Alternative module run:

```bash
python -m daily_improvement.cli --source data/daily_improvement/sample_raw_items.json --run-date 2026-04-25 --json
```

---

## Expected outputs

Daily report:

```text
docs/daily-research/2026-04-25.md
```

Backlog update:

```text
docs/IMPROVEMENT_BACKLOG.md
```

---

## Input format

The input JSON must be an array of objects:

```json
[
  {
    "source": "official_blog",
    "title": "Example title",
    "url": "https://example.com/item",
    "published_at": "2026-04-25T07:30:00Z",
    "summary_raw": "Short summary of the item.",
    "topic_guess": ["agents", "workflow"],
    "source_type": "blog",
    "source_category": "official"
  }
]
```

---

## Current limitations

This is Phase 1, so it intentionally does not yet include:
- live RSS fetching;
- live GitHub release fetching;
- semantic deduplication;
- LLM-based deep assessment;
- n8n scheduler;
- Telegram notification.

Those belong to Phase 2.

---

## Phase 1 acceptance criteria

Phase 1 is considered complete when:
- the CLI runs without manual edits;
- the sample fixture produces a markdown report;
- backlog updates are idempotent enough to avoid obvious duplicate IDs;
- CI runs the CLI smoke check;
- future agents can understand how to extend the system from this runbook.

---

## Next phase

Phase 2 should add:
- real RSS source collector;
- GitHub release collector;
- n8n scheduled workflow;
- Telegram summary;
- weekly synthesis.
