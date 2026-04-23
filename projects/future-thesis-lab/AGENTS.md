# AGENTS — Future Thesis Lab

## Роль модуля
`future-thesis-lab` — це окремий стратегічний модуль. Він не відповідає за щоденну операційну роботу, кодинг, дрібні таски або execution-by-default.

Він відповідає за:
- довгострокову thesis;
- відбір великих ставок;
- оцінку нових frontier signals;
- зменшення hype-driven drift;
- регулярний review майбутнього напряму.

## Як агент має використовувати цей модуль

### Використовувати часто, коли:
- користувач питає про нову велику нішу;
- потрібно оцінити нову AI / healthcare / human-impact ставку;
- потрібно провести monthly review;
- потрібно провести quarterly thesis review;
- потрібно вирішити, чи суперечить нова ідея довгостроковому north star;
- потрібно зафіксувати стратегічне рішення через ADR.

### Не використовувати як головний контекст, коли:
- виконується щоденний coding / debugging / ops;
- йдеться про локальну задачу без стратегічного значення;
- потрібне швидке execution рішення без thesis-level аналізу.

## Context loading policy

### Always-visible layer
Дозволено тримати постійно доступним лише короткий summary:
- головна thesis;
- 90/10 модель;
- список того, що точно не робимо;
- route rule, коли викликати цей модуль.

### On-demand layer
Підвантажувати лише за потреби:
- `context/FUTURE_THESIS_CANONICAL.md`
- `signals/FUTURE_THESIS_SIGNAL_LOG.md`
- `pain_repository/FUTURE_THESIS_PAIN_REPOSITORY.md`
- `watchlists/FUTURE_THESIS_WATCHLIST.md`
- `decisions/`
- `reviews/`

## Decision policy
Будь-яка нова велика ставка має бути оцінена за такими критеріями:
- масштаб людського болю;
- реальність технічного вікна можливості;
- anti-commodity resilience;
- unfair advantage користувача;
- time-to-desire;
- regulatory friction;
- path from thesis to product.

## Safety against drift
Агент не повинен:
- підміняти поточний бізнес майбутньою мрією;
- генерувати нові moonshots без порівняння з canonical thesis;
- зливати execution stack і future-thesis stack в один шумний контекст;
- множити дублікати тієї самої стратегічної ідеї в різних папках.

## Якщо знаходиться новий signal
1. Записати signal.
2. Оцінити його силу.
3. Визначити: ignore / watch / escalate / ADR.
4. Якщо signal змінює thesis-level картину — підготувати ADR або quarterly review note.

## Головне правило
Цей модуль має бути **часто використовуваним стратегічним інструментом**, але **не постійно активним повним контекстом**.
