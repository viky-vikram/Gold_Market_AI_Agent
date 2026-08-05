# Runbooks

Operational procedures for AurumIQ. Each runbook covers one situation and is written to be followed
under pressure by someone who did not build the system.

## Format

Every runbook states: symptom, impact, how to confirm, immediate mitigation, root-cause
investigation, recovery, and who to escalate to.

## Index

Runbooks are written in the sprint that makes them meaningful — a runbook for a service that does not
exist yet would be fiction. Planned coverage, with the sprint that delivers each:

| Runbook                          | Trigger                                                             | Delivered in |
| -------------------------------- | ------------------------------------------------------------------- | ------------ |
| Provider outage and fallback     | A market-data provider is unavailable or returning stale data       | Sprint 3     |
| OpenAI outage or rate limiting   | Analysis requests fail; deterministic features must stay up         | Sprint 7     |
| Budget circuit breaker opened    | AI generation suspended by cost controls                            | Sprint 9     |
| Analysis queue saturation        | Queue depth exceeds capacity; public endpoints must stay responsive | Sprint 9     |
| Stale or conflicting market data | Data-quality rules flag disagreement between sources                | Sprint 5     |
| Database restore                 | Data loss or corruption                                             | Sprint 14    |
| Model or prompt rollback         | A released model policy regresses quality, latency, or cost         | Sprint 13    |
| Incident response and comms      | Any user-visible degradation                                        | Sprint 14    |

## Related

- Threat models: `docs/threat-models/`
- Architecture decisions: `docs/adr/`
