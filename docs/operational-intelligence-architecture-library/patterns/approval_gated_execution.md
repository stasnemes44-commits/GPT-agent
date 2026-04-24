# Approval-Gated Execution

## Pattern summary

This pattern inserts an explicit approval checkpoint before certain actions are allowed to execute.

It is a key control for actions that are high-risk, hard to reverse, commercially meaningful, or trust-sensitive.

## Problem solved

Not every valid action should execute immediately.
Some actions need:
- user confirmation
- operator approval
- policy review
- second-layer validation

Without approval gates, systems may act too aggressively and create costly mistakes.

## Pattern structure

### 1. Detect approval-required action
A workflow classifies the action as requiring approval.

Triggers may include:
- destructive mutation
- financially meaningful change
- broad outbound communication
- ambiguous or incomplete inputs
- policy-defined high-risk state

### 2. Create approval item
The system records:
- action proposal
- context summary
- affected entities
- reason for approval requirement
- requester identity or source
- expiration or timeout if relevant

### 3. Pause execution safely
The runtime must not continue with the protected mutation until approval is resolved.

### 4. Resolve approval
Possible outcomes:
- approved
- rejected
- expired
- superseded
- escalated further

### 5. Resume or terminate
If approved, the runtime executes through standard validation and logging.
If rejected or expired, the mutation does not proceed.

## Why it matters

Approval gates:
- reduce costly mistakes
- increase operator trust
- create accountability around sensitive actions
- preserve system boundaries in ambiguous situations

## When to use it

Use it when:
- the action has meaningful business impact
- the action is hard to reverse
- policy requires human review
- user consent must be explicit
- confidence is not enough on its own

## Controls required

Recommended controls:
- explicit approval status model
- actor and approver identity tracking
- expiration handling
- revalidation before execution after approval
- structured approval log

## Failure modes to watch

- approval items with vague proposed action
- runtime proceeding before approval is final
- approvals not expiring when context changes
- approved action executing without fresh validation

## Product relevance

### Clinic Operations OS
Very high relevance.
Useful for sensitive schedule changes, unusual cancellations, operator-reviewed outbound actions, and business-critical mutations.

### AIRYS
High relevance for proactive actions affecting memory, external systems, or user-visible commitments.

## Extracted principle

Some actions should be intelligent enough to propose, but disciplined enough to wait for explicit approval before becoming real.
