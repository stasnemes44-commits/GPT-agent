# Handoff Protocol

This document defines the minimum protocol for transferring work between automated runtime components and human operators.

Handoff is not an exception.
In serious systems, it is a first-class operational capability.

## Core objectives

A handoff protocol exists to:
- stop unsafe or ambiguous autonomous execution
- preserve continuity of work
- make ownership explicit
- avoid dropped tasks and duplicate effort
- support clean resumption or closure

## When handoff should trigger

A workflow should hand off when one or more of the following is true:
- required data is missing and cannot be safely inferred
- business rules conflict or remain ambiguous
- a high-risk mutation requires approval
- identity or ownership cannot be validated
- the user is upset, confused, or requests a person
- repeated failure suggests automation should stop
- external system state is inconsistent

## Required handoff record

A valid handoff should create a structured record with at least:
- handoff id
- source workflow or system component
- current state
- reason code
- severity or urgency
- relevant context summary
- linked actor/session/entity ids
- timestamp
- current owner
- next expected action

## Ownership states

The system should make ownership explicit.

Recommended states:
- `runtime_owned`
- `pending_operator_acceptance`
- `operator_owned`
- `waiting_on_external_party`
- `returned_to_runtime`
- `closed`

A handoff without ownership state is incomplete.

## Lifecycle

### 1. Create handoff
Runtime creates the handoff record and stops unsafe progression.

### 2. Accept handoff
An operator explicitly accepts ownership.
No hidden or assumed acceptance.

### 3. Work the case
The operator may:
- request more data
- perform the action manually
- override a blocked state
- redirect to another queue
- close as not actionable

### 4. Return or close
After intervention, the case should either:
- return to runtime with a clear next state
- remain operator-owned until finished
- close with resolution status

## Reason code discipline

Reason codes should be normalized.
Examples:
- `missing_required_data`
- `ownership_unverified`
- `approval_required`
- `customer_requested_human`
- `external_system_conflict`
- `repeated_execution_failure`
- `policy_block`

## Operator experience requirements

A useful handoff must be understandable in under a minute.
The operator should immediately see:
- what happened
- why automation stopped
- what is blocked
- what action is expected
- what systems or users are affected

## Return-to-runtime rules

Return should happen only if:
- ambiguity is resolved
- required fields are present
- ownership is clear
- the system can continue safely
- the next state transition is valid

## Anti-patterns

Bad handoff behavior includes:
- sending vague transcripts with no summary
- no ownership state
- no reason code
- no clear next action
- automation continuing after escalation
- unresolved cases disappearing from view

## Design principle

The best handoff feels like controlled transfer of work, not abandonment.
That is one of the clearest signs that a system is operationally mature.
