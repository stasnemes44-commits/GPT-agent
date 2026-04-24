# Runtime Capability Design Template

Use this template to design a capability before implementation.

## 1. Capability identity
- Name:
- Product:
- Owner domain:
- Priority:

## 2. Operational purpose
What real workflow does this capability serve?

## 3. Trigger model
What starts this capability?
- inbound event
- scheduled job
- operator action
- user action
- system reconciliation

## 4. Inputs
What structured inputs are required?
What optional inputs are allowed?

## 5. Outputs
What result states or side effects can occur?

## 6. Source of truth
What system or data model has authority over the relevant state?

## 7. Runtime stages
Describe the stages explicitly.
Typical examples:
- normalize
- interpret
- validate
- approve
- execute
- verify
- log
- reconcile
- escalate

## 8. Validation requirements
What conditions must be true before execution?

## 9. Policy and permissions
What rules or access constraints apply?

## 10. Idempotency and duplication control
How is duplicate intent prevented?

## 11. Failure classes
List expected failure classes.
Examples:
- transient technical failure
- ambiguous state
- policy failure
- malformed input
- external system conflict

## 12. Recovery model
How should each failure class be handled?

## 13. Handoff model
When and how does this capability transfer work to a human?

## 14. Observability model
What logs, metrics, traces, and queue visibility are required?

## 15. Anti-pattern watchlist
Which anti-patterns are most likely to appear here?

## 16. Acceptance criteria
What concrete behaviors prove the capability is working correctly?

## 17. Implementation notes
What boundaries should the implementation respect?
What should remain deterministic?
What code areas are likely involved?
