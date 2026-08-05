# AurumIQ — Detailed Implementation Plan

**Document ID:** GMAA-PLAN-001  
**Version:** 1.2 Claude Code + Agent-Skills Enforced  
**Date:** 2026-08-05  
**Status:** Approved skill-driven execution baseline  
**Supersedes:** Version 1.1 Agent-Skills Enforced dated 2026-08-05  
**Delivery style:** Tested vertical slices with controlled specifications

---

## 1. Objective

Build the Chennai-first AurumIQ MVP from an empty repository to a production-demo release while preserving deterministic financial correctness, provider independence, OpenAI cost controls, security, observability, accessibility, and rollback capability.

The plan is sequence-based. Sprint numbering indicates order, not a promise of calendar duration.

## Addy Osmani Agent-Skills Workflow Mandate (Normative)

In these controlled documents, **`agent-skills` means only the production engineering workflow pack published at `addyosmani/agent-skills`**. It does not mean AurumIQ's runtime LangGraph market-analysis agents, and it must not be replaced by a generic project-local skill summary.

Authoritative source and Claude Code integration:

- Repository: `https://github.com/addyosmani/agent-skills`
- Development environment: Claude Code CLI and its supported IDE integration
- Marketplace installation inside Claude Code:

  ```text
  /plugin marketplace add addyosmani/agent-skills
  /plugin install agent-skills@addy-agent-skills
  ```

- HTTPS fallback when GitHub SSH cloning is unavailable:

  ```text
  /plugin marketplace add https://github.com/addyosmani/agent-skills.git
  /plugin install agent-skills@addy-agent-skills
  ```

- Meta-skill invoked at the start of work: `/agent-skills:using-agent-skills`
- Task-specific skill invocation: `/agent-skills:<skill-name>`
- Lifecycle command wrappers, when used: `/agent-skills:spec`, `/agent-skills:plan`, `/agent-skills:build`, `/agent-skills:test`, `/agent-skills:review`, `/agent-skills:webperf`, `/agent-skills:code-simplify`, and `/agent-skills:ship`
- Skill definitions: the actual `skills/<skill-name>/SKILL.md` files installed from the authoritative repository

At repository bootstrap, the team must record the installed repository commit SHA in an `agent-skills.lock` file. Upgrades require human review, a documented change record, and revalidation of affected gates.

### Claude Code execution requirements

1. Start Claude Code from the AurumIQ repository root so the root `CLAUDE.md`, project settings, and repository context are applied consistently.
2. Keep the root `CLAUDE.md` concise. It must point Claude Code to these seven controlled documents, define their precedence, require the namespaced Addy Osmani skills, list approved build/test commands, and prohibit silent edits to controlled specifications. Do not copy Addy Osmani's repository-level `CLAUDE.md` or paste complete upstream `SKILL.md` bodies into the project `CLAUDE.md`.
3. Use fully namespaced commands such as `/agent-skills:using-agent-skills` and `/agent-skills:test-driven-development`. This prevents accidental use of similarly named Claude Code bundled skills or skills from another plugin.
4. After installation or upgrade, verify the plugin is enabled through `/plugin`, confirm the commands are visible through `/help`, invoke `/agent-skills:using-agent-skills`, and record the observed plugin version or commit SHA.
5. Claude Code may automatically select an applicable installed skill, but explicit invocation remains mandatory at controlled task boundaries and must be recorded as evidence.
6. Claude Code is the development assistant only. AurumIQ runtime agents continue to use OpenAI `gpt-5.4-mini` through the Responses API.

### Mandatory operating rules

1. Begin every implementation, design, migration, test, review, or release task by invoking `/agent-skills:using-agent-skills`.
2. Let the meta-skill route the task to the applicable Addy Osmani skill or skills. If a skill has even a plausible match, load and follow the actual `SKILL.md` workflow before proceeding.
3. Do not implement directly when an applicable skill exists. Complete its required specification, planning, verification, review, and exit gates.
4. Use `/agent-skills:git-workflow-and-versioning` for every code change and `/agent-skills:code-review-and-quality` before every merge.
5. Invoke `/agent-skills:debugging-and-error-recovery` immediately when tests, builds, migrations, runtime behaviour, or external integrations fail. Do not bypass or weaken a failing gate to continue.
6. Record evidence in the work item or pull request: task ID, installed agent-skills commit SHA, skills invoked, completed checkpoints, tests/commands run, results, unresolved risks, and approved exceptions.
7. A task is not complete when skill invocation or verification evidence is missing. Any exception requires explicit human approval and an ADR or controlled change record.

