# Phase 2 Live Sources Runbook

## Goal
Move the Daily Improvement System from sample JSON mode to real daily operation with live sources.

---

## What Phase 2 adds
- Config loader from `config/research_sources.example.yaml`.
- RSS collector.
- GitHub releases collector.
- Daily CLI subcommand.
- Weekly synthesis CLI subcommand.
- CI smoke checks for daily and weekly commands.

---

## Install

```bash
python -m pip install -e .[dev]
```

---

## Run sample mode

```bash
daily-improvement daily \
  --source data/daily_improvement/sample_raw_items.json \
  --run-date 2026-04-25 \
  --json
```

---

## Run live config mode

```bash
daily-improvement daily \
  --config config/research_sources.example.yaml \
  --max-items 50 \
  --json
```

This uses live collectors configured in the YAML file.

---

## Run weekly synthesis

```bash
daily-improvement weekly \
  --reports-dir docs/daily-research \
  --week-label 2026-W17 \
  --json
```

Expected output:

```text
docs/daily-research/weekly-2026-W17.md
```

---

## Safety rules
- Live source failure must not fail the whole run.
- Failed source errors are stored in the pipeline result.
- Backlog update remains manual-gated.
- No code is changed automatically.
- No pull requests are opened automatically.

---

## Current live collectors

### RSS
Supports common RSS and Atom feeds.

### GitHub releases
Supports public GitHub releases through:

```text
https://api.github.com/repos/{owner}/{repo}/releases
```

---

## Recommended n8n orchestration

Daily:
1. Cron at 07:30 Europe/Kyiv.
2. Execute command:

```bash
cd /path/to/GPT-agent && daily-improvement daily --config config/research_sources.example.yaml --max-items 50 --json
```

3. Parse JSON result.
4. If errors exist, send warning.
5. Send short Telegram summary with report path and counts.

Weekly:
1. Cron every Sunday at 09:00 Europe/Kyiv.
2. Execute command:

```bash
cd /path/to/GPT-agent && daily-improvement weekly --reports-dir docs/daily-research --week-label $(date +%G-W%V) --json
```

3. Send weekly report path to Telegram.

---

## Quality gates
A daily run is good when:
- raw_items_count > 0;
- findings_count > 0;
- report_path exists;
- created_backlog_items does not explode every day;
- errors are limited and understandable.

A weekly run is good when:
- it reviews up to 7 latest daily reports;
- it summarizes repeated topics;
- it lists verdict distribution;
- it asks human review questions.

---

## Known limitations
- Config parser is intentionally minimal and supports only the current config shape.
- Deduplication is URL/title-based, not semantic yet.
- Scoring is heuristic, not LLM-reviewed yet.
- Telegram and n8n JSON workflow are not implemented as runnable imports yet.

---

## Next improvements
- Add notification formatter.
- Add semantic deduplication.
- Add source quality ranking.
- Add local cache of collected raw items.
- Add real n8n importable workflow JSON.
