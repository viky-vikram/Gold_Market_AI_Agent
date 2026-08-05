# AurumIQ — API, Event, Provider, Model, and Tool Contracts

**Document ID:** GMAA-CONTRACT-001  
**Version:** 1.2 Claude Code + Agent-Skills Enforced  
**Date:** 2026-08-05  
**Status:** Approved for implementation  
**Supersedes:** Version 1.1 Agent-Skills Enforced dated 2026-08-05  
**Contract style:** OpenAPI 3.1 semantics, JSON Schema 2020-12, CloudEvents-inspired domain envelopes

---

## 1. Purpose

Define the stable boundaries between the web client, FastAPI services, background workers, LangGraph nodes, OpenAI integration, market/news providers, and event consumers.

Generated OpenAPI and JSON Schema files become executable artifacts in `packages/contracts`. This document defines the normative intent.

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

### Contract skill routing

| Contract activity | Mandatory Addy Osmani skills |
|---|---|
| REST, event, provider, model, tool, or module interface design | `/agent-skills:api-and-interface-design` |
| Framework, OpenAPI, JSON Schema, CloudEvents, SDK, or provider behaviour | `/agent-skills:source-driven-development` |
| Authentication, authorisation, validation, idempotency, webhook, secret, or trust boundary | `/agent-skills:security-and-hardening` |
| Contract implementation and consumer/provider verification | `/agent-skills:incremental-implementation`, `/agent-skills:test-driven-development` |
| Breaking, deprecated, or migrated contract | `/agent-skills:deprecation-and-migration`, `/agent-skills:documentation-and-adrs` |
| Request IDs, trace IDs, event delivery, provider health, or production diagnostics | `/agent-skills:observability-and-instrumentation` |
| Failed compatibility or integration test | `/agent-skills:debugging-and-error-recovery` |

A contract change is incomplete until producer and consumer tests, compatibility checks, security validation, generated artifacts, and the selected skill's verification evidence all pass.

---

## 2. Contract Rules

1. Public REST base path is `/v1`; breaking changes require `/v2` or a documented compatibility migration.
2. JSON uses `snake_case`; timestamps are RFC 3339 UTC; user-facing quota dates also include the IST date/reset time.
3. Prices are decimal strings in JSON to avoid binary floating-point loss.
4. Every response includes `request_id`; asynchronous resources also include `trace_id` and resource ID.
5. Protected writes accept `Idempotency-Key` where specified.
6. Clients must ignore unknown response fields; servers reject unknown request fields for security-sensitive commands.
7. Errors use one envelope and stable machine-readable codes.
8. Domain events are at-least-once; consumers deduplicate by `event_id`.
9. Provider payloads are normalised behind typed adapters; provider-specific fields never leak into core business contracts.
10. Model output that affects business logic uses strict Structured Outputs and a versioned schema.

## 3. Common REST Types

### 3.1 Success metadata

```json
{
  "request_id": "req_...",
  "trace_id": "tr_...",
  "generated_at": "2026-08-05T07:15:00Z",
  "data_freshness": "fresh"
}
```

### 3.2 Error envelope

```json
{
  "error": {
    "code": "ANALYSIS_QUOTA_EXHAUSTED",
    "message": "Your detailed-analysis quota is exhausted for the current IST day.",
    "details": {"reset_at": "2026-08-05T18:30:00Z"},
    "retryable": false
  },
  "request_id": "req_...",
  "trace_id": "tr_..."
}
```

Core error codes: `VALIDATION_ERROR`, `UNAUTHENTICATED`, `FORBIDDEN`, `NOT_FOUND`, `CONFLICT`, `RATE_LIMITED`, `IDEMPOTENCY_CONFLICT`, `ANALYSIS_QUOTA_EXHAUSTED`, `ANALYSIS_CAPACITY_REACHED`, `MARKET_DATA_INSUFFICIENT`, `PROVIDER_UNAVAILABLE`, `AI_TEMPORARILY_UNAVAILABLE`, `BUDGET_CIRCUIT_OPEN`, `INTERNAL_ERROR`.

### 3.3 Freshness

`fresh | delayed | stale | unavailable | conflicting | estimated | fallback`.

## 4. Public Market APIs