### Enforced execution lifecycle

Every ticket and pull request must follow the installed Addy Osmani lifecycle. The skill names below are exact invocations, not conceptual labels.

| Stage | Mandatory workflow |
|---|---|
| Discover | `/agent-skills:using-agent-skills` |
| Define | `/agent-skills:spec-driven-development`; add `/agent-skills:interview-me` or `/agent-skills:idea-refine` only when requirements remain unresolved |
| Plan | `/agent-skills:planning-and-task-breakdown` |
| Build | `/agent-skills:incremental-implementation`, `/agent-skills:test-driven-development`, `/agent-skills:git-workflow-and-versioning` |
| Ground | `/agent-skills:source-driven-development` when external frameworks, SDKs, providers, standards, or cloud behaviour affect the work |
| Verify failures | `/agent-skills:debugging-and-error-recovery` |
| Review | `/agent-skills:code-review-and-quality`; add `/agent-skills:security-and-hardening`, `/agent-skills:performance-optimization`, or `/agent-skills:doubt-driven-development` when triggered |
| Operate/ship | `/agent-skills:observability-and-instrumentation`, `/agent-skills:ci-cd-and-automation`, and `/agent-skills:shipping-and-launch` as applicable |

### Skill evidence required in every work item

```text
Agent-Skills source: addyosmani/agent-skills
Installed commit SHA: <sha>
Task ID: <GMAA-nnn>
Skills invoked: <exact namespaced `/agent-skills:<skill-name>` commands>
Skill checkpoints completed: <list>
Official sources verified: <links or N/A>
Tests/commands run: <list>
Observed results: <pass/fail with evidence>
Security/performance/observability impact: <summary>
Unresolved risks or approved exceptions: <none or reference>
Reviewer confirmation: <human reviewer>
```

Missing or fabricated skill evidence blocks merge. The workflow may select additional skills beyond the minimum mapping below; it may not omit a triggered skill merely because it is not listed in the sprint summary.

---

## 2. Delivery Governance

### Mandatory artifacts before code

- Approved PRD, TRD, UI/UX, flow, schema, contracts, and this implementation plan.
- Claude Code version recorded; pinned Addy Osmani `addyosmani/agent-skills` plugin installation verified through `/plugin`; `/help` and `/agent-skills:using-agent-skills` invocation tested.
- Decision owners are identified for architecture changes.
- Requirement IDs and acceptance criteria are present in the seven controlled documents and implementation tickets.
- Provider legal/technical approval register.
- Golden datasets and deterministic calculation fixtures.

### Branch and release policy

- Protected `main`; short-lived feature branches.
- Pull request required with requirement/ADR references, tests, security impact, migration impact, observability changes, and rollback notes.
- No direct production changes.
- Feature flags for incomplete or high-risk capabilities.
- Database migration and application deployment use expand–migrate–contract.

### Definition of Done for every work item

1. `/agent-skills:using-agent-skills` was invoked and routed the work to the applicable actual `SKILL.md` workflows.
2. Required skill checkpoints and evidence are recorded against the task.
3. Requirement and acceptance criteria are identified.
4. Tests fail before implementation where practical and pass after implementation.
5. Code follows layer and contract boundaries.
6. Security, privacy, cost, failure, and rollback paths are addressed.
7. Telemetry and actionable errors exist.
8. Documentation/contracts/migrations are updated.
9. `/agent-skills:code-review-and-quality` and any triggered specialist review gates pass.
10. CI passes, review feedback is resolved, and staging/runtime evidence is attached.

## 3. Workstreams

1. Governance and repository foundation.
2. Database and market-data ingestion.
3. Deterministic analytics and public APIs.
4. Authentication, dashboard, and history UX.
5. OpenAI/LangGraph analysis.
6. Alerts, reports, and notifications.
7. Administration, observability, and evaluations.
8. Security, performance, resilience, and release.

## 4. Phase 0 — Controlled Baseline and Repository Foundation

### Sprint 0: Governance and scaffold

**Mandatory task-specific skills:** `/agent-skills:spec-driven-development`, `/agent-skills:planning-and-task-breakdown`, `/agent-skills:git-workflow-and-versioning`, `/agent-skills:ci-cd-and-automation`, `/agent-skills:documentation-and-adrs`. Global `/agent-skills:using-agent-skills`, `/agent-skills:git-workflow-and-versioning`, and pre-merge `/agent-skills:code-review-and-quality` rules also apply.

