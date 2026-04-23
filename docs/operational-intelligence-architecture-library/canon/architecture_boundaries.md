# Architecture Boundaries

This document defines the minimum boundary model for operational AI systems.

## Core rule

Do not let the model become the runtime.

A strong system separates reasoning from authority.

## Recommended layers

### 1. Interface layer
Responsible for:
- inbound messages
- channel normalization
- metadata capture
- response rendering

### 2. Interpretation layer
Responsible for:
- intent inference
- summarization
- extraction of structured signals
- ambiguity detection

This layer may use an LLM.

### 3. Policy and validation layer
Responsible for:
- permission checks
- required field validation
- safety rules
- ownership checks
- business constraints

This layer should be deterministic wherever possible.

### 4. Execution layer
Responsible for:
- tool calls
- workflow steps
- mutation requests
- retries
- timeout handling
- idempotency protections

### 5. State authority layer
Responsible for:
- accepted system of record
- state reconciliation
- conflict resolution
- versioned truth

### 6. Observability and recovery layer
Responsible for:
- logging
- audit history
- error classification
- replay and recovery
- operator inspection

## Boundary rules

### The model may
- interpret user language
- rank options
- summarize context
- classify inputs
- draft safe outputs
- propose next steps

### The model must not independently own
- transactional mutations
- irreversible actions
- authority over identity
- final scheduling state
- permission decisions without deterministic checks
- audit integrity

## Recommended design questions

Before adding any capability, ask:

1. What layer owns this decision?
2. What is the source of truth?
3. What validates the action?
4. What prevents duplication?
5. What logs the result?
6. What recovers from partial failure?
7. When is escalation required?

## Smell list

The architecture is weak if:
- the prompt carries business logic that should live in code
- the model can mutate state without validation
- the same action can fire twice from duplicate events
- no source of truth is defined
- there is no clean handoff to human operators
- failures are invisible until a user complains

## Desired outcome

The system should feel intelligent at the interface level and disciplined at the runtime level.
That combination is the foundation of an operational AI system that can be trusted.