### `GET /v1/public/rates/current`

Query: `city=chennai`, optional `purity=22|24`, `unit_grams=1|8|10`.

Response includes each rate's instrument, purity, unit value, derived values, currency, direction and change, observation/market/retrieval timestamps, source, freshness, fallback, discrepancy range, and charges disclaimer.

### `GET /v1/public/rates/history`

Query: `city`, `purity`, `from`, `to`, `interval=daily|weekly`, optional `overlay=xau_usd|usd_inr|mcx_gold`.

Limits: guest preview range is configurable; authenticated export limits are role-based. Missing intervals are explicit, never silently interpolated.

### `GET /v1/public/market-summary`

Returns current rates, deterministic comparison, chart preview, and the latest reusable validated Simple Analysis when available. It must not trigger a new LLM call.

### `GET /v1/public/methodology`

Returns source categories, freshness definitions, calculation versions, limitations, guidance disclaimer, and current provider-neutral model methodology.

## 5. Authenticated User APIs

### `GET /v1/me`

Returns profile, roles, preferences, entitlements, and feature flags applicable to the user.

### `PATCH /v1/me/preferences`

Strict body containing display/unit/purity/notification preferences. Owner only.

### `GET /v1/dashboard`

Composite read model: rates, comparison, history preview, reusable Simple Analysis, alert summary, latest report, and quota. Partial panel failures are represented per section instead of failing the entire response.

## 6. Analysis APIs

### `POST /v1/analyses`

Headers: bearer auth, `Idempotency-Key` required for detailed mode.

Request:

```json
{
  "mode": "detailed",
  "city": "chennai",
  "purity": 22,
  "unit_grams": "1",
  "comparison_period": "30d",
  "purchase_objective": "jewellery_purchase_within_30_days",
  "question": "Explain the strongest drivers and uncertainty."
}
```

Rules:

- Reject unsupported investment/trading instructions or minimise them to safe informational scope.
- A reusable completed report returns `200` with `reused=true`.
- A new asynchronous analysis returns `202` with `analysis_id`, status, progress URL, estimated queue class (not a guaranteed time), quota reservation, and safe stage list.
- Same idempotency key plus equivalent body returns the original response.
- Same key plus different body returns `409 IDEMPOTENCY_CONFLICT`.

### `GET /v1/analyses/{analysis_id}`

Owner/authorised role only. Returns current status, safe progress stage, timestamps, quota disposition, failure code, and final report when complete. Never returns hidden reasoning.

### `GET /v1/analyses`

Cursor pagination, filters by mode/status/date. User sees owned analyses; analysts/admin rules are explicit and audited.

### `POST /v1/analyses/{analysis_id}/cancel`

Allowed only before the configured non-cancellable stage. Cancellation outcome defines quota release/finalisation.

### `POST /v1/analyses/{analysis_id}/feedback`

Body: rating, issue categories, optional comment. Idempotent per user/analysis.

### Final analysis result shape

```json
{
  "analysis_id": "uuid",
  "mode": "detailed",
  "market_conclusion": "...",
  "facts": [{"label":"22K rate","value":"...","source_ref":"src_1"}],
  "comparisons": [{"period":"1d","absolute_change":"...","percentage_change":"..."}],
  "drivers": [{"rank":1,"title":"...","evidence_refs":["src_2"],"confidence":"medium"}],
  "counter_factors": [{"title":"...","evidence_refs":["src_3"]}],
  "guidance": {"type":"conditional_jewellery_support","text":"..."},
  "confidence": {"level":"medium","reasons":["..."]},
  "limitations": ["..."],
  "sources": [{"id":"src_1","name":"...","published_at":null,"retrieved_at":"..."}],
  "freshness": {"overall":"fresh","as_of":"..."},
  "methodology": {"calculation_version":"...","model_policy_version":"...","schema_version":"..."}
}
```

## 7. Usage, Alerts, Reports, and Exports

### `GET /v1/usage`

Returns quota type, IST date, limit, reserved, finalised, released/adjusted, remaining, reset time, and recent consumption. No pricing secrets.

### Alert endpoints

