# Model Task Routing Standard

This document defines how to route work between implementation models such as Codex and Claude Code.

The goal is not brand preference.
The goal is to assign the right kind of work to the right model shape.

## Core rule

Route by task nature, not by habit.

A weaker routing choice can waste time, reduce architectural quality, or produce fragile implementation.

## Recommended routing logic

### Use Claude Code first when the task is primarily about:
- architecture analysis
- repo-wide refactor planning
- boundary redesign
- system decomposition
- doctrine alignment
- deep trade-off reasoning
- evaluating multiple possible implementation shapes

Why:
Claude Code is often stronger when the task requires extended architectural thinking before coding.

### Use Codex first when the task is primarily about:
- concrete implementation against a clear target
- file-level changes
- deterministic coding tasks
- well-scoped feature delivery
- testable code generation from a defined brief
- execution after the architecture is already shaped

Why:
Codex is often strong when the target shape is already clear and the task is to produce precise implementation work.

## Recommended two-step flow

For important capabilities, prefer:

1. Claude Code for architecture framing
2. Codex for implementation execution
3. Claude Code again for architectural review when needed

This is often stronger than asking one model to do everything.

## Tasks that should not start with raw code generation

Do not begin with implementation-first when the task involves:
- unclear source of truth
- ambiguous state model
- cross-layer architecture changes
- new handoff or recovery design
- major memory or runtime boundary changes

These tasks need architecture reasoning before code.

## Tasks well suited for direct implementation

Direct implementation is reasonable when:
- source of truth is already defined
- runtime stages are known
- anti-patterns are understood
- acceptance criteria are concrete
- file scope is clear

## Required input quality

Regardless of model, provide:
- operational purpose
- relevant canon
- relevant patterns
- relevant anti-patterns
- source of truth
- deterministic requirements
- observability requirements
- acceptance criteria

## Rule against vague prompting

If the task is important, never just ask a model to “implement the feature” without architecture framing.
That is how strong doctrine gets lost in translation.

## Desired outcome

Model routing should make the system stronger.
Not merely faster.
Good routing preserves architecture quality while still using each model where it is most effective.
