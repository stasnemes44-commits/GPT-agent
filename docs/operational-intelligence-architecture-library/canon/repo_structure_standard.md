# Repo Structure Standard

This document defines the intended structure and usage model of the Operational Intelligence Architecture Library.

The structure should support signal, not sprawl.

## Top-level structure

Recommended structure:

- `canon/`
- `patterns/`
- `anti_patterns/`
- `templates/`
- `research/`

## Purpose of each area

### `canon/`
Contains stable architecture doctrine.
This is where the strongest and most reusable principles live.

Use for:
- operational doctrine
- runtime principles
- boundary rules
- promotion protocol
- memory model
- handoff standard
- recovery standard

### `patterns/`
Contains reusable design patterns and product lenses.

Use for:
- deep pattern docs
- system-specific evaluation lenses
- standard runtime approaches

### `anti_patterns/`
Contains dangerous design tendencies and failure patterns.

Use for:
- common traps
- failure modes
- architecture smells
- lessons from incidents

### `templates/`
Contains working templates for evaluation and extraction.

Use for:
- pattern reviews
- scoring frameworks
- postmortem structures
- implementation brief templates

### `research/`
Contains backlog and working research outputs.
This area is allowed to be less polished than canon.

Use for:
- backlog lists
- raw extracted findings
- candidate ideas awaiting review

## Movement rules

### What belongs in `canon/`
Only material that is:
- reusable
- stable enough to guide future design
- written in your doctrine language
- bounded and operationally meaningful

### What belongs in `research/`
Material that is:
- promising but not yet validated
- source-driven
- still being evaluated
- temporary or exploratory

### What belongs in `anti_patterns/`
Material that is:
- repeatedly dangerous
- likely to recur
- useful as a warning or diagnostic signal

## Structural discipline

Avoid these mistakes:
- putting raw notes directly into canon
- mixing product-specific temporary context with stable doctrine
- duplicating the same principle across many files
- turning `research/` into an unfiltered dumping ground

## Growth rule

The library should grow by sharpening categories, not by multiplying vague documents.
Whenever possible:
- consolidate duplicate ideas
- raise strong ideas into canon
- archive or ignore weak ideas

## Design outcome

A good structure should make it obvious:
- where stable truth lives
- where experiments belong
- where warnings are recorded
- how ideas mature over time

That clarity is part of the architecture system itself.
