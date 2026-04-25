# AIRYS Memory Runtime Blueprint

This blueprint describes the target memory runtime shape for AIRYS.

AIRYS should not rely on undifferentiated memory accumulation.
Its memory runtime should preserve continuity, trust, and user agency through disciplined hierarchy and control.

## Core objective

Create a memory runtime that is:
- useful over long time horizons
- coherent across changing contexts
- private in direction
- inspectable enough to earn trust
- bounded enough to avoid stale or manipulative behavior

## Memory layers

### 1. Identity and doctrine layer
Stores the highest-authority truths.

Examples:
- AIRYS product identity
- safety boundaries
- core user-aligned principles
- enduring personal constraints only when explicitly intended

### 2. Domain canon layer
Stores stable patterns and user-relevant long-lived rules.

Examples:
- strong personal preferences
- stable life structures
- recurring routines
- enduring goals when confirmed

### 3. Active operating context layer
Stores context relevant to current projects and recent life phase.

Examples:
- current focus areas
- temporary constraints
- ongoing plans
- recent emotional or workload patterns

### 4. Session/context layer
Stores immediate conversational and situational context.
This layer should expire or compress aggressively.

### 5. Evidence/log layer
Stores observed events, summaries, and interaction traces that can support future promotion or review.

## Core runtime functions

### Memory intake
Responsibilities:
- classify incoming information by authority tier
- avoid over-promoting recent or noisy data
- preserve provenance where important

### Promotion logic
Responsibilities:
- promote only what survives repeated relevance or explicit confirmation
- protect canon from session noise
- require stronger thresholds for emotionally or identity-significant memory

### Expiry and revalidation
Responsibilities:
- let working context decay
- revalidate assumptions before treating them as durable
- reduce stale context accumulation

### Retrieval shaping
Responsibilities:
- retrieve by relevance and authority, not just recency
- separate stable truth from active context
- expose uncertainty when memory confidence is low

### User control surface
Responsibilities:
- support inspection of meaningful memory layers
- allow deletion or revision where appropriate
- keep memory behavior legible enough for trust

## Non-negotiable controls

- authority hierarchy
- promotion discipline
- expiry or revalidation for temporary context
- provenance-aware retrieval where important
- user agency around meaningful memory

## Failure modes to guard against

- session noise becoming canon
- stale assumptions driving proactive behavior
- emotionally sensitive over-retention
- manipulative memory accumulation
- retrieval that ignores authority level

## Design principle

AIRYS memory should feel like disciplined continuity, not uncontrolled accumulation.
That is what turns memory into trust instead of risk.
