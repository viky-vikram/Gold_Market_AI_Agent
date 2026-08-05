# AurumIQ — Backend Database Schema Specification

**Document ID:** GMAA-DB-001  
**Version:** 1.2 Claude Code + Agent-Skills Enforced  
**Date:** 2026-08-05  
**Status:** Approved for implementation  
**Supersedes:** Version 1.1 Agent-Skills Enforced dated 2026-08-05  
**Database:** Supabase PostgreSQL with pgvector  
**Related documents:** PRD 1.4, TRD 1.4, Flow 1.2, Contracts 1.2

---

## 1. Purpose

Define the canonical logical and physical database design for AurumIQ, including ownership, keys, constraints, indexes, partitioning, Row Level Security, event outbox, auditability, retention, and migration rules.

The schema is Chennai-first but city- and instrument-extensible. Market facts are append-only observations; user state and operational configuration are mutable under audited workflows.

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

### Database skill routing

| Database activity | Mandatory Addy Osmani skills |
|---|---|
| New schema, table, relationship, constraint, index, partition, or material data-model decision | `/agent-skills:documentation-and-adrs`, `/agent-skills:source-driven-development`, `/agent-skills:doubt-driven-development` |
| Migration implementation | `/agent-skills:planning-and-task-breakdown`, `/agent-skills:incremental-implementation`, `/agent-skills:test-driven-development` |
| RLS, roles, secrets, audit data, retention, privacy, or cross-tenant boundaries | `/agent-skills:security-and-hardening` |
| Renaming, removing, backfilling, repartitioning, or compatibility transition | `/agent-skills:deprecation-and-migration` |
| Repository or service boundary affected by schema | `/agent-skills:api-and-interface-design` |
| Migration/test failure | `/agent-skills:debugging-and-error-recovery` |

Every migration pull request must include the skill evidence, forward and rollback strategy, compatibility impact, data-safety analysis, migration tests, RLS tests where applicable, and backup/restore implications.

---

## 2. Database Principles

1. Use UTC `timestamptz` for storage; present quota resets and user dates in Asia/Kolkata.
2. Use UUID primary keys generated by `gen_random_uuid()` unless a natural immutable identifier is explicitly defined.
3. Preserve source, market, observation, publication, retrieval, and ingestion timestamps separately.
4. Store money/price values as `numeric`, never binary floating point.
5. Store model narrative separately from deterministic facts and claims.
6. Use soft deactivation for providers, policies, prompts, and alerts; do not rewrite historical runs.
7. Enforce user ownership with RLS and service operations with audited server-side roles.
8. Publish domain events from a transactional outbox.
9. Avoid duplicate writes when a provider reports an unchanged value.
10. Apply migrations only through Alembic and reviewed SQL; production has no manual schema drift.

## 3. Required Extensions and Schemas

```sql
create extension if not exists pgcrypto;
create extension if not exists vector;
create extension if not exists btree_gist;

create schema if not exists app;
create schema if not exists market;
create schema if not exists content;
create schema if not exists ai;
create schema if not exists ops;
```

Supabase-owned `auth.users` remains the identity source. Application tables reference it but never duplicate passwords or authentication secrets.

## 4. Enumerations

```sql
create type app.user_role as enum ('registered_user','analyst','administrator');
create type market.observation_status as enum ('valid','estimated','fallback','stale','rejected');
create type market.quality_severity as enum ('info','warning','error','critical');
create type ai.analysis_mode as enum ('simple','detailed');
create type ai.analysis_status as enum (
  'queued','data_validation','historical_analysis','evidence_retrieval',
  'openai_analysis','validation','completed','failed_retryable',
  'failed_final','cancelled','expired'
);
create type ai.validation_status as enum ('pending','passed','passed_degraded','failed');
create type app.delivery_channel as enum ('in_app','email');
create type app.delivery_status as enum ('pending','sent','failed_retryable','failed_final');
create type ops.health_state as enum ('healthy','degraded','unavailable','disabled');
```

Enum additions require backward-compatible migrations. Renaming or removing an enum value requires a multi-step migration.

## 5. Identity, Roles, and Preferences

### 5.1 `app.profiles`

| Column | Type | Rules |
|---|---|---|
| `user_id` | uuid | PK, FK `auth.users(id)` on delete cascade |
| `display_name` | text | 1–100 chars, nullable |
| `timezone` | text | default `Asia/Kolkata` |
| `preferred_purity` | smallint | check in (22,24), default 22 |
| `preferred_unit_grams` | numeric(8,3) | positive, default 1 |
| `email_reports_enabled` | boolean | default false |
| `created_at`, `updated_at` | timestamptz | required |

