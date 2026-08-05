# Gold Market AI Agent - Product Requirements Document

**Document ID:** GMAA-PRD-001  
**Version:** 1.4 Claude Code + Agent-Skills Enforced Baseline  
**Date:** 2026-08-05  
**Status:** Approved for implementation  
**Canonical format:** Markdown  
**Product working name:** AurumIQ  
**Supersedes:** Version 1.3 Agent-Skills Enforced Baseline dated 2026-08-05  

---

## Revision Summary

Version 1.4 retains the approved UI/UX, application-flow, OpenAI runtime-model, and Addy Osmani agent-skills decisions while selecting Claude Code as the implementation environment. All skill invocations use Claude Code's fully namespaced `/agent-skills:<skill-name>` form, with plugin verification, concise `CLAUDE.md` governance, evidence requirements, and a pinned repository version. The approved product scope, Chennai-first architecture, deterministic financial calculations, provider independence, quotas, observability, security, and cost-control principles remain unchanged.

## Approval Record

| Item | Decision | Approved baseline |
|---|---|---|
| UI/UX recommendations | Approved for implementation | Facts-first layout, progressive disclosure, safe trace, quota UX, degraded states, WCAG 2.2 AA, responsive P0 journeys |
| Application flow | Approved for implementation | Deterministic-first processing, asynchronous detailed analysis, deduplication, quota reservation, bounded repair, fallback, trace propagation |
| Runtime model | Approved | OpenAI `gpt-5.4-mini` through the Responses API for every runtime agent node |
| Development workflow | Approved | Claude Code with Addy Osmani `addyosmani/agent-skills`; fully namespaced `/agent-skills:using-agent-skills` is mandatory before task execution, with actual `SKILL.md` workflows, human review, and automated quality gates |

Approval does not authorise personalised investment advice, guaranteed price direction, unlicensed data redistribution, hidden chain-of-thought exposure, or silent model escalation.

---

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

### Product and requirement skill routing

| Product activity | Mandatory Addy Osmani skills |
|---|---|
| Unclear or incomplete requirement | `/agent-skills:using-agent-skills` → `/agent-skills:interview-me`; use `/agent-skills:idea-refine` when alternatives must be explored |
| New feature, material scope change, or behavioural change | `/agent-skills:spec-driven-development` |
| Breaking the approved scope into implementable work | `/agent-skills:planning-and-task-breakdown` |
| High-stakes financial, security, privacy, quota, or irreversible product decision | `/agent-skills:doubt-driven-development` |
| Decision that changes product intent, public behaviour, or controlled specifications | `/agent-skills:documentation-and-adrs` |
| Official framework/provider facts used to shape requirements | `/agent-skills:source-driven-development` |

The PRD is the product specification gate. No production code may begin for a feature until the relevant PRD requirement and acceptance criteria are explicit and the applicable skill workflow has cleared its human-review gate.

---

## 1. Executive Summary

AurumIQ is a production-shaped Gold Market AI Agent designed initially for Chennai consumers, jewellery buyers, and market learners. It provides current and historical Chennai 22K and 24K gold rates, compares price movements across time, and explains likely reasons for increases or decreases using international spot gold, USD/INR, MCX gold futures, macroeconomic events, and relevant financial news.

The MVP is Chennai-first while its architecture, data model, APIs, provider interfaces, and agent workflows remain ready for future multi-city expansion. The system provides evidence-based analysis and cautious decision support, but it does not issue guaranteed or personalised buy/sell trading instructions.

The product uses OpenAI `gpt-5.4-mini` through the OpenAI Responses API for agent routing, extraction, evidence synthesis, validation, and response composition. LangGraph remains the orchestration layer. Supabase PostgreSQL is the hosted database, Valkey provides caching and task coordination, Celery handles background processing, Next.js with TypeScript provides the frontend, FastAPI provides the backend, LangSmith Cloud provides agent observability, and OpenTelemetry with Grafana Cloud provides application and infrastructure observability.

Development follows spec-driven development, test-driven development, incremental implementation, controlled AI-assisted coding with Claude Code, Addy Osmani agent-skills, and automated quality gates.

---

## 2. Product Vision

> Enable ordinary users to understand not only what the Chennai gold rate is, but also how it changed, why it likely changed, how reliable the explanation is, and what cautious actions may be reasonable for their stated purchase objective.

