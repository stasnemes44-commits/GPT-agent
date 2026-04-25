# Anti-Pattern: No Clear Source of Truth

## Summary

This anti-pattern appears when multiple systems, workflows, or memory layers appear to own the same state without a clearly defined authority model.

The result is not healthy redundancy.
It is operational confusion.

## Why it happens

It often happens because:
- systems are integrated incrementally
- local caches become quasi-authoritative
- prompts or session context start acting like state owners
- teams optimize for convenience instead of authority clarity

## Why it is dangerous

Without a clear source of truth, systems produce:
- contradictory outputs
- weak reconciliation
- inconsistent operator decisions
- duplication of actions
- fragile recovery after failure

## Typical symptoms

Signs this anti-pattern is present:
- different tools report different versions of the same status
- nobody can answer which system should win in a conflict
- local state gets treated as final without verification
- operators and runtime disagree on what is current
- reconciliation jobs have no reliable authority target

## Operational failure modes

Common outcomes include:
- double-booking or false availability
- reminder workflows running from stale state
- operator screens showing a different truth than backend records
- memory-driven behavior conflicting with canon or persistent data

## Better alternative

Define authority explicitly.

Recommended controls:
- source-of-truth statement per domain
- conflict resolution rules
- reconciliation jobs against authority
- clear separation between cache, working context, and canonical state
- operator-visible status provenance where needed

## Product risk

### Clinic Operations OS
Extremely dangerous.
Scheduling and operational trust collapse quickly when authority is vague.

### AIRYS
Very high risk.
Memory, context, and user trust degrade when the system cannot distinguish canonical truth from temporary context.

## Rule

If two or more parts of the system appear to own the same truth, authority has not been designed strongly enough.

## Safer principle

Every important domain needs an explicit authority model so conflicts can be resolved instead of improvised.
