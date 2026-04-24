# Anti-Pattern: Prompt-as-Runtime

## Summary

This anti-pattern appears when core system behavior is governed primarily by a large prompt instead of a controlled runtime layer.

The prompt starts carrying:
- business rules
- mutation rules
- safety policy
- routing logic
- retry behavior
- escalation logic
- state assumptions

At that point, the prompt is no longer helping the runtime.
It is trying to be the runtime.

## Why it happens

It often appears because:
- prompt changes feel fast
- teams want to avoid writing explicit control logic
- demos look impressive early
- the system has not yet developed a real architecture boundary

## Why it is dangerous

Prompt-as-runtime leads to:
- hidden business logic
- weak testability
- fragile consistency across changes
- poor auditability
- unclear ownership of system decisions
- high risk of unexpected behavior after prompt edits

## Typical symptoms

Signs this anti-pattern is present:
- core workflow behavior changes dramatically after prompt tweaks
- business rules are easier to find in prompts than in code or canon docs
- state-changing actions depend mainly on natural-language instructions
- it is unclear what the real source of truth is
- the team says things like “the prompt handles that” for critical logic

## Why this fails operationally

Prompts are useful for:
- interpretation
- summarization
- extraction
- ranking
- drafting

They are weak as the main home for:
- state transitions
- policy enforcement
- permissions
- idempotency
- retries
- audit guarantees
- ownership logic

## Better alternative

Use prompts for reasoning support.
Use the runtime for authority.

Recommended split:
- prompt handles interpretation and proposal
- deterministic layer handles validation and policy
- execution layer handles mutation and observability

## Product risk

### Clinic Operations OS
Extremely dangerous.
This anti-pattern will eventually create booking mistakes, inconsistent operator behavior, and weak supportability.

### AIRYS
Also dangerous.
Without architectural boundaries, memory and proactive behavior become hard to trust over time.

## Rule

If a system becomes harder to reason about because too much behavior lives inside prompts, the architecture is moving in the wrong direction.

## Safer principle

Prompts should shape thinking, not secretly own the operating logic of the system.
