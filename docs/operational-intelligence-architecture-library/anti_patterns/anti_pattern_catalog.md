# Anti-Pattern Catalog

This document records dangerous design tendencies that weaken operational AI systems.

## 1. Prompt-as-runtime
Business logic lives mainly in a giant prompt instead of a controlled execution layer.

Why dangerous:
- hard to audit
- brittle under change
- weak validation
- invisible failure modes

## 2. Autonomous mutation without gates
The model can create, change, or delete state without deterministic validation.

Why dangerous:
- unsafe actions
- duplicate mutations
- poor accountability

## 3. No clear source of truth
Multiple systems appear to own the same state without reconciliation.

Why dangerous:
- state drift
- conflicting outputs
- operator confusion

## 4. Hidden retries
The system silently retries mutations without visibility or idempotency controls.

Why dangerous:
- duplicate actions
- noisy incidents
- hard-to-debug outcomes

## 5. Handoff without ownership transfer
A workflow escalates to a human, but no explicit ownership or lifecycle state is recorded.

Why dangerous:
- dropped tasks
- duplicated work
- unresolved conversations

## 6. Channel-specific chaos
Each channel behaves like a separate system with custom logic everywhere.

Why dangerous:
- maintenance explosion
- inconsistent behavior
- weak reporting

## 7. Context accumulation without hierarchy
The system stores everything as if all context were equally important.

Why dangerous:
- context poisoning
- weak prioritization
- unstable decisions over time

## 8. Logging only on failure
Successful actions are not logged with enough detail.

Why dangerous:
- invisible history
- weak debugging
- low trust after incidents

## 9. Retry instead of recovery design
The system responds to every failure mainly by retrying.

Why dangerous:
- retry storms
- repeated mutations
- no path to reconciliation

## 10. Demo-first architecture
The system is designed mainly to look intelligent rather than stay correct in production.

Why dangerous:
- misleading confidence
- operational fragility
- poor long-term maintainability

## Rule

Whenever one of these anti-patterns appears in research or implementation, it should be recorded with:
- source
- symptom
- likely failure mode
- safer alternative
