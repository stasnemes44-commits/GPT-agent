# Planner-Executor with Validation Gate

## Pattern summary

This pattern separates interpretation and planning from actual execution, while inserting an explicit validation gate before state-changing actions.

It is one of the most important baseline patterns for operational AI systems.

## Problem solved

Without this separation, the same component that interprets language may also mutate state directly.
That creates weak boundaries, poor auditability, and higher risk of unsafe or duplicated actions.

## Pattern structure

### 1. Planner
Responsible for:
- interpreting the request
- identifying likely intent
- proposing candidate actions
- extracting structured parameters
- identifying ambiguity

This layer may use an LLM.

### 2. Validation gate
Responsible for:
- checking required fields
- checking permissions and ownership
- enforcing policy
- blocking invalid or ambiguous mutations
- requiring approval when necessary

This layer should be deterministic wherever possible.

### 3. Executor
Responsible for:
- calling tools
- applying idempotency controls
- capturing results
- verifying postconditions where possible
- logging outcomes

## Why it matters

This pattern:
- keeps reasoning separate from authority
- prevents direct model-controlled mutation
- improves safety and trust
- makes handoff and escalation easier
- supports better observability

## When to use it

Use it when:
- language interpretation is needed before execution
- state changes affect real users or systems
- ambiguity is common
- policy checks matter
- recovery and auditability are important

## Deterministic controls required

Recommended controls:
- schema validation
- ownership checks
- permission checks
- idempotency keys
- explicit action classification
- structured result codes

## Failure modes to watch

- planner emits unclear or overly broad actions
- validation gate is too weak or bypassed
- executor lacks idempotency protection
- planner output and executor contract drift apart

## Anti-pattern it prevents

This pattern directly counters:
- prompt-as-runtime
- autonomous mutation without gates
- hidden policy logic inside prompts

## Product relevance

### Clinic Operations OS
Very high relevance.
Useful for booking actions, reminders, cancellations, confirmations, and escalation routing.

### AIRYS
High relevance.
Useful for bounded proactive actions, memory updates, and user-facing workflows that need trust.

## Extracted principle

Interpret with intelligence, but execute only through controlled validation and bounded authority.
