# Clinic Operations OS Pattern Lens

This document defines how to judge patterns specifically for Clinic Operations OS.

A pattern may be good in general and still be weak for a clinic operating system.
The evaluation lens must reflect the realities of scheduling, communication, ownership, human workflows, and trust.

## Core priorities for Clinic Operations OS

Patterns are more valuable when they strengthen:
- scheduling correctness
- anti-double-booking protections
- omnichannel normalization
- operator handoff quality
- patient communication reliability
- auditability
- queue visibility
- deterministic business rule enforcement

## High-value pattern areas

### 1. Scheduling authority patterns
Questions:
- what system owns booking truth
- how conflicts are prevented
- how tentative vs confirmed states are handled
- how cancellations are validated

### 2. Handoff and operator console patterns
Questions:
- can a human take over cleanly
- is ownership explicit
- does the operator understand the context fast
- can work return to runtime safely

### 3. Omnichannel normalization patterns
Questions:
- do Telegram, WhatsApp, Instagram, site chat, and future channels normalize early
- is actor/session identity carried clearly
- are channel quirks isolated from core logic

### 4. Reminder and follow-up patterns
Questions:
- can reminders be traced
- can failures be reconciled
- does the workflow support confirmation states and no-show mitigation

### 5. Safety and trust patterns
Questions:
- is state mutation bounded
- are ownership checks explicit
- is ambiguous state blocked or escalated
- is the workflow inspectable later

## Clinic-specific rejection criteria

A pattern is a poor fit if it:
- assumes free-form autonomy without scheduling safeguards
- hides state changes behind vague natural language flows
- lacks idempotency around messages or bookings
- makes human takeover messy
- treats channels as separate mini-products
- has no clear recovery path after partial failure

## Design principle

Clinic Operations OS should feel calm under pressure.
That means patterns must reduce chaos, not merely appear intelligent.

## Promotion bias

Prefer patterns that make the system:
- harder to break
- easier to inspect
- safer to hand over
- easier to support in production

This is more important than clever orchestration for its own sake.
