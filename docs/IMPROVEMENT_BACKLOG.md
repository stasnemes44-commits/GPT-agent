# Improvement Backlog

## Призначення
Це не список всього підряд, а curated backlog того, що вже пройшло щоденну аналітичну систему і має сенс для подальшої перевірки.

---

## Правила
- сюди потрапляють лише items із `adopt_full` або сильним `adopt_partial`;
- кожен item має мати джерело походження зі щоденного звіту;
- item не означає автоматичну імплементацію;
- перед кодовими змінами потрібен окремий implementation decision.

---

## Статуси
- `candidate`
- `validated`
- `scheduled`
- `spike`
- `implemented`
- `rejected`

---

## Шаблон запису

```md
## [ID] Назва покращення
- Статус: candidate
- Проєкт: OpenClaw / AIRYS / Medical / Automation
- Походження: daily-research/YYYY-MM-DD.md
- Тип: architecture / UX / memory / workflow / metrics / voice / browser
- Причина цінності:
- Що саме беремо:
- Що НЕ беремо:
- Мінімальний spike:
- Ризик:
- Очікуваний виграш:
- Власник:
```

---

## Активні кандидати

## [IB-001] Побудувати daily report generator
- Статус: candidate
- Проєкт: OpenClaw
- Походження: initial system design
- Тип: workflow
- Причина цінності: дає стабільний щоденний артефакт і дисциплінує весь цикл
- Що саме беремо: автоматичне створення markdown-звіту з секціями findings, verdict, backlog candidates
- Що НЕ беремо: автозміну коду чи автосинхронізацію з production
- Мінімальний spike: Python script, який з json findings формує markdown-файл
- Ризик: низький
- Очікуваний виграш: щоденна видимість і накопичення корисних ідей
- Власник: me

## [IB-002] Додати canonical finding schema
- Статус: candidate
- Проєкт: OpenClaw
- Походження: initial system design
- Тип: architecture
- Причина цінності: без єдиної сутності система швидко перетвориться на хаос
- Що саме беремо: фіксовану структуру normalized finding
- Що НЕ беремо: занадто ранню over-engineering схему на десятки полів
- Мінімальний spike: json schema + 3 приклади finding objects
- Ризик: низький
- Очікуваний виграш: стабільність пайплайна
- Власник: me

## [IB-003] Додати weekly synthesis report
- Статус: candidate
- Проєкт: OpenClaw
- Походження: architecture phase 2
- Тип: workflow
- Причина цінності: щоденні звіти без тижневого синтезу накопичують шум
- Що саме беремо: weekly summary з найкращими ідеями і трендами
- Що НЕ беремо: важкий аналітичний дашборд на старті
- Мінімальний spike: скрипт, який читає 7 markdown-звітів і створює weekly файл
- Ризик: низький
- Очікуваний виграш: кращий signal-to-noise
- Власник: me
