# Implementation Brief Template

Use this template when translating library doctrine and patterns into an implementation plan for a real system.

## Capability name

## Product context
- Clinic Operations OS / AIRYS / other
- Why this capability matters now

## Problem statement
What operational problem is being solved?

## Desired outcome
What should be true after this capability exists?

## Applicable canon
List relevant canon documents.

## Applicable patterns
List relevant patterns.

## Relevant anti-patterns to avoid
List anti-patterns most likely to appear.

## State authority
What system or rule owns the relevant truth?

## Event entry points
What events trigger this capability?

## Validation and policy gates
What must be checked before action?

## Execution design
What tools or runtime components actually perform the work?

## Idempotency strategy
How will duplicate intent be prevented from creating duplicate reality?

## Handoff and escalation path
When must automation stop or transfer to a human?

## Recovery and reconciliation design
What happens if execution fails, partially succeeds, or becomes ambiguous?

## Observability requirements
What must be logged, traced, measured, or surfaced to operators?

## Edge cases
List the highest-risk edge cases.

## Acceptance criteria
What concrete conditions define success?

## Notes for implementation model
If using Codex or Claude Code, specify:
- files likely affected
- boundaries not to violate
- expected architectural shape
- what must remain deterministic