### 5.2 `app.user_roles`

Composite PK `(user_id, role)`. Role grants and revocations write `ops.audit_logs`. Registration creates `registered_user`; analyst/admin assignment is privileged.

### 5.3 `app.user_preferences`

Versioned JSONB preferences for dashboard layout and notification windows. Validate against an application schema; do not store secrets.

## 6. Market Reference Data

### 6.1 `market.cities`

`id`, `code` unique (`CHE` initially), `name`, `state_code`, `country_code`, `timezone`, `is_visible`, timestamps.

### 6.2 `market.instruments`

| Column | Type | Description |
|---|---|---|
| `id` | uuid | PK |
| `code` | text | Unique, e.g. `CHE_GOLD_22K_G`, `XAU_USD_OZ`, `USD_INR`, `MCX_GOLD_NEAR` |
| `asset_class` | text | `retail_gold`, `spot_gold`, `fx`, `futures` |
| `city_id` | uuid | Nullable FK for local instruments |
| `purity_karat` | smallint | Nullable, check 1–24 |
| `quote_currency` | char(3) | ISO currency |
| `unit_code` | text | `gram`, `troy_ounce`, `contract` |
| `contract_metadata` | jsonb | Expiry, exchange, multiplier when applicable |
| `active` | boolean | Default true |

### 6.3 `market.data_sources`

Provider/source catalogue: `id`, `code`, `display_name`, `source_type`, `base_url`, `legal_basis`, `licence_summary`, `redistribution_allowed`, `priority`, `active`, timestamps.

### 6.4 `market.provider_configs`

Non-secret configuration only: schedules, timeout, retry, instrument mapping, freshness thresholds, circuit-breaker thresholds, and feature flag. API credentials remain in the secret manager. Changes are audited.

## 7. Market Observations

### 7.1 `market.observations`

Append-only, range-partitioned monthly by `observed_at`.

| Column | Type | Rules |
|---|---|---|
| `id` | bigint generated always as identity | PK within partition strategy |
| `instrument_id` | uuid | FK, required |
| `source_id` | uuid | FK, required |
| `observed_at` | timestamptz | Provider/market observation time |
| `market_at` | timestamptz | Nullable market/exchange timestamp |
| `retrieved_at` | timestamptz | Required |
| `ingested_at` | timestamptz | Default now() |
| `value` | numeric(24,8) | Required, positive where instrument requires |
| `bid`, `ask` | numeric(24,8) | Nullable |
| `currency` | char(3) | Required |
| `unit_code` | text | Required |
| `status` | `market.observation_status` | Required |
| `is_fallback` | boolean | Default false |
| `quality_score` | numeric(5,2) | 0–100 |
| `provider_record_id` | text | Nullable |
| `payload_hash` | char(64) | Normalised payload hash |
| `raw_payload_ref` | text | Optional object-store reference, never secret-bearing payload |
| `ingestion_run_id` | uuid | FK |

Uniqueness: `(source_id, instrument_id, observed_at, coalesce(provider_record_id,''))`. An additional current-value dedupe check compares normalised value/status to the last accepted observation and skips unnecessary insertions.

Indexes:

```sql
create index on market.observations (instrument_id, observed_at desc);
create index on market.observations (source_id, observed_at desc);
create index on market.observations (status, observed_at desc);
create index on market.observations using brin (observed_at);
```

### 7.2 `market.current_observations`

A materialized/current table maintained transactionally for low-latency reads. PK `(instrument_id)`. Stores selected observation ID, source priority, freshness state, discrepancy range, and `selected_at`. It is rebuildable from observations.

### 7.3 `market.market_aggregates`

Hourly/daily aggregates keyed by `(instrument_id, bucket_type, bucket_start, calculation_version)` with open/high/low/close, mean, count, missing interval count, and quality score.

### 7.4 `market.source_disagreements`

Records competing source values, selected source, absolute/percentage spread, resolution rule, and active/closed timestamps.

## 8. Ingestion and Data Quality

### 8.1 `ops.ingestion_runs`

Provider, scheduled/manual trigger, start/end, status, fetched/accepted/skipped/rejected counts, error code, trace ID, and configuration version.

