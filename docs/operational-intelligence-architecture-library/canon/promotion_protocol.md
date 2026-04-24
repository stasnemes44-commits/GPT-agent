# Promotion Protocol

This document defines how ideas move from research into canonical architecture guidance.

The purpose is to prevent random accumulation.
Not every interesting pattern deserves a permanent place in the library.

## Promotion stages

### Stage 1 — Discovery
A pattern, method, or architecture idea is found in:
- GitHub repositories
- SkillsMP listings
- articles and technical docs
- internal system experience
- failure postmortems

Output:
- quick note or raw reference

### Stage 2 — Structured review
The idea is reviewed using the Pattern Review Template.

Output:
- explicit strengths
- explicit weaknesses
- failure modes
- extracted principle

### Stage 3 — Scoring
The reviewed pattern is scored using the Pattern Scoring Framework.

Output:
- quantified fit
- strategic value estimate
- implementation realism estimate

### Stage 4 — Decision
The idea is classified as one of:
- reject
- inspiration only
- prototype candidate
- canon candidate

### Stage 5 — Canon promotion
A pattern enters canon only after the principle is rewritten in your own system language and boundaries are explicit.

Canon should capture:
- principle
- where it applies
- where it does not apply
- controls required
- likely failure modes

## Hard rules

Do not promote ideas just because they are:
- new
- popular
- highly upvoted
- clever-sounding
- strongly branded

Promote only if they are:
- operationally useful
- understandable
- bounded
- durable
- compatible with reliable runtime design

## Anti-noise rule

A library that grows without promotion discipline becomes another notes graveyard.
That is failure.

## Canon writing rule

When promoting to canon:
- rewrite in your own doctrine language
- strip away source hype and branding
- state the core principle clearly
- define constraints
- define interaction with deterministic layers

## Practical rule

If a pattern cannot survive translation into a clean operational principle, it probably does not deserve canon status.

## Desired outcome

The library should become sharper over time, not larger for its own sake.
Selective promotion is what turns research into architecture advantage.
