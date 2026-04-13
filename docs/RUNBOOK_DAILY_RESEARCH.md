# Runbook — Daily Improvement System

## Мета
Описати, як запускати систему щоденного аналізу новинок стабільно і без хаосу.

---

## Рекомендований режим

### Daily run
- час: `07:30 Europe/Kyiv`
- мета: зібрати новинки за останню добу, оцінити, створити звіт, оновити backlog/watchlist

### Weekly synthesis
- день: неділя
- час: `09:00 Europe/Kyiv`
- мета: зібрати головні патерни тижня

---

## Мінімальний workflow

### Крок 1. Scheduler
Запускає daily flow один раз на день.

### Крок 2. Source Collector
Отримує raw items із налаштованих джерел.

### Крок 3. Normalizer
Приводить все до canonical finding schema.

### Крок 4. Deduplication
Прибирає дублікати і зводить подібні items.

### Крок 5. Scoring
Проставляє оцінки по `SCORING_RUBRIC.md`.

### Крок 6. Project Mapping
Мапить findings до OpenClaw / AIRYS / інших проєктів.

### Крок 7. Report Generator
Створює `docs/daily-research/YYYY-MM-DD.md`.

### Крок 8. Backlog Update
Оновлює `IMPROVEMENT_BACKLOG.md` тільки для сильних items.

### Крок 9. Notify
Опційно надсилає тобі короткий summary у Telegram або email.

---

## Найкраща практична реалізація

### Варіант A — n8n + Python
Рекомендований.

- `n8n`:
  - scheduler
  - fetch feeds / APIs
  - retry / logging
  - notifications
- `Python`:
  - canonical normalization
  - dedup
  - scoring
  - markdown generation

### Варіант B — pure Python + cron
Добре для локального або серверного мінімалістичного запуску.

---

## n8n-структура

### Основний flow
1. `Cron`
2. `Load config`
3. `Collect sources`
4. `Merge raw items`
5. `Execute Command` або `Code` для Python scoring pipeline
6. `Write artifacts`
7. `Send notification`

### Розбивка на сабфлоу
- `research_collect_sources`
- `research_normalize_findings`
- `research_score_findings`
- `research_generate_report`
- `research_update_backlog`
- `research_weekly_synthesis`

---

## Правила надійності

### Обов'язково
- idempotent daily run;
- safe rerun for same date;
- логувати кількість raw items, deduped findings і adopted items;
- не ламати backlog при порожньому запуску;
- не додавати дублікати backlog items;
- при помилці одного джерела не валити весь pipeline.

### Бажано
- окремий `run_id`;
- журнал помилок;
- alert, якщо findings = 0 кілька днів поспіль;
- alert, якщо одне джерело почало давати надто багато шуму.

---

## Очікувані виходи

### Щодня
- `docs/daily-research/YYYY-MM-DD.md`
- оновлений `IMPROVEMENT_BACKLOG.md`
- опційно оновлений `INNOVATION_WATCHLIST.md`

### Щотижня
- `docs/daily-research/weekly-YYYY-WW.md`

---

## Manual Gate
Після daily report дозволені лише такі дії:
- прочитати звіт;
- переглянути backlog candidates;
- вручну вибрати, що перетворити у spike;
- вручну вирішити, чи створювати issue або PR.

Заборонено:
- auto-merge;
- auto-refactor;
- auto-rewrite architecture.

---

## Критерії якості системи
Система працює добре, якщо:
- за день дає мало шуму;
- виділяє 1-3 сильні речі;
- backlog не роздувається сміттям;
- кожен verdict має пояснення;
- є чітка різниця між `adopt_partial`, `watch` і `ignore`.