### 8.2 `ops.data_quality_issues`

Entity reference, rule code, severity, observed/expected JSON, status, first/last seen, resolution, and related ingestion run. Critical unresolved issues can invalidate a market state.

### 8.3 `ops.provider_health`

Current health per provider capability: state, latency, consecutive failures, last success/failure, circuit state, and checked_at.

## 9. News, Events, and RAG

### 9.1 `content.documents`

Canonical news/official document record: URL hash unique, title, publisher, source ID, document type, language, published_at, retrieved_at, event_at, licence metadata, content hash, raw text/object-store reference, trust tier, and active flag.

### 9.2 `content.document_chunks`

`id`, `document_id`, `chunk_index`, `text`, `token_count`, `embedding vector`, `embedding_model`, `embedding_version`, and metadata JSONB. Unique `(document_id, chunk_index, embedding_version)`. Use HNSW/IVFFlat only after representative data-volume testing.

### 9.3 `content.market_events`

Normalised event: event type, entity, event_at, confirmed status, impact direction candidate, source count, summary, and confidence. AI extraction is not authoritative until deterministic/schema validation passes.

### 9.4 `content.document_event_links`

Many-to-many link with relationship type and evidence strength.

## 10. Market-State Fingerprints

### 10.1 `market.state_snapshots`

Immutable snapshot of selected observation IDs, aggregate versions, evidence cut-off, source-health summary, freshness summary, and `fingerprint` unique. The fingerprint is used for analysis reuse and cache invalidation.

A fingerprint must include: city, purity, requested comparison range, selected observation IDs, calculation version, evidence cutoff, prompt/schema/model policy versions where report compatibility requires them.

## 11. Analyses and Agent Runs

### 11.1 `ai.analysis_requests`

| Column | Type | Rules |
|---|---|---|
| `id` | uuid | PK |
| `user_id` | uuid | Nullable for system Simple Analysis; FK auth.users |
| `mode` | enum | Required |
| `status` | enum | Required |
| `request_payload` | jsonb | Validated, minimised |
| `request_fingerprint` | char(64) | Required |
| `market_state_id` | uuid | FK |
| `idempotency_key_hash` | char(64) | Nullable |
| `quota_reservation_id` | uuid | Nullable FK |
| `celery_task_id` | text | Nullable unique |
| `created_at`, `started_at`, `completed_at`, `expires_at` | timestamptz | |
| `failure_code` | text | Nullable |
| `trace_id` | text | Required |

Partial unique indexes prevent more than one active request for the same reusable fingerprint.

### 11.2 `ai.analysis_runs`

One request may have multiple bounded attempts. Stores attempt number, graph version, prompt bundle version, model policy ID, OpenAI response ID, token counts, estimated cost in USD and INR, validation status, confidence score, structured result JSONB, user-facing narrative, degraded reason, and timestamps.

### 11.3 `ai.analysis_sources`

Links a run to exact market observations, aggregates, documents, events, and retrieval scores. This is the evidence manifest used for citations and audits.

### 11.4 `ai.analysis_claims`

Stores each material claim with type (`fact`, `calculation`, `inference`, `guidance`), text, support references, confidence, validation result, and rejection reason. Unsupported claims are not presented.

### 11.5 `ai.tool_executions`

Tool name/version, validated arguments hash, result reference/hash, latency, status, error code, and trace/span IDs. Do not store secrets or unrestricted raw provider payloads.

### 11.6 `ai.llm_calls`

Task, model ID, reasoning effort, prompt/schema versions, OpenAI response ID, input/output/cached/reasoning token counts when available, latency, retry, finish status, cost, and redacted request/response hashes. Hidden chain-of-thought is never stored.

### 11.7 `ai.analysis_feedback`

Unique per `(analysis_request_id,user_id)` where appropriate; rating, issue categories, comment, created_at. Comments are treated as untrusted input.

## 12. Quotas and Usage

### 12.1 `app.quota_accounts`

Per user and quota type: daily limit, timezone, active, effective dates.

### 12.2 `app.quota_ledger`

Immutable ledger with operation `reserve`, `finalise`, `release`, `adjust`; amount; IST quota date; analysis ID; idempotency key; actor; reason; timestamps. Unique idempotency constraint prevents double charging.

Current remaining quota is derived transactionally or maintained in a locked summary row. PostgreSQL is authoritative; Valkey only accelerates locking and display.

### 12.3 `ops.usage_daily`