### 2.1 Product promise

A user should be able to ask:

> “What is the Chennai gold rate today, how does it compare with yesterday, and why did it change?”

The system should respond with:

- Verified Chennai 22K and 24K prices.
- Absolute and percentage changes.
- Relevant historical comparisons.
- Supporting international and Indian market data.
- Ranked market drivers.
- Conflicting or counter-evidence.
- Source names and timestamps.
- Data freshness status.
- Confidence level.
- Cautious, non-personalised decision-support guidance.

---

## 3. Problem Statement

Gold-rate information is widely available, but users commonly face the following problems:

1. Different websites and jewellers display different values.
2. Many sources do not clearly show when a rate was updated.
3. Price changes are reported without explaining the underlying drivers.
4. Explanations may confuse correlation with causation.
5. Users cannot easily compare current prices with reliable historical records.
6. Consumers often receive trading-style recommendations unsuitable for jewellery-buying decisions.
7. Existing tools rarely expose confidence, data quality, fallback usage, or source disagreement.
8. AI-generated market explanations may hallucinate facts, dates, prices, or causes if they are not grounded in deterministic tools and verified sources.

AurumIQ addresses these problems by separating factual retrieval, deterministic calculation, market analysis, validation, and response generation.

---

## 4. Goals

### 4.1 Business and product goals

- Deliver a reliable Chennai gold-rate intelligence experience.
- Demonstrate a production-ready multi-agent architecture.
- Support up to 1,000 registered users in the MVP design.
- Support an expected initial range of 50–150 daily active users.
- Maintain operating costs within INR 8,000 per month during an active public demo, excluding licensed market-data fees.
- Create a provider-independent foundation that can adopt licensed market-data feeds later.
- Provide transparent source lineage, timestamps, freshness, confidence, and limitations.
- Build a reusable platform that can later add other Indian cities and precious metals.

### 4.2 User goals

- View the latest available Chennai 22K and 24K gold rates.
- Compare today with yesterday and selected historical periods.
- Understand why prices likely moved.
- Distinguish local retail rates from benchmarks and futures prices.
- View simple or detailed analysis.
- Set alerts and receive daily summaries.
- Download analysis reports and historical data.
- Trust that the system discloses stale, delayed, missing, estimated, or conflicting data.

### 4.3 Engineering goals

- Use deterministic code for financial calculations.
- Use LLMs for orchestration, synthesis, and explanation rather than factual price generation.
- Use OpenAI `gpt-5.4-mini` for all runtime agent nodes, with task-specific reasoning effort and output limits.
- Maintain typed tool contracts and schema-constrained model outputs.
- Include comprehensive observability, auditability, security, and automated testing.
- Apply spec-driven and test-driven development.
- Enable modular replacement of data providers, model versions, and hosting services.

---

## 5. Non-Goals for the MVP

The MVP will not provide:

- Personalised investment advice.
- Guaranteed BUY, SELL, or profit predictions.
- Automated trading or order placement.
- Portfolio management.
- High-frequency or exchange-grade trading workflows.
- Full real-time market data unless legally licensed and available.
- Silver, platinum, palladium, or other commodities.
- Visible support for cities other than Chennai.
- Tamil, Tanglish, or other language support.
- WhatsApp or Telegram delivery.
- Native mobile applications.
- A public view of hidden chain-of-thought or private model reasoning.
- Unlicensed redistribution of protected financial-market data.
- Automatic escalation to a larger or more expensive non-mini model in the MVP.

---

## 6. Confirmed Product Decisions

