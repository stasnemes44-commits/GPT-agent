# Daily Improvement System Architecture

## Призначення
Побудувати повноцінну систему, яка щодня знаходить новинки, оцінює їхню придатність для:
- самого OpenClaw-агента;
- AIRYS;
- медичних агентів;
- автоматизацій та інших моїх проєктів.

Система повинна бути:
- керованою;
- пояснюваною;
- безпечною;
- придатною до щоденного запуску;
- без автоматичних самозмін коду без окремого рішення.

---

## Архітектурний принцип
Не "self-modifying agent", а **improvement intelligence system**:

1. збір зовнішніх сигналів;
2. нормалізація;
3. дедуплікація;
4. scoring;
5. витягування придатних патернів;
6. мапінг до моїх проєктів;
7. створення звіту;
8. формування backlog;
9. окремий manual gate перед імплементацією.

---

## Рівні системи

### Layer 1. Source Intake
Відповідає за збір сигналів із джерел.

Приклади джерел:
- офіційні анонси моделей;
- GitHub releases;
- changelog-и інструментів;
- агентні фреймворки;
- memory systems;
- browser / voice / workflow платформи;
- медичні AI-новинки;
- релевантні стартапи.

Вихід:
- масив сирих items з полями `source`, `title`, `url`, `published_at`, `summary_raw`, `topic_guess`.

### Layer 2. Canonical Normalization
Приводить усі items до єдиного формату.

Canonical item:
```json
{
  "id": "stable-content-hash",
  "source": "anthropic_blog",
  "title": "...",
  "url": "...",
  "published_at": "...",
  "summary": "...",
  "topics": ["agents", "memory", "voice"],
  "entity_names": ["Claude Managed Agents"],
  "evidence_strength": "official|secondary|social",
  "raw_type": "blog|release|tweet|news|doc"
}
```

### Layer 3. Dedup + Clustering
Мета:
- не дублювати одну й ту саму новину з 7 джерел;
- вміти звести кілька джерел до одного clustered finding.

Вихід:
- canonical findings;
- список supporting sources.

### Layer 4. Relevance + Scoring Engine
Оцінює кожен finding за шкалами.

Обов'язкові осі:
- relevance_openclaw;
- relevance_airys;
- relevance_medical_agents;
- practical_value;
- integration_effort;
- maturity;
- risk;
- partial_adoptability;
- business_impact;
- novelty.

Вихід:
- scorecard;
- verdict;
- short rationale.

### Layer 5. Pattern Extraction
Для кожної цікавої новинки система повинна відповісти:
- що саме тут сильне;
- це ціле рішення чи лише патерн;
- чи є там reusable component;
- чи можна взяти лише UX, лише memory-підхід, лише business scoring або лише orchestration.

### Layer 6. Project Mapping
Кожна корисна знахідка має бути змеплена до одного чи кількох проєктів:
- OpenClaw;
- AIRYS;
- clinic assistant;
- personal doctor assistant;
- sales / automation tools.

Для кожного проєкту:
- навіщо це;
- де саме в архітектурі це живе;
- який мінімальний test spike;
- який очікуваний виграш.

### Layer 7. Report Generation
Генерує щоденний markdown-звіт.

### Layer 8. Backlog Update
Оновлює backlog без автокодових змін.

### Layer 9. Human Decision Gate
Лише після людського рішення можна:
- створювати issue;
- робити spike;
- відкривати PR;
- змінювати код.

---

## Режими запуску

### Daily Run
Щоденний повний цикл.

### Weekly Synthesis
Щотижневе зведення:
- найкращі ідеї тижня;
- що повторюється у трендах;
- що переходить у backlog;
- що відкидається.

### Deep-Dive Mode
Окремий режим для одного об'єкта:
- продукт;
- модель;
- фреймворк;
- конкурент;
- стартап.

---

## Рекомендований стек

### Найкращий підхід для тебе
**Hybrid system**:
- orchestration: n8n;
- scoring / normalization / report generation: Python;
- knowledge outputs: markdown у repo;
- optional task creation: GitHub issues / backlog.

### Чому так
`n8n` сильний для:
- scheduler;
- connectors;
- routing;
- retries;
- notifications.

`Python` сильний для:
- нормалізації;
- дедуплікації;
- scoring;
- класифікації;
- побудови markdown-звітів.

---

## Потоки даних

```text
Sources
  -> collector
  -> canonical normalizer
  -> dedup clusterer
  -> scoring engine
  -> pattern extractor
  -> project mapper
  -> report generator
  -> markdown files
  -> backlog updater
  -> optional notification
```

---

## Мінімальні сутності

### Finding
Один канонічний сигнал.

### Assessment
Оцінка придатності finding.

### Recommendation
Конкретна рекомендація для проєкту.

### Experiment
Найменший тест, який варто зробити.

### Backlog Item
Одиниця роботи, що переходить до виконання.

---

## Формат verdict
Кожна знахідка мусить мати один з verdict:
- `adopt_full`
- `adopt_partial`
- `watch`
- `ignore`

Додатково:
- `time_horizon`: now / later / future
- `confidence`: low / medium / high

---

## Правила безпеки

### Обов'язково
- не змінювати код автоматично;
- не робити автоматичний merge;
- не піднімати hype вище за evidence;
- не переносити consumer-патерни в medical use без окремого фільтра;
- не копіювати архітектуру лише через популярність.

### Для медичних напрямків
Окремий жорсткий фільтр:
- safety impact;
- auditability;
- traceability;
- deterministic fallback;
- human override.

---

## Артефакти

```text
/docs
  DAILY_IMPROVEMENT_LOOP.md
  DAILY_IMPROVEMENT_SYSTEM_ARCHITECTURE.md
  SCORING_RUBRIC.md
  IMPROVEMENT_BACKLOG.md
  INNOVATION_WATCHLIST.md
  RUNBOOK_DAILY_RESEARCH.md
  /daily-research
    TEMPLATE.md
    YYYY-MM-DD.md
/config
  research_sources.example.yaml
```

---

## Фази реалізації

### Phase 1. Reporting System
- джерела;
- збір;
- scoring;
- markdown report.

### Phase 2. Structured Backlog
- backlog updater;
- weekly synthesis;
- ranking by project.

### Phase 3. Decision Support
- auto-generated experiment proposals;
- suggested implementation notes;
- GitHub issue drafts.

### Phase 4. Controlled Execution
- створення spike-задач;
- PR draft suggestions;
- manual-gated implementation.

---

## Що є успіхом
Система вважається корисною, якщо вона щодня дає:
- 1-3 дійсно корисні висновки;
- мінімум шуму;
- зрозумілий backlog;
- видимість, що варто брати повністю, частково або взагалі не чіпати.