- `POST /v1/alerts`
- `GET /v1/alerts`
- `GET /v1/alerts/{id}`
- `PATCH /v1/alerts/{id}`
- `DELETE /v1/alerts/{id}` (deactivate)
- `GET /v1/alerts/{id}/events`

Conditions: price threshold, percentage movement, material-movement rule, daily-report-ready. Server validates threshold bounds and cooldown.

### Report endpoints

- `POST /v1/reports` creates/returns an asynchronous generation resource.
- `GET /v1/reports/{id}` returns status and time-limited download link when ready.
- `GET /v1/reports` lists owned reports.
- `POST /v1/reports/{id}/deliveries` requests permitted email delivery.
- `GET /v1/exports/history` returns or creates a CSV export according to size.

## 8. Administrator APIs

Admin routes require verified role and audit entry.

- `GET /v1/admin/operations/overview`
- `GET /v1/admin/providers`
- `PATCH /v1/admin/providers/{id}`
- `POST /v1/admin/providers/{id}/health-check`
- `GET /v1/admin/data-quality/issues`
- `GET /v1/admin/traces/{trace_id}` (redacted safe trace)
- `GET /v1/admin/usage/costs`
- `GET /v1/admin/evaluations`
- `POST /v1/admin/model-releases`
- `POST /v1/admin/model-releases/{id}/approve`
- `POST /v1/admin/model-releases/{id}/activate`
- `POST /v1/admin/model-releases/{id}/rollback`
- `GET/PATCH /v1/admin/feature-flags`
- `GET /v1/admin/audit-logs`

Activation cannot bypass required evaluation, approval separation, or rollback metadata.

## 9. Domain Event Envelope

```json
{
  "specversion": "1.0",
  "id": "uuid",
  "type": "aurumiq.analysis.completed.v1",
  "source": "urn:aurumiq:api",
  "subject": "analysis/{analysis_id}",
  "time": "2026-08-05T07:15:00Z",
  "datacontenttype": "application/json",
  "trace_id": "tr_...",
  "correlation_id": "req_...",
  "data": {}
}
```

Event payloads contain IDs and stable facts, not secrets or large narrative bodies. Consumers fetch authorised details when needed.

## 10. Event Catalogue

| Event | Producer | Main consumers | Minimum data |
|---|---|---|---|
| `aurumiq.market.observation.accepted.v1` | ingestion | aggregate, quality, current selector | observation/instrument/source IDs, value, timestamps, status |
| `aurumiq.market.state.changed.v1` | market service | cache invalidation, alerts, simple-analysis scheduler | state ID, fingerprint, changed instruments, freshness |
| `aurumiq.provider.health.changed.v1` | health service | admin notifications, routing | provider, capability, previous/new state |
| `aurumiq.analysis.requested.v1` | API | analysis worker | analysis ID, mode, state ID, policy bundle |
| `aurumiq.analysis.status.changed.v1` | worker | UI notifier, ops | analysis ID, old/new status, safe stage |
| `aurumiq.analysis.completed.v1` | worker | reports, notifications, usage | analysis/run IDs, validation, quota disposition |
| `aurumiq.analysis.failed.v1` | worker | notification, ops | analysis ID, failure code, retryable, quota disposition |
| `aurumiq.alert.triggered.v1` | alert engine | notification worker | alert/event IDs, triggering state |
| `aurumiq.report.ready.v1` | report worker | delivery, UI notifier | report ID, owner ID, expiry |
| `aurumiq.delivery.failed.v1` | delivery worker | retry/ops | delivery ID, channel, error code |
| `aurumiq.budget.circuit.changed.v1` | cost controller | API, workers, admin | state, threshold, reason |

### Event semantics

- Outbox insertion and domain update are one database transaction.
- Publisher retries with exponential backoff and dead-letter escalation.
- Consumers record processed `event_id` or use a unique business dedupe key.
- Events are immutable. Corrections are new events.
- Additive fields are backward compatible. Removing/renaming fields requires a new event version.

## 11. Provider Interface Contracts

