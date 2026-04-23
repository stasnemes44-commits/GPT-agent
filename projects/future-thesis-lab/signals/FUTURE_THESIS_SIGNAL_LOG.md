# FUTURE THESIS SIGNAL LOG

## Purpose
Тут фіксуються сильні сигнали, які можуть вплинути на future thesis.

## How to use
Кожен signal має пройти коротку оцінку:
- source
- category
- signal strength
- relevance to thesis
- likely action: ignore / watch / escalate / ADR

## Current baseline signals

### Signal 001
- Category: agent infrastructure
- Observation: великі моделі і платформи рухаються до computer-use / tool-use / action-taking agents
- Relevance: дуже висока
- Why it matters: майбутнє зміщується від “чату” до “дії”, що напряму підтримує care execution thesis
- Action: watch continuously

### Signal 002
- Category: healthcare workflow
- Observation: прості ambient notes / transcription швидко комодитизуються
- Relevance: дуже висока
- Why it matters: thesis має стояти не на note generation, а на guided action + navigation + follow-through
- Action: canonical reminder

### Signal 003
- Category: privacy / architecture
- Observation: local-first і private agent patterns стають дедалі важливішими
- Relevance: висока
- Why it matters: для health equity і trust privacy — це не бонус, а частина продуктового фундаменту
- Action: watch and integrate into architecture decisions

## Rule
Signal сам по собі не змінює thesis.
Thesis змінюється лише через явне рішення, review або ADR.
