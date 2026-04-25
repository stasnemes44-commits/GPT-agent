# n8n Daily Improvement Blueprint

## Purpose
Run the Daily Improvement System automatically every day and send a short summary to the owner.

This blueprint is intentionally implementation-focused, but not yet an importable n8n workflow JSON.

---

## Daily workflow

### 1. Cron Trigger
- Mode: every day
- Time: 07:30
- Timezone: Europe/Kyiv

### 2. Execute Command
Command:

```bash
cd /path/to/GPT-agent && daily-improvement daily --config config/research_sources.example.yaml --max-items 50 --json
```

Expected JSON output:

```json
{
  "run_date": "2026-04-25",
  "raw_items_count": 10,
  "findings_count": 6,
  "report_path": "docs/daily-research/2026-04-25.md",
  "backlog_updated": true,
  "created_backlog_items": 2,
  "errors": []
}
```

### 3. IF: run has errors
Condition:

```text
errors.length > 0
```

If true, send warning message.

### 4. Format Telegram Summary
Message template:

```text
Daily Improvement Run complete.

Date: {{$json.run_date}}
Raw items: {{$json.raw_items_count}}
Findings: {{$json.findings_count}}
Backlog items added: {{$json.created_backlog_items}}
Report: {{$json.report_path}}
Errors: {{$json.errors.length}}
```

### 5. Telegram Send Message
Send summary to your private Telegram chat.

---

## Weekly workflow

### 1. Cron Trigger
- Mode: every week
- Day: Sunday
- Time: 09:00
- Timezone: Europe/Kyiv

### 2. Execute Command
Command:

```bash
cd /path/to/GPT-agent && daily-improvement weekly --reports-dir docs/daily-research --week-label $(date +%G-W%V) --json
```

Expected JSON output:

```json
{
  "weekly_report_path": "docs/daily-research/weekly-2026-W17.md"
}
```

### 3. Telegram Send Message
Message:

```text
Weekly Improvement Synthesis is ready.

Report: {{$json.weekly_report_path}}
```

---

## Reliability rules

### Daily workflow
- Continue even if one source fails.
- Alert only when `errors.length > 0`.
- Do not auto-commit generated reports until Git sync policy is decided.
- Do not create PRs automatically.

### Weekly workflow
- Should run even if there are fewer than 7 daily reports.
- Should not delete or rewrite daily reports.

---

## Recommended future nodes

### Optional Git commit node
Only after manual approval policy exists.

Possible command:

```bash
git add docs/daily-research docs/IMPROVEMENT_BACKLOG.md && git commit -m "Add daily improvement report" && git push
```

Do not enable this until repo write policy is decided.

### Optional source health tracker
Track source failures by source ID and notify if the same source fails 3 days in a row.

### Optional backlog review workflow
Once per week, send backlog candidates and ask for manual selection.

---

## Why this design is safe
- n8n only orchestrates.
- Python owns deterministic logic.
- Markdown remains the source of traceable decisions.
- Human decision gate remains before implementation.
