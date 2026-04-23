# Pattern Catalog

This catalog is the starting index of high-value patterns for operational AI systems.

Each pattern should later receive its own dedicated document.

## 1. Planner-Executor with validation gate
Use when interpretation and execution should be separated.

Why it matters:
- keeps language reasoning separate from action authority
- allows deterministic checks before mutation
- reduces unsafe autonomy

## 2. Human escalation queue
Use when a workflow must pause safely and transfer ownership to a human operator.

Why it matters:
- preserves trust in ambiguous cases
- prevents bad autonomous actions
- gives the runtime a designed fallback path

## 3. Idempotent mutation wrapper
Use around all state-changing actions.

Why it matters:
- prevents duplicate bookings, duplicate sends, duplicate updates
- protects against retries and repeated inbound events

## 4. Event normalization envelope
Use at system entry points.

Why it matters:
- gives all channels a common schema
- reduces branching chaos deeper in the runtime
- improves observability and replay

## 5. Ownership validation gate
Use before any mutation that depends on actor ownership or access scope.

Why it matters:
- prevents cross-user state corruption
- makes access rules explicit
- strengthens handoff integrity

## 6. State reconciliation job
Use for systems with external dependencies or partial failures.

Why it matters:
- detects drift between intended and actual state
- repairs inconsistencies after tool or network failure
- improves production resilience

## 7. Memory authority hierarchy
Use in systems with multiple memory layers.

Why it matters:
- distinguishes stable canon from temporary context
- reduces context poisoning and accidental overwrite
- improves consistency over time

## 8. Approval-gated execution
Use when an action is high-risk, user-visible, or commercially meaningful.

Why it matters:
- creates a clean pause point before mutation
- supports operator review or user confirmation
- reduces irreversible mistakes

## 9. Dead-letter and retry lane
Use when actions can fail asynchronously or partially.

Why it matters:
- prevents silent loss of work
- supports controlled retries
- creates inspection points for recovery

## 10. Audit-first workflow design
Use for any serious operational workflow.

Why it matters:
- ensures actions are inspectable later
- supports debugging and trust
- makes production operations manageable

## Promotion standard

A pattern should become part of stable canon only after:
- real-world relevance is clear
- boundaries are explicit
- failure modes are documented
- implementation cost is acceptable
- operational benefit is strong
