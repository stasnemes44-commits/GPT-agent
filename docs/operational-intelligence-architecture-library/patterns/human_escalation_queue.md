# Human Escalation Queue

## Pattern summary

This pattern creates an explicit queue for cases that automation should not finish alone.

The queue is not a dumping ground for failures.
It is a designed collaboration surface between runtime and humans.

## Problem solved

Without a structured escalation queue:
- ambiguous cases disappear
- operators lack ownership clarity
- the system keeps retrying the wrong thing
- users lose trust when no one takes over properly

## Pattern structure

### 1. Trigger escalation
A workflow identifies a condition that should stop autonomous progression.

Common triggers:
- missing required data
- policy conflict
- upset user
- ownership mismatch
- external state ambiguity
- repeated technical failure

### 2. Create structured queue item
The system creates a normalized queue item with:
- escalation id
- source workflow
- reason code
- severity
- affected entity ids
- context summary
- current state
- recommended next action
- timestamp

### 3. Set ownership state
The runtime marks the work as awaiting human acceptance or human ownership.

### 4. Support operator action
The queue should support:
- accept
- reassign
- resolve manually
- request more info
- return to runtime
- close

### 5. Preserve traceability
The queue item should remain linked to the workflow, event history, and affected entities.

## Why it matters

A strong escalation queue:
- turns ambiguity into visible work
- prevents silent workflow loss
- supports accountability
- improves operational trust
- creates a clean surface for human collaboration

## When to use it

Use it when:
- automation frequently encounters ambiguity
- human review is part of business reality
- workflows affect real customers, schedules, or revenue
- runtime needs a safe off-ramp

## Controls required

Recommended controls:
- normalized reason codes
- explicit ownership states
- queue priority rules
- SLA or aging visibility
- resolution status tracking
- return-to-runtime validation rules

## Failure modes to watch

- vague queue items with no next action
- no acceptance lifecycle
- queue overload from poor trigger discipline
- automation continuing after escalation
- unresolved items losing visibility

## Product relevance

### Clinic Operations OS
Extremely high relevance.
This should be a core operational surface for admins and operators.

### AIRYS
Moderate to high relevance for higher-sensitivity support cases, boundary-triggered interventions, or user-requested human contact.

## Extracted principle

When automation should stop, the work must become visible, owned, and actionable by a human.
