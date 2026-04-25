# Codex Execution Brief Template

Use this template when preparing a concrete implementation task for Codex.

The goal is to keep implementation productive without losing architecture discipline.

## 1. Task identity
- Capability name:
- Repo area:
- Priority:

## 2. Operational purpose
What real workflow problem are we solving?

## 3. Outcome required
What should be true after implementation?
Be concrete.

## 4. Relevant canon
List the canon documents Codex must respect.

## 5. Relevant patterns
List the patterns this implementation should follow.

## 6. Relevant anti-patterns
List the anti-patterns Codex must avoid.

## 7. Source of truth
What system/model has authority over the relevant state?

## 8. Required runtime stages
List the required stages.
Example:
- normalize
- interpret
- validate
- execute
- verify
- log
- reconcile or escalate

## 9. Deterministic requirements
What must remain deterministic?
Examples:
- validation
- permissions
- state transitions
- idempotency
- ownership updates

## 10. Observability requirements
What logs, metrics, identifiers, or audit outputs must exist?

## 11. Failure handling requirements
What failure classes must be handled explicitly?
What should happen in each class?

## 12. Handoff and recovery requirements
When should work escalate or reconcile instead of continuing automatically?

## 13. Files likely involved
List likely files or layers to change.

## 14. Files or boundaries not to violate
List constraints clearly.

## 15. Acceptance criteria
State concrete tests or behaviors that must pass.

## 16. Output expectation for Codex
Ask Codex to return:
- architecture summary
- file-by-file plan
- exact implementation changes
- edge-case handling notes
- any doctrine conflicts noticed
