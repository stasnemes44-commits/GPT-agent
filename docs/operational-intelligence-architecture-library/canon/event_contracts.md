# Event Contracts

This document defines the role of event contracts in operational AI systems.

Event discipline is one of the core foundations of runtime quality.
If inputs arrive in inconsistent shape, the rest of the system becomes fragile.

## Core rule

All important inbound and internal events should conform to explicit contracts.

The contract should define:
- required fields
- optional fields
- identifiers
- timestamps
- provenance
- actor/session linkage
- payload shape
- validation rules

## Why event contracts matter

They make it possible to:
- normalize multi-channel systems
- reduce downstream branching chaos
- support tracing and replay
- validate before execution
- build reliable analytics and observability

## Recommended event envelope

Every event should include a standard envelope with at least:
- `event_id`
- `event_type`
- `event_version`
- `occurred_at`
- `received_at`
- `source_system`
- `channel`
- `actor_id` or equivalent identifier
- `session_id` if relevant
- `correlation_id` if available
- `payload`
- `raw_reference` or original payload storage reference

## Event qualities

A good event contract is:
- explicit
- versioned
- validated at entry
- stable enough for downstream consumers
- clear about source provenance

## Versioning rule

Event contracts should be versioned whenever shape changes could affect downstream behavior.
Do not rely on hidden assumptions in consumers.

## Validation at entry

Before an event enters the main runtime, validate:
- required identifiers exist
- timestamps are parseable
- source/channel are known
- payload type is expected
- critical fields are within allowed ranges

Invalid events should go to an inspection lane, not silently flow through.

## Correlation and traceability

Strong contracts support linking events across workflow stages.

Useful identifiers:
- event id
- correlation id
- conversation id
- job id
- booking id
- actor id
- handoff id

## Multi-channel principle

When multiple channels feed the same runtime, normalize early.
The runtime should not carry channel-specific chaos deep into business logic.

## Anti-patterns

Avoid:
- passing raw channel payloads deep into the system
- inconsistent field names for the same concept
- missing versioning
- missing timestamps
- missing provenance
- hidden assumptions about optional fields

## Design outcome

A mature event contract makes the runtime calmer.
It allows interpretation, validation, mutation, and observability layers to speak a common language.
That is one of the clearest markers of production-grade architecture.
