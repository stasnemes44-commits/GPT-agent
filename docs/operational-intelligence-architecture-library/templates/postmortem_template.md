# Postmortem Template

Use this template after an incident, failure, near-miss, or recurring instability.

The goal is not blame.
The goal is to strengthen the architecture system.

## 1. Incident summary
- Incident title:
- Date/time:
- Product:
- Severity:
- Status:

## 2. What happened
Describe the incident in concrete operational terms.

## 3. User and business impact
What was affected?
Examples:
- duplicate booking
- missed reminder
- wrong escalation
- stale memory behavior
- operator confusion
- silent workflow failure

## 4. Detection
How was the issue detected?
- user report
- operator observation
- logs/metrics
- reconciliation job
- engineering review

## 5. Timeline
List the main events in order.

## 6. Source of truth
What system or rule should have had authority here?
Was authority clear or ambiguous?

## 7. Failure classification
Choose one or more:
- transient technical failure
- ambiguous state failure
- policy failure
- validation failure
- hidden state logic
- ownership failure
- channel normalization failure
- memory hierarchy failure
- recovery design failure
- observability failure

## 8. Root causes
What underlying architectural causes made this incident possible?
Avoid superficial answers.

## 9. Contributing factors
What made the incident worse or harder to detect?

## 10. Canon or pattern gaps
What doctrine was missing, weak, ignored, or bypassed?

## 11. Anti-pattern signals
Which anti-pattern(s) appeared?

## 12. Fixes
### Immediate fix
What was done to stop the issue now?

### Structural fix
What should change so this class of problem becomes less likely?

## 13. Observability improvements
What should be logged, surfaced, measured, or alerted next time?

## 14. Recovery improvements
What recovery or reconciliation mechanism should exist?

## 15. Promotion outcome
Should this incident produce:
- anti-pattern update
- canon update
- new pattern doc
- implementation standard change
- no library change

## 16. Final lesson
State the architectural lesson in one or two sharp sentences.