Tasks:

- Install Claude Code and record `claude --version`.
- Install the Addy Osmani plugin with `/plugin marketplace add addyosmani/agent-skills` and `/plugin install agent-skills@addy-agent-skills`; use the HTTPS fallback when SSH cloning is unavailable.
- Verify `/plugin`, `/help`, `/agent-skills:using-agent-skills`, and at least one task-specific namespaced skill before implementation begins.
- Create a concise repository-root `CLAUDE.md` that points to these seven controlled documents, defines precedence and protected-file rules, requires namespaced skills, and lists approved setup/build/test commands without copying full upstream skills.
- Create monorepo structure from TRD.
- Add `agent-skills.lock`, `.env.example`, contribution guide, pull-request evidence template, ADR template, threat-model template, and runbook index.
- Configure Python/Node lock files, formatting, linting, type checking, test commands, pre-commit hooks, secret scanning, dependency scanning, and licence checks.
- Establish requirement-to-test traceability directly from the seven controlled documents into implementation tickets and automated test IDs.
- Create local Docker Compose for PostgreSQL/pgvector, Valkey, API, worker, and web.
- Create CI jobs: docs/contracts, backend, frontend, migrations/RLS, integration, E2E smoke, security.

Exit criteria:

- Clean clone can run documented setup and all empty/smoke checks.
- Claude Code and human contributors use the same pinned Addy Osmani skill pack, root `CLAUDE.md` policy, and the same seven controlled documents.
- Controlled documents are immutable except through reviewed change process.

### Sprint 1: Environment and observability skeleton

**Mandatory task-specific skills:** `/agent-skills:incremental-implementation`, `/agent-skills:test-driven-development`, `/agent-skills:observability-and-instrumentation`, `/agent-skills:security-and-hardening`, `/agent-skills:ci-cd-and-automation`. Global `/agent-skills:using-agent-skills`, `/agent-skills:git-workflow-and-versioning`, and pre-merge `/agent-skills:code-review-and-quality` rules also apply.

- Settings management with environment validation and secret-manager boundaries.
- Request/trace IDs, structured logs, OpenTelemetry bootstrap, health/readiness endpoints.
- Celery/Valkey connectivity and queue isolation skeleton.
- Supabase project environments and auth configuration baseline.
- Vercel/backend staging deployment skeleton with no production data.

Exit: one request traces from web to API, DB, Valkey, and worker in staging.

## 5. Phase 1 — Data Foundation and Public Current-Rate Slice

### Sprint 2: Database core

**Mandatory task-specific skills:** `/agent-skills:source-driven-development`, `/agent-skills:documentation-and-adrs`, `/agent-skills:planning-and-task-breakdown`, `/agent-skills:incremental-implementation`, `/agent-skills:test-driven-development`, `/agent-skills:security-and-hardening`, `/agent-skills:deprecation-and-migration`. Global `/agent-skills:using-agent-skills`, `/agent-skills:git-workflow-and-versioning`, and pre-merge `/agent-skills:code-review-and-quality` rules also apply.

- Implement schemas, enums, identity/profile/RBAC tables, market reference data, observations, current selections, ingestion runs, quality issues, outbox, and audit log.
- Add partitions, indexes, RLS, seed data, migration tests, backup/restore test.
- Implement repository layer and transaction boundaries.

Tests: migration upgrade/downgrade, RLS matrix, decimal/timestamp invariants, partition routing, outbox atomicity.

### Sprint 3: Provider framework and fixture provider

**Mandatory task-specific skills:** `/agent-skills:api-and-interface-design`, `/agent-skills:source-driven-development`, `/agent-skills:incremental-implementation`, `/agent-skills:test-driven-development`, `/agent-skills:security-and-hardening`, `/agent-skills:observability-and-instrumentation`. Global `/agent-skills:using-agent-skills`, `/agent-skills:git-workflow-and-versioning`, and pre-merge `/agent-skills:code-review-and-quality` rules also apply.

- Implement typed provider protocols, normalisation, source hierarchy, health/circuit breaker, dedupe hash, quality rules, and fallback selector.
- Add synthetic fixture provider first; add approved public/low-cost adapters only after legal register entry.
- Celery Beat schedules remain configurable by source type.

Tests: provider contract fixtures, malformed payloads, stale timestamps, unit mismatch, rate limit, timeout, unchanged value skip, fallback labelling.

### Sprint 4: Current-rate vertical slice