```python
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Protocol, Sequence

class Health(str, Enum):
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNAVAILABLE = "unavailable"

@dataclass(frozen=True)
class ProviderCapability:
    name: str
    instruments: tuple[str, ...]
    expected_delay_seconds: int
    redistribution_allowed: bool
    licence_id: str

@dataclass(frozen=True)
class NormalizedObservation:
    instrument_code: str
    value: Decimal
    currency: str
    unit_code: str
    observed_at: datetime
    market_at: datetime | None
    retrieved_at: datetime
    provider_record_id: str | None
    is_estimated: bool
    payload_hash: str

class MarketDataProvider(Protocol):
    code: str
    async def capabilities(self) -> Sequence[ProviderCapability]: ...
    async def fetch_latest(self, instrument_codes: Sequence[str]) -> Sequence[NormalizedObservation]: ...
    async def fetch_history(self, instrument_code: str, start: datetime, end: datetime) -> Sequence[NormalizedObservation]: ...
    async def health_check(self) -> tuple[Health, dict[str, str]]: ...
```

News provider output includes canonical URL, title, publisher, publication/event/retrieval timestamps, document type, language, content hash, licence metadata, and text/object reference.

### Provider requirements

- Timeouts and retries are adapter configuration, not embedded business logic.
- Validate TLS, content type, schema, units, currencies, and timestamp plausibility.
- Normalisation is deterministic and unit-tested with captured permitted fixtures.
- Provider adapters cannot write directly to core tables; ingestion services validate and persist.
- Provider errors map to stable classes: `ProviderAuthError`, `ProviderRateLimitError`, `ProviderTimeoutError`, `ProviderSchemaError`, `ProviderLicenceError`, `ProviderUnavailableError`.
- Fallback selection uses configured priority, freshness, legal permission, and health; fallback is visible in stored metadata and UI.
- Raw payload logging is disabled by default and always redacted.

## 12. OpenAI Model Contract

All runtime tasks use `gpt-5.4-mini` through the Responses API and a versioned `ModelPolicy`.

```python
class ModelPolicy(BaseModel):
    task: str
    model: Literal["gpt-5.4-mini"]
    reasoning_effort: Literal["none", "low", "medium", "high"]
    max_output_tokens: int
    timeout_seconds: float
    max_retries: int
    prompt_version: str
    output_schema_version: str
    allowed_tools: tuple[str, ...]
```

Rules:

1. Model policy is resolved by task, environment, and approved release—not user input.
2. Business-producing calls use JSON Schema Structured Outputs.
3. Tool calls are validated against strict argument schemas and an allowlist.
4. Tool results are untrusted data and delimited from instructions.
5. One model-output repair maximum; further failure produces deterministic degraded output.
6. No automatic switch to a larger model.
7. Store response ID, model ID, reasoning policy, prompt/schema versions, tokens, cost, latency, and validation result; never store hidden reasoning.
8. Current rates and calculations are never accepted from unverified model text.

## 13. Typed Tool Contract

```python
class ToolResult(BaseModel):
    tool_name: str
    tool_version: str
    status: Literal["success", "partial", "failed"]
    data: dict
    source_refs: list[str]
    freshness: str
    warnings: list[str]
    trace_id: str
```

Every tool has an explicit input/output schema, permission class, timeout, maximum result size, caching policy, deterministic/non-deterministic designation, and test fixture. Tools do not expose secrets, raw SQL, arbitrary URLs, or unrestricted filesystem/network access to the model.

## 14. Compatibility and Contract Testing

CI gates:

- OpenAPI lint and generated-client diff.
- JSON Schema validation for examples and golden payloads.
- Consumer-driven tests between web/API and API/workers.
- Event schema compatibility and idempotency tests.
- Provider fixture contract tests including malformed/stale/conflicting responses.
- RLS and authorisation tests for every protected endpoint.
- Structured-output conformance, refusal, timeout, and repair tests.
- Decimal and timestamp round-trip tests.

## 15. Contract Acceptance Criteria

- The web client can implement every P0 journey using documented contracts only.
- Repeated detailed-analysis requests cannot double reserve quota or create duplicate jobs.
- Unknown provider formats fail closed without corrupting market tables.
- Every domain state change that requires downstream processing creates an outbox event atomically.
- No contract exposes credentials, hidden reasoning, raw unrestricted provider payloads, or cross-user data.
- Model and tool outputs cannot bypass deterministic validation or typed schemas.
