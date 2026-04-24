# Anti-Pattern: Channel-Specific Chaos

## Summary

This anti-pattern appears when each communication channel evolves into its own mini-system with separate business logic, identity logic, and workflow behavior.

Instead of having one operational core with normalized input and output adaptation, the architecture fragments into channel-bound silos.

## Why it happens

It often appears when teams add channels one by one and optimize locally:
- Telegram logic here
- Instagram logic there
- WhatsApp special cases elsewhere
- site chat with different state handling

This feels practical early.
It becomes expensive and unstable later.

## Why it is dangerous

Channel-specific chaos leads to:
- duplicated logic
- inconsistent behavior across channels
- identity mismatches
- reporting fragmentation
- harder support and debugging
- slower future expansion

## Typical symptoms

Signs this anti-pattern is present:
- the same business rule is implemented differently in each channel flow
- identity linking differs per channel with no shared authority
- message status and workflow state semantics change by channel
- new channels require major logic duplication
- operators see different realities depending on where the conversation began

## Operational failure modes

Common outcomes include:
- duplicate or conflicting conversations
- broken cross-channel continuity
- inconsistent reminders or confirmations
- different booking behavior across channels
- hidden bugs that exist only in one interface path

## Better alternative

Build a normalized operational core.

Recommended structure:
- channel adapters at the edge
- event normalization envelope
- shared identity and session model
- shared business logic
- channel-specific rendering only at output boundaries

## Product risk

### Clinic Operations OS
Extremely dangerous.
Omnichannel reliability depends on early normalization and shared operational semantics.

### AIRYS
Dangerous when multiple interfaces, devices, or surfaces need to feel like one coherent system.

## Rule

Channels should express the system.
They should not become separate versions of the system.

## Safer principle

Normalize meaning at the boundary, then run one operational logic core behind all channels.
