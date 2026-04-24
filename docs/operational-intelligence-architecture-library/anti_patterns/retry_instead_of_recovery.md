# Anti-Pattern: Retry Instead of Recovery

## Summary

This anti-pattern appears when a system responds to many failures mainly by retrying, instead of distinguishing failure classes and applying proper recovery design.

Retry is useful.
But when it becomes the default answer to everything, the system becomes noisy, repetitive, and fragile.

## Why it happens

It often happens because retry feels easy to add:
- wrap the step
- add backoff
- try again

This can help for transient errors.
It fails badly when the underlying problem is ambiguity, policy failure, malformed input, or state drift.

## Why it is dangerous

Overusing retry leads to:
- duplicate mutations
- retry storms
- delayed escalation
- hidden incidents
- repeated user-visible mistakes
- increased operational noise

## Typical symptoms

Signs this anti-pattern is present:
- many failure classes all funnel into the same retry logic
- the system keeps re-attempting actions with unclear outcomes
- policy or validation failures trigger retries instead of blocking
- operators learn about incidents only after repeated damage
- dead-letter lanes are weak or absent

## Operational failure modes

Common outcomes include:
- duplicate reminders or messages
- repeated booking attempts against an unclear state
- queues filling with noisy repeats
- delayed human intervention
- drift getting worse before someone inspects it

## Better alternative

Separate:
- transient technical failure
- persistent execution failure
- ambiguous state failure
- policy or validation failure

Then apply the right response:
- bounded retry
- reconciliation
- escalation
- explicit stop
- engineering fix path

## Product risk

### Clinic Operations OS
Very dangerous.
This can directly damage trust around reminders, confirmations, and schedule integrity.

### AIRYS
Dangerous for proactive workflows, memory sync, and ambient actions that should stop when uncertain.

## Rule

Retry is a tactic, not a recovery strategy.
A mature system decides first what kind of failure occurred.

## Safer principle

Recover by classification and control, not by reflexive repetition.
