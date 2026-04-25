# Incident Learning Protocol

This document defines how incidents should strengthen the architecture system.

Incidents should not end as one-off fixes.
They should produce learning that improves doctrine, patterns, implementation standards, or observability.

## Core rule

Every meaningful incident should be translated into architectural learning.

That learning may become:
- anti-pattern refinement
- canon update
- new pattern guidance
- implementation rule
- observability requirement
- recovery requirement

## Incident learning loop

### 1. Capture the incident
Use the postmortem template.
Do not rely on vague recollection.

### 2. Classify the failure
Identify what class of architectural failure occurred.
Examples:
- hidden state
- weak source of truth
- insufficient validation
- handoff failure
- retry misuse
- channel normalization failure
- memory hierarchy failure

### 3. Identify doctrine gap
Ask:
- was doctrine missing
- was doctrine present but ignored
- was doctrine too vague
- did implementation violate translation rules

### 4. Decide the library output
Choose one or more:
- update anti-pattern doc
- add new anti-pattern doc
- strengthen canon
- add or refine a pattern
- create implementation brief rule
- add observability/recovery standard

### 5. Record the lesson sharply
The final learning should be expressible in a small number of clear sentences.
If the lesson remains vague, the learning is not yet useful.

## What not to do

Do not:
- stop at patching the symptom
- treat incidents as isolated human error when architecture enabled them
- bury failures without producing library updates
- produce long postmortems with no operational takeaway

## Promotion threshold

Not every small issue needs a new document.
But recurring or high-impact incidents should change the library.
Otherwise the architecture system is not compounding.

## Desired outcome

Over time, the library should become stronger because reality keeps teaching it.
That is how architectural judgment becomes durable.