Aggregated by IST date, task, model, user tier, and environment: requests, successes, tokens, cost, latency percentiles, cache hits, and quota consumption.

## 13. Alerts, Reports, and Notifications

### 13.1 `app.alert_rules`

User-owned rule: instrument/city/purity, condition type, threshold, channel, quiet window, active status, cooldown, last triggered. Validate sensible thresholds.

### 13.2 `app.alert_events`

Rule, triggering observation/state, condition result, dedupe key, triggered_at, and delivery status. Unique dedupe key prevents repeated notifications for the same state.

### 13.3 `app.reports`

Owner/system report, report type, market state, analysis request, status, storage key, content hash, generated_at, expires_at, and source manifest version.

### 13.4 `app.report_deliveries`

Report, channel, recipient hash/reference, status, provider message ID, attempts, last error, sent_at. Never store unnecessary recipient secrets.

## 14. Model and Prompt Governance

### 14.1 `ai.prompt_versions`

Task, semantic version, content hash, template object-store/reference, schema version, approval status, author/approver, created/effective/retired timestamps.

### 14.2 `ai.model_policies`

Task, model (`gpt-5.4-mini`), reasoning effort, output limit, timeout, retries, tool allowlist, prompt version, schema version, active status, effective dates.

### 14.3 `ai.model_releases`

Policy bundle, evaluation report, canary status, approval, activated_at, rolled_back_at, and rollback reason.

## 15. Operations and Audit

### 15.1 `ops.outbox_events`

`id`, `event_type`, `event_version`, aggregate type/id, payload JSONB, trace ID, occurred_at, available_at, published_at, attempts, last_error. Inserted in the same transaction as the state change.

### 15.2 `ops.audit_logs`

Append-only actor, action, resource, before/after hashes or redacted deltas, request/trace IDs, IP/user-agent where permitted, occurred_at. No secrets or private model reasoning.

### 15.3 `ops.feature_flags`

Name, environment, enabled, rules JSONB, owner, version, effective dates, audit metadata.

## 16. Row Level Security

Enable RLS on every user-owned table. Representative policy intent:

```sql
alter table app.profiles enable row level security;
create policy profile_self_read on app.profiles
for select using (auth.uid() = user_id);
create policy profile_self_update on app.profiles
for update using (auth.uid() = user_id)
with check (auth.uid() = user_id);
```

Apply equivalent owner policies to preferences, alert rules/events, reports, analysis history, and feedback. Users cannot read raw LLM calls, tool traces, provider configs, audit logs, or other users' quota ledgers. Admin access is enforced server-side through verified role claims and audited service functions, not client-supplied flags.

## 17. Retention and Privacy

| Data | Default retention |
|---|---|
| Market observations/aggregates | At least 3 years; longer when licence permits |
| News document text/chunks | According to licence and source policy |
| Analysis reports and source manifests | 1 year for normal users; configurable |
| LLM/tool operational metadata | 90 days detailed, then aggregated |
| Audit logs | 1 year minimum |
| Failed raw payload references | 30 days unless needed for incident investigation |
| Idempotency records | 30 days |

Deletion requests remove or anonymise user-owned profile, preferences, alerts, feedback, and personal report references while preserving legally necessary aggregate/audit records.

## 18. Migration and Compatibility Rules

1. Alembic migration IDs are immutable and ordered.
2. Every migration has upgrade and tested downgrade or a documented irreversible reason.
3. Use expand–migrate–contract for destructive changes.
4. New non-null columns require safe defaults/backfill before enforcement.
5. Partition creation is automated ahead of time and monitored.
6. RLS policy tests run in CI with guest, owner, other-user, analyst, and admin contexts.
7. Seed data is deterministic and contains no production credentials.
8. Schema changes update contracts, ORM models, fixtures, and docs in the same pull request.

## 19. Database Acceptance Criteria

- Duplicate unchanged provider values do not create unnecessary market observations.
- Current-rate reads return the selected source, timestamps, freshness, and discrepancy metadata.
- Quota races with one unit remaining allow only one accepted reservation.
- Analysis idempotency returns the original request for repeated keys.
- Outbox state and domain state commit atomically.
- User A cannot access User B's alerts, reports, analyses, or profile through direct SQL/API paths.
- Every completed analysis is reproducible to its market state, source manifest, calculation, prompt, schema, model policy, and validation version.
- Partition and index plans meet the documented latency/load targets on representative data.
