# Claude Code Architecture Brief Template

Use this template when you want Claude Code to think architecturally before or during implementation.

This is best for tasks that require stronger design reasoning, refactoring judgment, or boundary analysis before coding.

## 1. Architectural objective
What system capability, refactor, or design decision is being worked on?

## 2. Product and context
- Product:
- Current stage:
- Why this matters now:

## 3. Problem framing
What operational weakness, risk, or opportunity exists?

## 4. Desired architecture outcome
Describe the target shape, not just the code change.

## 5. Relevant canon
List the doctrine Claude Code must use as reference.

## 6. Relevant patterns
List patterns Claude Code should apply or consider.

## 7. Relevant anti-patterns
List architecture traps Claude Code must watch for.

## 8. Source-of-truth model
What system or layer owns the relevant truth?

## 9. Boundary requirements
What layer boundaries must remain clear?
Examples:
- model vs runtime authority
- interface vs policy vs execution
- canon vs temporary context

## 10. Operational constraints
List non-negotiable realities.
Examples:
- deterministic booking protection
- omnichannel normalization
- handoff visibility
- private memory direction

## 11. Failure and recovery expectations
What failure classes matter here?
What should happen when ambiguity appears?

## 12. Observability expectations
What must be visible or auditable after this change?

## 13. Deliverable requested from Claude Code
Ask for:
- architecture analysis
- recommended target design
- risks and trade-offs
- file-level implementation plan
- doctrine conflicts or warnings
- optional phased rollout path

## 14. Final instruction
Tell Claude Code to optimize for operational correctness, boundary clarity, and long-term maintainability rather than cleverness alone.