| Area | Confirmed decision |
|---|---|
| Geographic scope | Chennai-first, multi-city-ready architecture |
| Market coverage | Chennai 22K and 24K, international spot gold, USD/INR, MCX gold futures |
| Primary users | General users, jewellery buyers, and market learners |
| Analysis modes | Simple Analysis and Detailed Market Analysis |
| Guidance | Cautious, conditional decision support; no guaranteed trading instructions |
| Language | English only for UI, responses, notifications, and reports |
| Historical data | Three years initially |
| Source strategy | Source hierarchy by data type with primary and fallback providers |
| Timeliness | Near-real-time where legally and technically available; delayed/EOD fallback |
| Refresh policy | Source-specific configurable schedules |
| Provider strategy | Public/low-cost initially; licensed-provider-ready |
| Registered capacity | Up to 1,000 users |
| Expected DAU | 50–150 initially |
| Concurrency | At least 25 general users; 2–3 concurrent AI analyses |
| Standard AI quota | Five newly generated detailed analyses per registered user per day |
| Runtime LLM | OpenAI `gpt-5.4-mini` for all agent nodes |
| LLM API | OpenAI Responses API |
| Orchestration | LangGraph |
| Authentication | Public basic rates; login required for AI and personalised functions |
| Roles | Guest, Registered User, Analyst, Administrator |
| Alerts | In-app and email |
| Reports | Dashboard and optional email delivery |
| Downloads | PDF reports and CSV historical data |
| Trace view | Admin and authorised demo users only |
| Cost dashboard | Admin dashboard and simplified user quota view |
| Budget | Target maximum INR 8,000/month for active public demo |
| CI/CD | GitHub Actions |
| Development agent | Claude Code CLI and supported IDE integration with reviewed root `CLAUDE.md` instructions and pinned Addy Osmani plugin |
| Documentation | Markdown as canonical source |

---

## 7. Target Users and Personas

### 7.1 Jewellery Buyer

**Objective:** Understand whether the current price is relatively favourable for a planned jewellery purchase.

**Needs:** Current rates, comparisons, simple explanations, awareness of making charges and taxes, and cautious staged-purchase guidance rather than trading advice.

### 7.2 Market Learner

**Objective:** Understand how international prices, currency movements, MCX, macroeconomic events, and news influence Chennai gold rates.

**Needs:** Detailed analysis, historical charts, ranked drivers, educational explanations, source links, and timestamps.

### 7.3 Analyst User

**Objective:** Explore deeper historical and market relationships within the permitted product scope.

**Needs:** Higher quota, detailed tables, CSV exports, advanced filters, and data-quality information.

### 7.4 Administrator

**Objective:** Operate, monitor, test, and control the system.

**Needs:** User and role management, provider configuration, prompt/model controls, agent traces, token/cost dashboards, data-quality alerts, audit logs, and feature flags.

---

## 8. User Roles and Permissions

| Capability | Guest | Registered User | Analyst | Administrator |
|---|---:|---:|---:|---:|
| View current Chennai rates | Yes | Yes | Yes | Yes |
| View basic daily comparison | Yes | Yes | Yes | Yes |
| Run detailed OpenAI analysis | No | Up to 5/day | Configurable higher quota | Configurable internal quota |
| View three-year history | Limited preview | Yes | Yes | Yes |
| Save preferences | No | Yes | Yes | Yes |
| Configure alerts | No | Yes | Yes | Yes |
| Receive email reports | No | Yes | Yes | Yes |
| Download PDF report | No | Yes | Yes | Yes |
| Download CSV data | No | Limited | Yes | Yes |
| View safe agent trace | No | No | Optional authorised access | Yes |
| View cost dashboard | No | Quota only | Quota only | Full |
| Manage providers/prompts/users | No | No | No | Yes |

---

## 9. Functional Scope

### 9.1 Current Gold Rate

Display Chennai 22K and 24K prices per gram, derived 8 g and 10 g values, source, market and retrieval timestamps, freshness, fallback status, observation type, and a notice that GST, making charges, and jeweller-specific charges may be additional.

### 9.2 Daily Comparison

Calculate today-versus-yesterday absolute and percentage change, direction, purity-specific comparisons, and 1-day, 7-day, 30-day, 90-day, 1-year, and custom-range comparisons. All calculations are deterministic.

### 9.3 Historical Data and Charts

Maintain three years of Chennai 22K/24K rates, international spot gold, USD/INR, and MCX gold futures where legally permitted. Charts support range selection, daily/weekly aggregation, overlays, missing-data indicators, source metadata, and authorised CSV export.

### 9.4 Simple Analysis

Provide a movement summary, top one to three likely drivers, plain-English explanation, confidence category, important uncertainty, cautious guidance, source citations, and update times. Reuse a validated cached market-state report whenever possible.

### 9.5 Detailed Market Analysis