**Mandatory task-specific skills:** `/agent-skills:incremental-implementation`, `/agent-skills:test-driven-development`, `/agent-skills:api-and-interface-design`, `/agent-skills:frontend-ui-engineering`, `/agent-skills:browser-testing-with-devtools`, `/agent-skills:performance-optimization`. Global `/agent-skills:using-agent-skills`, `/agent-skills:git-workflow-and-versioning`, and pre-merge `/agent-skills:code-review-and-quality` rules also apply.

- Current observation selector and freshness calculator.
- Deterministic 1 g, 8 g, 10 g values and day comparison.
- Cache keys and invalidation from market-state events.
- Public current-rate and market-summary APIs.
- Next.js public rate cards with source/timestamps/freshness/disclaimer/degraded states.

Exit:

- P95 cache/DB targets meet PRD under expected load.
- OpenAI is not configured and all current-rate functionality works.

## 6. Phase 2 — History, Authentication, and Core Dashboard

### Sprint 5: Historical data and analytics

**Mandatory task-specific skills:** `/agent-skills:source-driven-development`, `/agent-skills:incremental-implementation`, `/agent-skills:test-driven-development`, `/agent-skills:api-and-interface-design`, `/agent-skills:frontend-ui-engineering`, `/agent-skills:performance-optimization`. Global `/agent-skills:using-agent-skills`, `/agent-skills:git-workflow-and-versioning`, and pre-merge `/agent-skills:code-review-and-quality` rules also apply.

- Historical backfill pipeline with legal limits and resumability.
- Aggregates, missing-period markers, deterministic comparison engine, calculation versioning.
- History API, chart/table model, role-based CSV export.
- ECharts history chart with accessible table alternative.

Tests: arithmetic golden dataset, time-zone boundary, missing data, provider change, leap day, CSV injection protection.

### Sprint 6: Authentication, RLS, and dashboard

**Mandatory task-specific skills:** `/agent-skills:security-and-hardening`, `/agent-skills:frontend-ui-engineering`, `/agent-skills:browser-testing-with-devtools`, `/agent-skills:incremental-implementation`, `/agent-skills:test-driven-development`. Global `/agent-skills:using-agent-skills`, `/agent-skills:git-workflow-and-versioning`, and pre-merge `/agent-skills:code-review-and-quality` rules also apply.

- Supabase Auth integration, session validation, profile and role claims.
- Dashboard composite endpoint and partial-panel failure contract.
- Authenticated shell, preferences, quota panel, history, source/freshness UI.
- Admin route protection scaffold.

Exit: cross-user and privilege escalation tests pass; guest and authenticated journeys pass Playwright.

## 7. Phase 3 — OpenAI and LangGraph Analysis

### Sprint 7: OpenAI client and evaluation harness

**Mandatory task-specific skills:** `/agent-skills:source-driven-development`, `/agent-skills:context-engineering`, `/agent-skills:api-and-interface-design`, `/agent-skills:test-driven-development`, `/agent-skills:doubt-driven-development`, `/agent-skills:security-and-hardening`. Global `/agent-skills:using-agent-skills`, `/agent-skills:git-workflow-and-versioning`, and pre-merge `/agent-skills:code-review-and-quality` rules also apply.

- Official OpenAI SDK wrapper using Responses API.
- `gpt-5.4-mini` task policies for routing/extraction/synthesis/critic/composition.
- Strict Structured Outputs, bounded tool calling, timeout/retry, redaction, token/cost accounting.
- Golden evaluation set for citation coverage, arithmetic non-invention, timeline alignment, safe guidance, prompt injection, stale-data behaviour.
- Mock/fake model gateway for deterministic tests.

Release gate: model policy passes agreed quality, latency, safety, and cost thresholds; no larger-model fallback.

### Sprint 8: Reusable Simple Analysis

**Mandatory task-specific skills:** `/agent-skills:context-engineering`, `/agent-skills:incremental-implementation`, `/agent-skills:test-driven-development`, `/agent-skills:doubt-driven-development`, `/agent-skills:observability-and-instrumentation`. Global `/agent-skills:using-agent-skills`, `/agent-skills:git-workflow-and-versioning`, and pre-merge `/agent-skills:code-review-and-quality` rules also apply.

- Market-state snapshots/fingerprints.
- Evidence retrieval, deterministic fact bundle, concise LangGraph flow, validator, one repair, degraded summary.
- Shared cached Simple Analysis scheduler and market-state invalidation.
- Consumer UX with facts/inference separation and citations.

Exit: cache reuse verified; Simple Analysis does not consume detailed user quota.

