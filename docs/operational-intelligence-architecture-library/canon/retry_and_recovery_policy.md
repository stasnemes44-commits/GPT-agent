# Retry and Recovery Policy

This document defines how operational AI systems should respond to failure.

A mature system does not treat retry as the universal answer.
Retry is one tool inside a broader recovery design.

## Core rule

Retry should be controlled, visible, and safe.
Recovery should be designed explicitly for each important workflow.

## Failure classes

### 1. Transient technical failure
Examples:
- network timeout
- temporary API failure
- rate limiting
- short-lived service unavailability

Typical response:
- bounded retry
- backoff
- idempotency protection
- structured logging

### 2. Persistent execution failure
Examples:
- malformed payload
- invalid credentials
- broken integration mapping
- unsupported external response

Typical response:
- stop retrying early
- raise incident or queue item
- require operator or engineering intervention

### 3. Ambiguous state failure
Examples:
- request may have succeeded but confirmation missing
- external system state unclear
- partial mutation observed

Typical response:
- reconcile against source of truth
- avoid blind repeat mutation
- escalate if ambiguity remains

### 4. Policy or validation failure
Examples:
- missing required field
- ownership mismatch
- blocked business rule
- approval missing

Typical response:
- no retry
- surface explicit reason code
- request missing action or escalate

## Retry policy baseline

Retries should define:
- which actions are retryable
- maximum attempts
- backoff strategy
- timeout boundaries
- idempotency key behavior
- stop conditions

## Recommended guardrails

### Do retry when:
- the failure is likely transient
- idempotency is enforced
- the action is safe to repeat
- the state authority can later verify outcome

### Do not retry when:
- the cause is policy-related
- ownership is unclear
- the mutation may already have succeeded
- repeated retries could create duplicates or confusion

## Recovery design requirements

Every important workflow should specify:
- failure categories
- retryable steps
- reconciliation method
- dead-letter path
- escalation rules
- final failure visibility

## Dead-letter lane

When automatic recovery is not safe or not successful, work should move to a visible dead-letter or exception lane.

The dead-letter record should include:
- original event id
- workflow name
- failure type
- last known state
- attempts made
- recommended next action
- relevant payload summary

## Reconciliation principle

When outcome is uncertain, reconcile before mutating again.

This is critical for:
- bookings
- messages
- notifications
- financial actions
- workflow state transitions

## Anti-patterns

Avoid:
- infinite retries
- invisible retries
- retrying policy failures
- replaying ambiguous mutations without reconciliation
- using retry instead of operator escalation

## Design outcome

A strong system fails in a controlled way.
It either recovers safely, escalates clearly, or stops with visible evidence.
That is more important than pretending the workflow never breaks.