Provide local movement, international gold, USD/INR, MCX, relevant events, ranked factors, counter-factors, update-timing effects, provider discrepancies, short-term interpretation, evidence strength, and clear separation of fact, inference, and opinion.

### 9.6 News and Macro Intelligence

Collect permitted news and official announcements; deduplicate related stories; extract entities, events, and timestamps; verify event timing; classify potential impact; prefer primary sources; and mark opinion separately from confirmed facts.

### 9.7 Decision-Support Guidance

Conditional statements are allowed, such as staged purchasing for a planned jewellery need or explaining that making charges may outweigh a small daily price difference. The product must not guarantee direction, issue personalised buy/sell instructions, or recommend leverage or speculative derivatives.

### 9.8 Alerts

Support price thresholds, daily percentage movement, material movement, and daily-report-ready alerts through in-app and email channels.

### 9.9 Daily Reports

Generate a daily Chennai report containing 22K/24K rates, comparisons, weekly/monthly context, market drivers, source/freshness information, confidence, uncertainty, and cautious guidance. Reports are available in-app, optionally emailed, and downloadable as PDF.

### 9.10 AI Chat and Query Experience

Registered users may ask supported market questions. The system classifies each request and invokes only required agents and typed tools. Normal rate viewing never calls the LLM.

### 9.11 Safe Agent Trace View

Display trace ID, intent, agents/tools, providers, timings, retry/fallback events, OpenAI model ID, reasoning-effort policy, token usage, estimated cost, validation status, and structured reason codes. Never expose hidden chain-of-thought, credentials, auth tokens, or sensitive unredacted content.

### 9.12 Usage and Cost Dashboard

Administrator view includes requests, OpenAI calls by model/task, input/output/cached tokens, estimated cost, cache savings, quotas, budget alerts, and anomalies. Registered users see daily quota, used/remaining analyses, reset time, and recent history.

---

## 10. Data Requirements

### 10.1 Data source hierarchy

Maintain a separate source hierarchy for Chennai retail rates, Indian benchmark, MCX, international spot gold, USD/INR, economic events, and news. Exact vendors require legal and technical approval.

### 10.2 Data timeliness

- International spot gold: every 5–10 minutes.
- USD/INR and MCX: every 5–15 minutes.
- Chennai retail rates: every 15–30 minutes.
- News: every 10–15 minutes.
- Official announcements: every 30–60 minutes, with event-aware checks.
- Aggregates: hourly and end-of-day.

Schedules are configurable. Unchanged values should not create unnecessary database writes.

### 10.3 Data quality

Track missing and duplicate records, unit/timestamp consistency, provider discrepancies, suspicious jumps, stale data, fallback usage, estimated values, and data-quality score.

---

## 11. AI and Agent Requirements

### 11.1 Model strategy

- **Single runtime model family:** OpenAI `gpt-5.4-mini`.
- **Routing/extraction policy:** low reasoning effort, small output budget, strict JSON schema.
- **Evidence synthesis policy:** medium reasoning effort, bounded output, citation coverage required.
- **Validation/critic policy:** medium reasoning effort with deterministic checks executed first.
- **Complex-case policy:** the same mini model may use a higher configured reasoning effort when supported and within budget; it must not silently switch to a larger model.
- **API:** OpenAI Responses API through the official OpenAI SDK and `langchain-openai` integration.
- **Configuration:** model IDs, reasoning effort, timeout, token limits, and prompt versions are environment/configuration values, not hardcoded business logic.

### 11.2 Agent responsibilities

1. Supervisor and intent routing.
2. Market-data retrieval.
3. Historical analytics.
4. News and macro research.
5. India/Chennai pricing context.
6. Evidence synthesis.
7. Validation and critic checks.
8. Response composition.

Agents are logical LangGraph nodes in a modular monolith, not separate microservices by default.

### 11.3 Evidence workflow

The system establishes numerical movement first, generates plausible hypotheses, checks each against data and event timing, ranks supporting factors, identifies contradictory evidence, distinguishes fact from inference, calculates confidence, and rejects unsupported causal claims.

### 11.4 Structured outputs

Every model call that feeds business logic must return a versioned schema. Invalid output is rejected and may be repaired once. Prices and calculations from model text are never accepted as authoritative.

### 11.5 Failure behaviour

