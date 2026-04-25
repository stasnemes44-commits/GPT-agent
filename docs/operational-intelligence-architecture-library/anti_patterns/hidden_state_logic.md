# Anti-Pattern: Hidden State Logic

## Summary

This anti-pattern appears when important system state exists implicitly across prompts, branch conditions, ad hoc variables, or loosely coordinated services instead of living in explicit, inspectable state models.

The system behaves as if it has state discipline.
In reality, too much of its state is hidden.

## Why it happens

It often appears because:
- early prototypes evolve without a formal state model
- teams rely on conversation context as de facto state
- multiple components infer status instead of reading authoritative state
- prompt logic carries assumptions that are never stored explicitly

## Why it is dangerous

Hidden state logic leads to:
- hard-to-debug behavior
- inconsistent transitions
- duplicated actions
- broken recovery after interruption
- unclear ownership during handoff
- weak operator visibility

## Typical symptoms

Signs this anti-pattern is present:
- nobody can quickly explain the current state of an entity or workflow
- the same workflow behaves differently depending on conversation path
- recovery after timeout or restart is unreliable
- handoffs require reading long transcripts to infer status
- important state exists only in memory, chat history, or prompt wording

## Operational failure modes

Common outcomes include:
- bookings stuck between tentative and confirmed
- escalations with unclear ownership
- retries running against the wrong assumed state
- operator confusion after partial failures
- different components acting on different versions of reality

## Better alternative

Use explicit state models.

Recommended controls:
- state tables or clearly modeled entities
- explicit status values
- valid transition rules
- source-of-truth definition
- lifecycle logging
- reconciliation support

## Product risk

### Clinic Operations OS
Extremely dangerous.
Scheduling, reminders, and handoff workflows require inspectable state.

### AIRYS
High risk.
Long-horizon continuity becomes unstable if important context and behavior rely on implicit state.

## Rule

If a workflow's status can only be understood by reconstructing context from scattered clues, the architecture is too implicit.

## Safer principle

Make important state visible, authoritative, and transition-safe instead of letting it hide inside conversational flow.