### Sprint 9: Detailed asynchronous analysis

**Mandatory task-specific skills:** `/agent-skills:planning-and-task-breakdown`, `/agent-skills:incremental-implementation`, `/agent-skills:test-driven-development`, `/agent-skills:debugging-and-error-recovery`, `/agent-skills:security-and-hardening`, `/agent-skills:observability-and-instrumentation`. Global `/agent-skills:using-agent-skills`, `/agent-skills:git-workflow-and-versioning`, and pre-merge `/agent-skills:code-review-and-quality` rules also apply.

- Analysis request/run/source/claim/tool/LLM tables.
- Idempotency, atomic quota reservation, deduplication, queue admission, durable status state machine.
- Full LangGraph: request validation, facts, history, evidence, Chennai context, synthesis, critic, composition, persistence.
- Polling status UI with safe stages; cancellation policy; feedback.
- OpenAI outage, schema failure, stale data, and queue saturation fallbacks.

Tests: quota race, duplicate request, one-repair maximum, process retry, worker crash recovery, cross-user access, no hidden reasoning, budget circuit.

## 8. Phase 4 — Alerts, Reports, and Notifications

### Sprint 10: Alerts

**Mandatory task-specific skills:** `/agent-skills:incremental-implementation`, `/agent-skills:test-driven-development`, `/agent-skills:security-and-hardening`, `/agent-skills:observability-and-instrumentation`. Global `/agent-skills:using-agent-skills`, `/agent-skills:git-workflow-and-versioning`, and pre-merge `/agent-skills:code-review-and-quality` rules also apply.

- Alert rule CRUD, deterministic evaluation after accepted market-state change, cooldown/dedupe, in-app events, email queue.
- Quiet-hour and notification preference handling.

### Sprint 11: Reports and exports

**Mandatory task-specific skills:** `/agent-skills:api-and-interface-design`, `/agent-skills:incremental-implementation`, `/agent-skills:test-driven-development`, `/agent-skills:security-and-hardening`, `/agent-skills:frontend-ui-engineering`, `/agent-skills:performance-optimization`. Global `/agent-skills:using-agent-skills`, `/agent-skills:git-workflow-and-versioning`, and pre-merge `/agent-skills:code-review-and-quality` rules also apply.

- Daily report orchestration that reuses validated analysis.
- PDF generation with source manifest, freshness, disclaimer, and accessible structure.
- CSV export hardening, object storage, time-limited downloads, email delivery retries.

Exit: email failure does not remove in-app report; duplicate events do not duplicate delivery.

## 9. Phase 5 — Administration and Observability

### Sprint 12: Operations and safe trace

**Mandatory task-specific skills:** `/agent-skills:observability-and-instrumentation`, `/agent-skills:security-and-hardening`, `/agent-skills:frontend-ui-engineering`, `/agent-skills:browser-testing-with-devtools`, `/agent-skills:test-driven-development`. Global `/agent-skills:using-agent-skills`, `/agent-skills:git-workflow-and-versioning`, and pre-merge `/agent-skills:code-review-and-quality` rules also apply.

- Provider health/data-quality screens.
- Redacted trace API/UI showing nodes, tools, timings, models, policy/prompt/schema versions, tokens, cost, validation, retries, fallbacks.
- Grafana dashboards and alerts for API latency/error, queues, provider health, stale data, OpenAI errors, validation, costs, budget.

### Sprint 13: Model/prompt governance and evaluations

**Mandatory task-specific skills:** `/agent-skills:context-engineering`, `/agent-skills:source-driven-development`, `/agent-skills:doubt-driven-development`, `/agent-skills:test-driven-development`, `/agent-skills:documentation-and-adrs`, `/agent-skills:observability-and-instrumentation`. Global `/agent-skills:using-agent-skills`, `/agent-skills:git-workflow-and-versioning`, and pre-merge `/agent-skills:code-review-and-quality` rules also apply.

- Prompt/model policy/release records and admin workflow: draft → offline evaluation → canary → approval → activation → monitoring → rollback.
- LangSmith datasets/evaluators and release evidence links.
- Feature flags and audit-log viewer.

Exit: unauthorised users cannot access operational internals; release rollback is demonstrated in staging.

## 10. Phase 6 — Production Hardening and Demo Release

### Sprint 14: Security and resilience

