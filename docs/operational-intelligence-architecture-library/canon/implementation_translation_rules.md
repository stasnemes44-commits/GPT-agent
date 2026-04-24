# Implementation Translation Rules

This document defines how to translate architecture doctrine into implementation work without losing the core operational principles.

The goal is to prevent a common failure:
strong architecture thinking that degrades into weak implementation instructions.

## Core rule

Implementation instructions should preserve:
- source of truth clarity
- boundary discipline
- deterministic controls
- observability requirements
- recovery and escalation design

If those disappear during translation, the architecture has not actually survived implementation.

## Translation sequence

### 1. Start from operational purpose
Do not start from code structure alone.
First state:
- what workflow problem is being solved
- what outcome must be protected
- what failure must be prevented

### 2. Identify relevant canon
Before drafting implementation, identify:
- applicable doctrine
- applicable patterns
- relevant anti-patterns

### 3. Name the source of truth
Implementation should explicitly state which system or model owns the relevant state.

### 4. Name the control points
Implementation should explicitly state:
- validation gates
- approval gates if needed
- idempotency layer
- reconciliation points
- escalation points

### 5. Separate interpretation from mutation
If a model helps reason about the request, the implementation should still separate:
- interpretation logic
- validation logic
- mutation logic
- logging and recovery logic

### 6. Make observability part of the spec
Implementation guidance should define:
- what to log
- what to measure
- what should be visible to operators
- what identifiers must be traceable

### 7. Translate failure classes, not just happy path
Every important capability should include expected failure classes and the required response for each.

### 8. State what must remain deterministic
This is especially important when handing work to Codex or Claude Code.
Examples:
- policy checks
- permissions
- state transitions
- idempotency behavior
- queue ownership changes

## Anti-pattern during translation

Bad implementation briefs often:
- focus only on files and classes
- ignore source of truth
- describe the happy path only
- leave retries and recovery implicit
- treat observability as optional
- blur the boundary between model behavior and runtime authority

## Desired outcome

A good implementation brief should let an implementation model build faster without accidentally weakening the system.

The translation from doctrine to code should reduce ambiguity, not create it.
