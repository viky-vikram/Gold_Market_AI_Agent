# Requirement-to-test traceability

Every acceptance criterion in the seven controlled documents gets a stable requirement ID and a test
ID. Requirement IDs are permanent: once assigned, never renumber or reuse one, because commit
messages, PRs, and test names reference them.

`Test ID` is `TBD` where the delivering sprint has not run yet. That is expected during Sprint 0 and
is not a gap — it becomes one if a requirement is still `TBD` when its sprint closes.

**Status:** `TBD` not yet implemented · `PARTIAL` some criteria covered · `DONE` fully covered by
passing tests.

## Source of IDs

| Prefix     | Controlled document          | Section                              |
| ---------- | ---------------------------- | ------------------------------------ |
| `REQ-PRD`  | PRD                          | 17 Acceptance Criteria Highlights    |
| `REQ-FLOW` | Application Flow             | 15 Acceptance Scenarios              |
| `REQ-DB`   | Backend Database Schema      | 19 Database Acceptance Criteria      |
| `REQ-API`  | API/Event/Provider Contracts | 15 Contract Acceptance Criteria      |
| `REQ-UX`   | UI/UX Recommendations        | 13 UX Acceptance Criteria            |
| `REQ-GOV`  | Detailed Implementation Plan | 2 Delivery Governance, Sprint 0 exit |

## Governance (Sprint 0)

| ID         | Requirement                                                                 | Test ID                                           | Sprint | Status |
| ---------- | --------------------------------------------------------------------------- | ------------------------------------------------- | ------ | ------ |
| REQ-GOV-01 | Controlled documents are immutable except through a reviewed change process | `test_controlled_document_is_unmodified`          | 0      | DONE   |
| REQ-GOV-02 | The controlled set is exactly seven documents                               | `test_controlled_document_count_is_exactly_seven` | 0      | DONE   |
| REQ-GOV-03 | A clean clone runs documented setup and all smoke checks                    | Checkpoint A clean-clone run                      | 0      | DONE   |
| REQ-GOV-04 | Claude Code and humans use the same pinned skill pack                       | `agent-skills.lock` + `.claude/settings.json`     | 0      | DONE   |
| REQ-GOV-05 | Secrets never reach version control                                         | gitleaks hook + `.gitignore`                      | 0      | DONE   |

## Product acceptance (PRD section 17)

| ID         | Requirement                                                                   | Test ID | Sprint | Status |
| ---------- | ----------------------------------------------------------------------------- | ------- | ------ | ------ |
| REQ-PRD-01 | Basic rate and history features work during an OpenAI outage                  | TBD     | 4, 7   | TBD    |
| REQ-PRD-02 | Every important price displays source, timestamp, and freshness               | TBD     | 4      | TBD    |
| REQ-PRD-03 | Detailed analysis contains no unsupported prices or calculations              | TBD     | 9      | TBD    |
| REQ-PRD-04 | Causal claims include evidence and timeline alignment                         | TBD     | 9      | TBD    |
| REQ-PRD-05 | Duplicate requests reuse an existing queued or completed report               | TBD     | 9      | TBD    |
| REQ-PRD-06 | With one quota unit left, only one of two simultaneous requests is accepted   | TBD     | 9      | TBD    |
| REQ-PRD-07 | Validation failure triggers at most one repair before degraded output         | TBD     | 8, 9   | TBD    |
| REQ-PRD-08 | Queue saturation never blocks public rate and history endpoints               | TBD     | 9      | TBD    |
| REQ-PRD-09 | Admin trace shows model and tool metadata without hidden reasoning or secrets | TBD     | 12     | TBD    |

## Application flow (Application Flow section 15)

| ID          | Requirement                                                              | Test ID | Sprint | Status |
| ----------- | ------------------------------------------------------------------------ | ------- | ------ | ------ |
| REQ-FLOW-01 | Basic rate survives an OpenAI outage                                     | TBD     | 7      | TBD    |
| REQ-FLOW-02 | Duplicate request reuses a matching queued or completed report           | TBD     | 9      | TBD    |
| REQ-FLOW-03 | Quota race: one unit left, only one request succeeds                     | TBD     | 9      | TBD    |
| REQ-FLOW-04 | Stale data yields no full causal conclusion without a visible limitation | TBD     | 8      | TBD    |
| REQ-FLOW-05 | Provider fallback is labelled and audited                                | TBD     | 3      | TBD    |
| REQ-FLOW-06 | At most one validator repair before degraded output                      | TBD     | 8      | TBD    |
| REQ-FLOW-07 | AI saturation does not block basic endpoints                             | TBD     | 9      | TBD    |
| REQ-FLOW-08 | Report delivery failure keeps the report in-app; email retried           | TBD     | 11     | TBD    |
| REQ-FLOW-09 | Backend rejects unauthorised admin access                                | TBD     | 6, 12  | TBD    |
| REQ-FLOW-10 | Traces expose no secrets or hidden reasoning                             | TBD     | 12     | TBD    |
| REQ-FLOW-11 | Every runtime model call resolves to `gpt-5.4-mini`                      | TBD     | 7      | TBD    |
| REQ-FLOW-12 | Each model call records task policy and prompt/schema version            | TBD     | 7      | TBD    |