**Mandatory task-specific skills:** `/agent-skills:security-and-hardening`, `/agent-skills:doubt-driven-development`, `/agent-skills:test-driven-development`, `/agent-skills:debugging-and-error-recovery`, `/agent-skills:code-review-and-quality`. Global `/agent-skills:using-agent-skills`, `/agent-skills:git-workflow-and-versioning`, and pre-merge `/agent-skills:code-review-and-quality` rules also apply.

- Threat model review, OWASP ASVS-aligned controls, dependency/container scans, penetration-style API tests, prompt-injection tests.
- Backup restore, disaster recovery, provider/OpenAI/Valkey/worker/database fault drills.
- Rate limits, queue limits, circuit breakers, storage lifecycle, privacy deletion workflow.

### Sprint 15: Performance, accessibility, and release

**Mandatory task-specific skills:** `/agent-skills:performance-optimization`, `/agent-skills:frontend-ui-engineering`, `/agent-skills:browser-testing-with-devtools`, `/agent-skills:code-review-and-quality`, `/agent-skills:ci-cd-and-automation`, `/agent-skills:observability-and-instrumentation`, `/agent-skills:shipping-and-launch`. Global `/agent-skills:using-agent-skills`, `/agent-skills:git-workflow-and-versioning`, and pre-merge `/agent-skills:code-review-and-quality` rules also apply.

- k6/Locust tests for 25 concurrent normal users and 2–3 AI executions with queued overflow.
- P0 WCAG 2.2 AA audit and mobile 360 px journeys.
- Cost soak test and INR 8,000/month projection under expected demo usage.
- Operational runbooks, support checklist, release notes, go/no-go review, production canary and rollback rehearsal.

Release exit:

- All MVP completion criteria in PRD pass.
- No P0/P1 unresolved defect.
- Source/legal approval register is complete.
- Monitoring, alerts, backups, rollback, incident owner, and budget circuit are active.

## 11. Requirement-to-Test Traceability

Minimum test suites:

| Area | Required tests |
|---|---|
| Rates/calculations | unit golden tests, provider reconciliation, missing data, timestamps |
| Database | migrations, constraints, RLS, quota transactions, outbox, partitions |
| APIs | schema, auth, idempotency, errors, pagination, decimal serialization |
| Providers | contract, timeout, rate limit, malformed/stale/conflicting data |
| Agents | structured output, citations, tool allowlist, repair, degraded output |
| Safety | prohibited advice, prompt injection, data exfiltration, trace redaction |
| UI | guest/auth/admin P0 journeys, degraded states, quota, accessibility |
| Resilience | OpenAI/provider/worker/Valkey/database failure and recovery |
| Performance | public/API latency, queue isolation, concurrency, cost |

Every acceptance criterion receives a stable test ID, the exact Addy Osmani skills used to implement and verify it, and CI/staging/runtime evidence.

## 12. Risk Register and Mitigations

| Risk | Mitigation |
|---|---|
| Retail-rate source inconsistency | source hierarchy, discrepancy visibility, legal review, fallback metadata |
| LLM unsupported causality | deterministic fact bundle, evidence manifest, claim validator, one repair |
| Cost overrun | cache/reuse, quota, output bounds, task policies, global budget circuit |
| Queue starvation | dedicated AI queue/concurrency, public endpoint isolation |
| Duplicate quota charge | PostgreSQL ledger, idempotency, row locks, retry-safe finalisation |
| Schema drift | generated contracts, compatibility CI, migrations only |
| Cross-user data leak | RLS, server authz, negative security tests |
| Provider licence violation | licence registry and adapter capability gate |
| Vendor/model change | provider/model abstraction, versioned policy, eval and rollback |

## 13. Initial Implementation Ticket Order

1. `GMAA-001` Repository scaffold and CI.
2. `GMAA-002` Settings/secrets/telemetry skeleton.
3. `GMAA-003` Core database migration and RLS.
4. `GMAA-004` Provider protocols and fixture provider.
5. `GMAA-005` Ingestion, dedupe, quality, current selector.
6. `GMAA-006` Public current-rate API.
7. `GMAA-007` Public current-rate UI.
8. `GMAA-008` Historical analytics/API/chart.
9. `GMAA-009` Auth/profile/roles/dashboard.
10. `GMAA-010` OpenAI client and eval harness.
11. `GMAA-011` Simple Analysis.
12. `GMAA-012` Quota/idempotency/analysis queue.
13. `GMAA-013` Detailed LangGraph analysis.
14. `GMAA-014` Alerts.
15. `GMAA-015` Reports/email/exports.
16. `GMAA-016` Admin observability and model governance.
17. `GMAA-017` Security/resilience/performance/accessibility release gate.
