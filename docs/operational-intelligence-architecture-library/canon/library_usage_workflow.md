# Library Usage Workflow

This document defines how the Operational Intelligence Architecture Library should be used in practice.

A strong library is not just a place to store documents.
It is a working decision system.

## Core loop

Use the library in the following sequence:

1. detect an architectural need or weakness
2. research candidate patterns and anti-patterns
3. review and score findings
4. extract the underlying principle
5. decide whether to reject, prototype, or promote
6. implement with explicit boundaries
7. observe real behavior
8. feed lessons back into canon or anti-pattern records

## Typical entry points

You should reach for the library when:
- designing a new runtime capability
- evaluating outside architecture ideas
- deciding whether a pattern is worth adopting
- debugging recurring workflow failure
- separating stable doctrine from temporary assumptions
- preparing an implementation plan for Codex or Claude Code

## Working modes

### Mode 1 — Research mode
Use when exploring external ideas.

Primary documents:
- `research/research_backlog.md`
- `templates/pattern_review_template.md`
- `templates/pattern_scoring_framework.md`
- relevant `patterns/*_lens.md`

Output:
- reviewed and scored candidate pattern

### Mode 2 — Doctrine mode
Use when converting promising ideas into stable architecture guidance.

Primary documents:
- `canon/operational_intelligence_doctrine.md`
- `canon/promotion_protocol.md`
- related canon files

Output:
- canon candidate or update to an existing canon rule

### Mode 3 — Implementation mode
Use when preparing a real system change.

Primary questions:
- what canon rules apply
- what pattern is being implemented
- what anti-patterns must be avoided
- what deterministic controls are required
- what observability and recovery are needed

Output:
- implementation-ready architecture direction

### Mode 4 — Incident review mode
Use after failures, surprises, or recurring instability.

Primary questions:
- what failed
- what assumption was wrong
- what anti-pattern appeared
- what canon should change
- what pattern should be strengthened

Output:
- anti-pattern record, canon refinement, or recovery standard

## Recommended workflow before implementation

Before implementing any substantial capability, do this:

1. check relevant canon
2. identify related pattern(s)
3. identify likely anti-pattern(s)
4. define boundaries and source of truth
5. define failure and escalation paths
6. define observability requirements
7. only then write implementation instructions

## Rule for external ideas

Never import an outside idea directly into architecture.
Always pass it through:
- product lens
- boundary analysis
- scoring
- promotion discipline

## Desired behavior

The library should make you slower at naive adoption and faster at high-quality architectural judgment.
That is a feature, not friction.
