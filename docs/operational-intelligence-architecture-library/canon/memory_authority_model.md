# Memory Authority Model

This document defines how memory should be structured in an operational AI system.

The goal is not to remember everything.
The goal is to preserve the right truth at the right level of authority.

## Core rule

Not all memory is equal.

Operational systems need explicit memory hierarchy, otherwise they accumulate noise, stale assumptions, and unsafe context carryover.

## Authority tiers

### Tier 1 — Identity and doctrine
This is the highest authority memory.
It changes rarely and should be treated as canonical.

Examples:
- system purpose
- product doctrine
- safety boundaries
- core operating principles
- permanent identity constraints

Properties:
- highly stable
- explicitly versioned
- edited intentionally
- never overwritten by session chatter

### Tier 2 — Domain canon
This contains stable domain truth that guides behavior.

Examples:
- scheduling rules
- ownership policy
- escalation rules
- data contracts
- workflow rules
- approved prompt standards

Properties:
- durable
- reviewed before updates
- stronger authority than temporary context

### Tier 3 — Active operating context
This contains context needed for current work.

Examples:
- current project phase
- active repo focus
- current migration effort
- pending rollout risks
- temporary working assumptions

Properties:
- important but revisable
- should expire or be promoted
- must be separated from canon

### Tier 4 — Session memory
This contains short-horizon local context.

Examples:
- what the user is doing right now
- current conversation goals
- immediate tasks
- working notes

Properties:
- disposable
- low authority
- should not silently become truth

### Tier 5 — Evidence and logs
This includes records of events, outputs, experiments, and traces.

Examples:
- workflow logs
- execution history
- search findings
- experiment results
- audit traces

Properties:
- useful for verification
- not automatically policy truth
- can support promotion into canon

## Promotion rules

Context should move upward only with intention.

### Promote upward only when:
- it is repeatedly useful
- it survived real usage
- it has clear boundaries
- it is not contradicted by stronger authority
- it should guide future system behavior

### Do not promote when:
- it is merely recent
- it came from one noisy session
- it is still ambiguous
- it belongs only to one narrow local task

## Conflict resolution order

When memory layers disagree, prefer this order:

1. identity and doctrine
2. domain canon
3. active operating context
4. session memory
5. evidence/logs without explicit promotion

## Memory smell list

The memory model is weak if:
- temporary notes keep overriding stable rules
- logs are treated as canon without review
- old assumptions remain active indefinitely
- there is no expiry model for working context
- user preferences and system doctrine are mixed together

## Operational guidance

A strong memory system should answer:
- what is permanently true
- what is currently active
- what is merely observed
- what is provisional
- what can be safely forgotten

## Design outcome

The system should remember with discipline.
Not maximal accumulation.
Not vibe-based recall.
Disciplined memory authority is what keeps long-lived AI systems coherent over time.