OpenAI timeout, rate limit, malformed output, or outage must not block validated rates or historical data. The product falls back to deterministic facts and a clearly labelled limited explanation.

---

## 12. RAG and Knowledge Requirements

Use pgvector for permitted news, official documents, methodology notes, and internal curated reference material. Retrieval must preserve URL/source, publication time, event time, document type, and licence metadata. Retrieved text is untrusted input and cannot override system instructions or tool permissions.

---

## 13. Non-Functional Requirements

- P95 public rate API latency target: under 500 ms from cache and under 1.5 seconds from database under expected load.
- At least 25 concurrent normal users without degradation of core rate endpoints.
- Two to three concurrent AI analyses, with additional requests queued.
- Availability of deterministic rate/history features must not depend on OpenAI availability.
- Accessibility target: WCAG 2.2 AA.
- All sensitive data encrypted in transit and at rest through managed platform controls.
- No API key, token, prompt secret, or hidden reasoning in logs.
- Full trace correlation across API, task, tool, model, provider, database, and report generation.

---

## 14. Cost and Quota Controls

- Five newly generated detailed analyses per registered user per IST day.
- Cached equivalent reports do not consume a new-analysis quota.
- Valkey/PostgreSQL atomic reservation prevents race conditions.
- Per-user and global rate limits apply.
- Budget circuit breakers can suspend new AI generation while keeping market facts available.
- Prompt and response size limits apply per task.
- OpenAI token and cost usage is recorded per run.

---

## 15. Security and Safety Requirements

- Authentication and RBAC for protected features.
- Row Level Security for user-owned data.
- Tool allowlists and typed arguments.
- Prompt-injection resistance for retrieved content.
- Output validation for unsupported claims, prohibited advice, and missing citations.
- No hidden chain-of-thought storage or display.
- Audit logs for model/prompt releases, provider changes, role changes, and budget overrides.

---

## 16. Observability and Evaluation

Capture graph nodes, tool calls, OpenAI Responses API calls, model ID, reasoning effort, prompt version, token usage, cost, latency, structured output, validation results, and user feedback. Maintain golden datasets for arithmetic correctness, citation coverage, timeline consistency, safe guidance, stale-data behaviour, and prompt-injection resistance.

---

## 17. Acceptance Criteria Highlights

- Basic rate and history features work during an OpenAI outage.
- Every important price displays source, timestamp, and freshness.
- Detailed analysis contains no unsupported prices or calculations.
- Causal claims include evidence and timeline alignment.
- Duplicate requests reuse an existing queued/completed report.
- Only one of two simultaneous requests is accepted when one quota unit remains.
- Validation failure triggers at most one controlled repair before degraded output.
- Queue saturation never blocks public rate and history endpoints.
- Admin trace displays model/tool metadata without hidden reasoning or secrets.

---

## 18. Delivery Phases

### Phase 0 — Specification and source approval

Approve controlled documents, providers, ADRs, test strategy, and golden datasets.

### Phase 1 — Data foundation

Create schema, migrations, provider contracts/adapters, historical backfill, quality rules, and current-rate API.

### Phase 2 — Core application

Implement authentication, RBAC, dashboard, historical charts, caching, and basic alerts.

### Phase 3 — Agent workflow

Implement LangGraph, OpenAI Responses API integration, task-specific `gpt-5.4-mini` policies, historical/news agents, validation, and simple/detailed analysis.

### Phase 4 — Reporting and observability

Implement reports, exports, LangSmith tracing/evaluation, Grafana dashboards, safe trace UI, and token/cost dashboard.

### Phase 5 — Production hardening

Complete load, security, resilience, backup/recovery, and public-demo deployment.

---

## 19. Dependencies and Open Decisions

1. Exact primary/fallback Chennai retail-rate providers.
2. Legal usage and redistribution rights.
3. MCX data source and delay/licensing status.
4. International spot-gold source.
5. USD/INR source.
6. News provider and usage rights.
7. Email provider.
8. Backend hosting provider and region.
9. Retention/privacy policy wording.
10. Terms of use and financial disclaimer review.
11. Final OpenAI organisation/project configuration and approved API spend limit.
12. Whether OpenAI prompt caching/batch features are beneficial for specific offline workloads.

---

## 20. Definition of MVP Completion

