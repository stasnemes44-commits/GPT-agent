# Clinic Operations OS Operator Console Blueprint

This blueprint describes the target operational console for human admins and operators inside Clinic Operations OS.

The operator console is not just a dashboard.
It is the human collaboration surface of the runtime.

## Core objective

Give operators a clear, fast, actionable view of:
- what needs human attention
- what the runtime already did
- what is blocked
- what requires approval
- what failed or drifted

## Core surfaces

### 1. Priority queue
Shows the highest-value items needing action now.

Examples:
- escalation-required conversations
- booking conflicts
- failed confirmations
- unresolved ambiguous states
- approval-required actions

### 2. Active conversations/work items
Shows live or recently active operational threads with:
- channel
- patient/entity context
- current workflow state
- owner
- urgency

### 3. Scheduling risk surface
Shows operational scheduling issues.

Examples:
- potential double-booking
- missing confirmation
- slot risk
- last-minute change requests
- unresolved booking ambiguity

### 4. Recovery and exception lane
Shows:
- failed workflow actions
- dead-letter items
- reconciliation anomalies
- repeated retry incidents

### 5. Approval surface
Shows actions awaiting operator confirmation or rejection.

### 6. Audit/detail drawer
For a selected work item, show:
- normalized event history
- workflow steps taken
- tool results
- reason codes
- ownership transitions
- current recommended next action

## Required qualities

The console should let an operator understand a case quickly.
Within roughly one minute, the operator should know:
- what happened
- what the runtime did
- why the case is here
- what action is expected
- what the current owner/state is

## Critical design principles

### Ownership clarity
Every case should show who owns it now.

### Reason-code visibility
Escalated or failed items should never appear without a clear reason.

### Actionability over clutter
The console should emphasize what to do next, not just what exists.

### Traceability
Operators should be able to inspect why the system behaved the way it did.

### Calmness under load
The interface should reduce chaos, not multiply it.

## Product value

A strong operator console is one of the key ways Clinic Operations OS becomes commercially real.
It proves the system is not trying to replace human operations blindly.
It is strengthening them.
