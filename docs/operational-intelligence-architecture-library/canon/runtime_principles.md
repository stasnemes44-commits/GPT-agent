# Runtime Principles

This document defines the baseline principles for any operational AI runtime built in this repository.

## 1. Runtime over prompt

The primary unit of system quality is runtime behavior, not prompt cleverness.

Questions to ask first:
- what actions can the system take
- under what conditions
- with what validation
- with what rollback or recovery path
- with what audit trail

## 2. Fail closed by default

If the system is uncertain about a state-changing action, it should avoid mutation and escalate or request verification.

Preferred order:
1. validate
2. constrain
3. execute
4. log
5. verify outcome

## 3. Deterministic boundary around the model

Language models may help with interpretation, summarization, classification, prioritization, and suggestion.
They must not be the only authority for transactional or stateful mutations.

A deterministic layer should own:
- validation
- state transitions
- permissions
- idempotency
- retries
- timeout handling
- ownership rules

## 4. Observable execution

Every meaningful action should produce traceable evidence.
At minimum:
- event id
- actor or session id
- timestamp
- action type
- inputs used
- outcome
- failure code if relevant

## 5. Human escalation is a system feature

Escalation is not a sign of weakness.
It is a designed safety mechanism.

A mature runtime must define:
- when human review is required
- when an operator can override
- how ownership transfers during handoff
- how pending work is resumed or closed

## 6. Recovery must be designed, not improvised

Every important workflow should define what happens if:
- the tool fails
- the external system times out
- the state is ambiguous
- a duplicate event arrives
- a partial mutation succeeds

## 7. State authority must be explicit

The runtime must define the source of truth for each stateful domain.
Examples:
- scheduling authority
- message state authority
- identity authority
- memory authority

## 8. Small bounded capabilities beat vague autonomy

Prefer narrow capabilities with explicit contracts over broad claims of autonomous behavior.

Good:
- validate booking mutation
- reconcile failed reminder delivery
- route escalation to operator queue

Bad:
- manage the clinic autonomously
- handle everything end to end without constraints

## 9. Production reality beats conceptual elegance

Architecture should improve operational outcomes.
If a design is elegant but fragile, slow, or impossible to support in real workflows, it is the wrong design.

## 10. Trust is cumulative

Users trust systems that are:
- predictable
- inspectable
- reversible where needed
- recoverable after failure
- respectful of boundaries

Operational trust is a core product asset.