The MVP is complete when all must-have stories pass; current Chennai rates and three-year history are available; sources and freshness are visible; Simple and Detailed Analysis pass evaluation thresholds; OpenAI quotas, caching, and cost dashboards work; alerts/reports/exports work; RBAC passes; LangSmith and Grafana are active; quality gates pass; projected monthly cost remains within budget; and documentation/runbooks are complete.

---

## Appendix A — Environment Configuration

```text
OPENAI_API_KEY=...
OPENAI_PROJECT_ID=...
OPENAI_MODEL_ROUTER=gpt-5.4-mini
OPENAI_MODEL_SYNTHESIS=gpt-5.4-mini
OPENAI_MODEL_VALIDATOR=gpt-5.4-mini
OPENAI_REASONING_ROUTER=low
OPENAI_REASONING_SYNTHESIS=medium
OPENAI_REASONING_VALIDATOR=medium
OPENAI_MAX_OUTPUT_ROUTER=800
OPENAI_MAX_OUTPUT_SYNTHESIS=4000
OPENAI_MAX_OUTPUT_VALIDATOR=2000
OPENAI_TIMEOUT_SECONDS=45
```

Exact supported parameter names must be confirmed against the installed OpenAI SDK version and pinned in configuration tests.

---

## Appendix B — Model Migration Decision

| Previous decision | Revised decision |
|---|---|
| Claude Sonnet primary | OpenAI `gpt-5.4-mini` with medium reasoning |
| Claude Haiku lightweight | OpenAI `gpt-5.4-mini` with low reasoning |
| Claude Opus escalation | Removed from MVP; same mini model with bounded policy only |
| Anthropic API | OpenAI Responses API |
| Claude-specific LangChain integration | `langchain-openai` and official OpenAI SDK |
| Development environment | Claude Code CLI and supported IDE integration |
| Claude outage wording | OpenAI/LLM outage wording |

## Approved UX and Flow Amendments Incorporated in This Baseline

The following decisions from `Gold_Market_AI_Agent_UI_UX_Recommendations.md` and `Gold_Market_AI_Agent_Application_Flow.md` are now normative product requirements:

1. Current rates, source, market time, retrieval time, freshness, and fallback status render before AI narrative.
2. Verified facts, deterministic calculations, model-supported inference, uncertainty, and guidance use visibly distinct presentation treatments.
3. Normal consumer surfaces use provider-neutral wording; exact OpenAI model and policy metadata is limited to methodology, safe traces, and administrator controls.
4. Detailed analysis is an asynchronous, resumable job with visible safe workflow stages and status polling or server-sent events.
5. Quota is atomically reserved at request acceptance, finalised according to billable-work policy, and released for eligible pre-model failures.
6. Equivalent requests are deduplicated by a market-state and request fingerprint; validated reusable reports do not consume a new detailed-analysis unit.
7. OpenAI or provider failure must preserve current rates, history, deterministic comparisons, and clearly labelled limited output.
8. P0 journeys target WCAG 2.2 AA and functional layouts down to 360 px without unintended page-level horizontal scrolling.
9. Safe traces expose operational metadata but never hidden reasoning, credentials, secrets, or unredacted sensitive content.
10. Administrator model-policy changes require versioning, evaluation, approval, rollout metadata, monitoring, and rollback.

## Controlled Implementation Specifications

The controlled implementation set is intentionally limited to these seven documents:

- `Gold_Market_AI_Agent_PRD.md`
- `Gold_Market_AI_Agent_TRD.md`
- `Gold_Market_AI_Agent_UI_UX_Recommendations.md`
- `Gold_Market_AI_Agent_Application_Flow.md`
- `Gold_Market_AI_Agent_Backend_Database_Schema.md`
- `Gold_Market_AI_Agent_API_Event_Provider_Contracts.md`
- `Gold_Market_AI_Agent_Detailed_Implementation_Plan.md`

The implementation workflow authority is Addy Osmani's pinned `addyosmani/agent-skills` repository. The detailed implementation plan contains the project-specific skill routing; no separate generic skill map overrides it.

A conflict is resolved in this order: approved ADR, PRD product intent, TRD architecture, contract/schema specifications, UI/UX and application flow, then the detailed implementation plan. Any unresolved conflict blocks implementation until documented through the applicable `agent-skills` workflow.
