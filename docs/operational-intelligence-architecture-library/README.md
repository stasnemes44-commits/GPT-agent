# Operational Intelligence Architecture Library

This library is the canonical foundation for building production-grade operational AI systems.

It is not a collection of random skills or prompts.
It is a structured architecture library for:

- operational AI runtimes
- AI agent systems
- deterministic workflow layers
- orchestration and handoff patterns
- memory and context discipline
- observability and recovery standards

## Purpose

The goal is to extract reusable operational intelligence patterns from real systems and research, then convert them into canonical documents that can guide implementation.

This library exists to support systems such as:

- Clinic Operations OS
- AIRYS
- future vertical AI operating systems

## Principles

1. Operational correctness is more important than novelty.
2. Deterministic boundaries must exist around model behavior.
3. Human trust requires auditability, recoverability, and clear escalation.
4. Patterns matter more than one-off prompts.
5. Reliability is a product feature, not an afterthought.

## Library structure

- `canon/` — stable architectural standards and principles
- `patterns/` — reusable design patterns
- `anti_patterns/` — known failure modes and dangerous approaches
- `templates/` — review and extraction templates
- `research/` — working notes and extracted insights

## Recommended usage

Use this library in the following loop:

1. discover patterns from GitHub / SkillsMP / docs / real systems
2. extract the underlying architectural principle
3. record strengths, limits, and failure modes
4. promote validated ideas into canon
5. implement only after boundaries and operational value are clear

## Promotion rule

Nothing becomes canon because it sounds smart.
A pattern should be promoted only when it is:

- useful in real workflows
- understandable
- bounded
- observable
- resilient to failure

## Long-term objective

Build an internal architecture system that makes it possible to design top-tier AI operating systems with stronger reliability, clearer boundaries, and better operational leverage than generic agent stacks.
