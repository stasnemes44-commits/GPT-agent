# Idempotent Mutation Wrapper

## Pattern summary

This pattern places an idempotency wrapper around any state-changing action so the same intended mutation is not applied more than once.

In operational systems, this is not optional hygiene.
It is one of the foundations of trust.

## Problem solved

Real systems encounter:
- duplicate inbound events
- user retries
- network retries
- webhook redelivery
- unclear success responses
- repeated operator actions

Without idempotency protection, these conditions create duplicate mutations.

## Typical risks prevented

This pattern helps prevent:
- duplicate bookings
- duplicate reminders or messages
- repeated status transitions
- double cancellation
- conflicting downstream state

## Pattern structure

### 1. Define mutation intent
The runtime defines the intended mutation clearly.

Examples:
- create booking for actor X in slot Y
- send reminder Z for appointment A
- cancel appointment B initiated by actor C

### 2. Build idempotency key
The system generates or receives a stable key that represents the intended action.

A strong key may include:
- actor id
- entity id
- action type
- normalized target state
- bounded time scope when appropriate

### 3. Check existing execution record
Before mutating, the runtime checks whether the same action has already completed or is in progress.

### 4. Execute once
If not already completed, execute the mutation and record the result.

### 5. Return consistent result
If the same request appears again, return the same logical result instead of replaying the mutation.

## Why it matters

Idempotency is one of the clearest separations between:
- demo logic
and
- production-grade operational design

## When to use it

Use around:
- bookings
- cancellations
- state transitions
- notifications
- webhooks
- queue-driven actions
- approval-triggered mutations

## Controls required

Recommended controls:
- stable key construction
- execution status store
- clear success/failure/in-progress states
- timeout and stuck-execution handling
- reconciliation path for ambiguous outcomes

## Failure modes to watch

- weak idempotency key design
- no distinction between same-intent and new-intent requests
- storing only success and ignoring in-progress state
- replaying after unknown outcome without reconciliation

## Product relevance

### Clinic Operations OS
Extremely high relevance.
This should be standard around booking and messaging mutations.

### AIRYS
High relevance for user-facing actions, reminders, and recurring workflow events.

## Extracted principle

Every meaningful mutation should be protected so repeated intent does not create repeated reality.
