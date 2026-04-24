# Tool Execution Standard

This document defines how tools should be used inside an operational AI system.

Tools are where reasoning turns into impact.
That means tool execution needs stricter discipline than language generation.

## Core rule

The model may propose or prepare tool use.
The runtime must control whether and how the tool actually executes.

## Tool contract requirements

Every meaningful tool should define:
- purpose
- allowed inputs
- required inputs
- output schema
- side effects
- failure modes
- retryability
- idempotency expectations
- permission requirements

## Tool classes

### 1. Read-only tools
Examples:
- fetch schedule
- read contact details
- search logs
- retrieve documentation

Risk profile:
- lower risk
- can usually be model-invoked with runtime mediation
- still requires observability and rate discipline

### 2. State-changing tools
Examples:
- create booking
- cancel appointment
- send message
- update CRM record
- move workflow state

Risk profile:
- higher risk
- requires validation and policy checks
- usually requires idempotency and structured result logging

### 3. High-risk tools
Examples:
- destructive actions
- multi-party notifications
- financial operations
- cross-system data mutation

Risk profile:
- strict gating
- approval or extra validation often required
- stronger audit standards

## Execution sequence

Recommended order:
1. gather context
2. validate preconditions
3. check permissions and policy
4. assign idempotency key if relevant
5. execute tool
6. capture structured result
7. verify postcondition when possible
8. log outcome

## Required runtime controls

A strong execution layer should support:
- parameter validation
- schema normalization
- timeout control
- retry policy
- duplicate prevention
- permission checks
- outcome classification
- escalation path

## Result discipline

Tool results should be structured, not vague.

Prefer returning:
- success flag
- machine-readable status code
- human-readable summary
- entity identifiers affected
- next action hint
- retryability hint if failed

## Approval-gated execution

A tool should not execute automatically when:
- the mutation is user-visible and costly to reverse
- the inputs are ambiguous
- policy requires human review
- the downstream effect is broad or sensitive

## Anti-patterns

Avoid:
- letting prompts contain hidden tool policies
- vague tool schemas
- mutating state without structured result capture
- retrying dangerous mutations without idempotency
- treating all tools as equal risk

## Design outcome

Tool use should feel boring in the best possible way.
Predictable. Observable. Safe. Recoverable.
That is what lets an intelligent system act in the real world without becoming chaotic.