## Database (Backend Database Schema section 19)

| ID        | Requirement                                                            | Test ID | Sprint | Status |
| --------- | ---------------------------------------------------------------------- | ------- | ------ | ------ |
| REQ-DB-01 | Duplicate unchanged provider values create no unnecessary observations | TBD     | 3      | TBD    |
| REQ-DB-02 | Current-rate reads return source, timestamps, freshness, discrepancy   | TBD     | 4      | TBD    |
| REQ-DB-03 | Quota race with one unit remaining allows one reservation              | TBD     | 9      | TBD    |
| REQ-DB-04 | Analysis idempotency returns the original request for a repeated key   | TBD     | 9      | TBD    |
| REQ-DB-05 | Outbox state and domain state commit atomically                        | TBD     | 2      | TBD    |
| REQ-DB-06 | User A cannot access User B's data via SQL or API paths                | TBD     | 2, 6   | TBD    |
| REQ-DB-07 | Every completed analysis is reproducible to its inputs and versions    | TBD     | 9      | TBD    |
| REQ-DB-08 | Partition and index plans meet latency targets on representative data  | TBD     | 15     | TBD    |

## Contracts (API/Event/Provider Contracts section 15)

| ID         | Requirement                                                                          | Test ID | Sprint | Status |
| ---------- | ------------------------------------------------------------------------------------ | ------- | ------ | ------ |
| REQ-API-01 | The web client can implement every P0 journey from documented contracts alone        | TBD     | 6      | TBD    |
| REQ-API-02 | Repeated detailed-analysis requests cannot double-reserve quota or duplicate jobs    | TBD     | 9      | TBD    |
| REQ-API-03 | Unknown provider formats fail closed without corrupting market tables                | TBD     | 3      | TBD    |
| REQ-API-04 | Every domain state change needing downstream work creates an outbox event atomically | TBD     | 2      | TBD    |
| REQ-API-05 | No contract exposes credentials, hidden reasoning, raw payloads, or cross-user data  | TBD     | 12     | TBD    |
| REQ-API-06 | Model and tool outputs cannot bypass deterministic validation or typed schemas       | TBD     | 7      | TBD    |

## User experience (UI/UX Recommendations section 13)

| ID        | Requirement                                                                        | Test ID | Sprint | Status |
| --------- | ---------------------------------------------------------------------------------- | ------- | ------ | ------ |
| REQ-UX-01 | Users immediately identify 22K/24K rates, movement, source, time, freshness        | TBD     | 4      | TBD    |
| REQ-UX-02 | Facts and AI inference are visually separated                                      | TBD     | 8      | TBD    |
| REQ-UX-03 | Delayed, stale, fallback, conflicting, estimated, unavailable states are explained | TBD     | 4      | TBD    |
| REQ-UX-04 | Detailed-analysis progress is visible and resumable                                | TBD     | 9      | TBD    |
| REQ-UX-05 | Supporting sources and timestamps are inspectable                                  | TBD     | 8      | TBD    |
| REQ-UX-06 | P0 journeys meet WCAG 2.2 AA                                                       | TBD     | 15     | TBD    |
| REQ-UX-07 | Mobile P0 journeys avoid unintended horizontal scrolling at 360 px                 | TBD     | 15     | TBD    |
| REQ-UX-08 | Quota behaviour is understandable                                                  | TBD     | 9      | TBD    |
| REQ-UX-09 | No guaranteed or personalised trading instruction is presented                     | TBD     | 8      | TBD    |
| REQ-UX-10 | Safe trace excludes hidden reasoning and secrets                                   | TBD     | 12     | TBD    |
| REQ-UX-11 | OpenAI outage leaves current rates and history usable                              | TBD     | 7      | TBD    |
| REQ-UX-12 | Model branding does not dominate the consumer experience                           | TBD     | 8      | TBD    |

## Maintenance

Add a row when a controlled document gains an acceptance criterion. Fill in `Test ID` in the PR that
implements it, and move `Status` to `DONE` only when the named test passes in CI. A requirement whose
sprint has closed while still `TBD` is a gap and blocks that sprint's exit criteria.
