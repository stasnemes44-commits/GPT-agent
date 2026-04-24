# Research Backlog

This backlog defines the highest-value research tracks for the Operational Intelligence Architecture Library.

The goal is not to collect interesting things.
The goal is to extract patterns that improve real operational systems.

## Priority 1 — Runtime control

Research targets:
- planner-executor separation
- execution coordinators
- runtime dispatchers
- approval-gated execution
- deterministic control layers

Why this matters:
This is the core of any serious operational AI runtime.

## Priority 2 — Reliability and recovery

Research targets:
- idempotent mutation strategies
- dead-letter lanes
- reconciliation jobs
- retry backoff strategies
- incident visibility patterns

Why this matters:
Systems fail in production. The difference is whether they fail visibly and recoverably.

## Priority 3 — State and event discipline

Research targets:
- event normalization envelopes
- state transition validation
- source-of-truth models
- distributed workflow consistency
- channel normalization

Why this matters:
Without state discipline, the runtime becomes fragile and contradictory.

## Priority 4 — Handoff and HITL

Research targets:
- operator escalation queues
- manual override models
- human acceptance lifecycle
- return-to-runtime design
- queue prioritization

Why this matters:
Human collaboration is a core feature of real operational systems.

## Priority 5 — Memory systems

Research targets:
- memory hierarchy models
- canon vs. working context separation
- episodic vs. stable memory
- memory compression and summarization
- stale-context prevention

Why this matters:
Long-lived systems become incoherent without memory authority discipline.

## Priority 6 — Observability

Research targets:
- execution tracing
- audit-first workflow design
- runtime telemetry for agent systems
- operator inspection views
- decision provenance

Why this matters:
You cannot manage what you cannot inspect.

## Priority 7 — Tooling discipline

Research targets:
- safe tool invocation standards
- schema-driven tool design
- permissioned tools
- postcondition verification
- tool risk classification

Why this matters:
Tools are where systems stop being theoretical and start changing reality.

## Priority 8 — Product-specific lenses

### Clinic Operations OS lens
Research targets:
- scheduling authority models
- anti-double-booking patterns
- operator console patterns
- patient communication workflows
- omnichannel runtime normalization

### AIRYS lens
Research targets:
- privacy-first context systems
- emotional stabilization patterns
- ambient assistance patterns
- long-horizon memory discipline
- user-trust architecture

## Research selection rule

Prioritize sources that provide:
- real implementation logic
- boundary discipline
- failure handling
- observable workflow structure
- reusable operational principles

Avoid over-investing in sources that mainly provide:
- flashy prompts
- unbounded autonomy claims
- demo-oriented cleverness
- generic assistant framing

## Output standard

Every research session should ideally produce one of three outputs:
- anti-pattern recorded
- candidate pattern extracted
- canon-worthy principle proposed
