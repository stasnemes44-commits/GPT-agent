# Event Normalization Envelope

## Pattern summary

This pattern converts diverse inbound events into a consistent normalized envelope before deeper runtime processing begins.

It is especially important in omnichannel and multi-source systems.

## Problem solved

Different channels and systems produce payloads with:
- different field names
- different identity forms
- different timestamp formats
- missing metadata
- different retry behaviors
- different message semantics

If raw payloads flow deep into business logic, the runtime becomes fragmented and fragile.

## Pattern structure

### 1. Capture raw input
Preserve the original payload or a stable reference to it.

### 2. Normalize core metadata
Convert the input into a common structure.

Typical normalized fields:
- event id
- event type
- source system
- channel
- actor id
- session id if relevant
- occurred at
- received at
- payload summary or canonical payload
- correlation id if available
- raw reference

### 3. Add channel capabilities or flags
Store normalized channel constraints separately rather than mixing them into deeper business logic.

Examples:
- supports buttons
- time-window restrictions
- attachment support
- reply threading behavior

### 4. Validate before runtime entry
Reject or divert malformed events into inspection lanes.

## Why it matters

This pattern:
- reduces branching chaos
- improves observability
- enables replay and tracing
- supports cleaner business logic
- makes future channels easier to add

## When to use it

Use it when:
- more than one inbound channel exists
- external systems send inconsistent events
- reliable tracing matters
- downstream workflows depend on stable fields

## Controls required

Recommended controls:
- normalized schema versioning
- raw payload retention or reference
- actor/session mapping discipline
- validation at entry
- provenance logging

## Failure modes to watch

- normalization that loses important source data
- stuffing channel-specific quirks into generic fields
- inconsistent actor id generation across channels
- skipping raw reference storage

## Product relevance

### Clinic Operations OS
Extremely high relevance.
This should be foundational for Telegram, WhatsApp, Instagram, site chat, voice, and future channels.

### AIRYS
High relevance when context enters from multiple interfaces, sensors, tools, or interaction surfaces.

## Extracted principle

Normalize early so the runtime can operate on stable meaning instead of channel-specific chaos.
