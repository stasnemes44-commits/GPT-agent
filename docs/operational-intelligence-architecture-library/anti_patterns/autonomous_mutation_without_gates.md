# Anti-Pattern: Autonomous Mutation Without Gates

## Summary

This anti-pattern appears when a model or loosely controlled workflow can change state directly without strong validation, approval, permission checks, or idempotency controls.

The system may seem fast and impressive at first.
In production, it becomes a liability.

## Why it happens

It often happens because teams want:
- less friction
- a more “agentic” feel
- fewer explicit control layers
- faster shipping

But removing gates does not create maturity.
It removes safety.

## Why it is dangerous

Without gates, systems can:
- create duplicate mutations
- act on incomplete or ambiguous inputs
- violate business policy
- damage user trust
- become hard to audit after failure

## Typical symptoms

Signs this anti-pattern is present:
- the model can call state-changing tools directly
- approval is assumed rather than explicit
- missing data does not reliably block mutation
- ownership is inferred loosely
- retries can re-trigger real-world actions with little control

## Operational failure modes

Common outcomes include:
- duplicate bookings
- wrong outbound messages
- bad cancellations
- conflicting state across systems
- silent policy violations
- support burden after irreversible actions

## Better alternative

Use a controlled execution stack:
- interpretation layer
- validation gate
- permission check
- idempotent executor
- structured logging
- reconciliation or escalation when needed

## Product risk

### Clinic Operations OS
Extremely dangerous.
This can directly break scheduling trust and operator confidence.

### AIRYS
Dangerous for proactive actions, memory changes, and any user-visible commitment.

## Rule

If an action changes real state, it should pass through a deliberate control path.
Autonomy without gates is not intelligence.
It is unmanaged risk.

## Safer principle

The more real-world impact an action has, the more explicit the control path around that action must be.
