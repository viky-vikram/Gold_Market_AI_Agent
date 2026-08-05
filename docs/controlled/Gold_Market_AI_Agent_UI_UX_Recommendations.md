# AurumIQ — UI/UX Recommendation

**Document ID:** GMAA-UX-001  
**Version:** 1.2 Claude Code + Agent-Skills Enforced  
**Date:** 2026-08-05  
**Status:** Approved for implementation  
**Canonical format:** Markdown  
**Related documents:** `Gold_Market_AI_Agent_PRD.md`, `Gold_Market_AI_Agent_TRD.md`  
**Supersedes:** Version 1.1 Agent-Skills Enforced dated 2026-08-05  

---

## Revision Summary

This revision retains the approved facts-first, evidence-based, accessible UI, selects Claude Code as the implementation environment, and keeps Addy Osmani's `addyosmani/agent-skills` workflow mandatory. UI changes must use the exact frontend, browser-testing, test-driven, performance, security, debugging, Git, and review skills routed through `/agent-skills:using-agent-skills`. Users still do not need to know the model vendor during normal use; model/provider details remain available in methodology, safe traces, and administrator configuration.

## Approval Record

| Item | Decision | Approved baseline |
|---|---|---|
| UI/UX recommendations | Approved for implementation | Facts-first layout, progressive disclosure, safe trace, quota UX, degraded states, WCAG 2.2 AA, responsive P0 journeys |
| Application flow | Approved for implementation | Deterministic-first processing, asynchronous detailed analysis, deduplication, quota reservation, bounded repair, fallback, trace propagation |
| Runtime model | Approved | OpenAI `gpt-5.4-mini` through the Responses API for every runtime agent node |
| Development workflow | Approved | Claude Code with Addy Osmani `addyosmani/agent-skills`; UI implementation must follow the actual frontend, browser, test, performance, security, and review skills |

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

### UI/UX skill routing

| UI/UX activity | Mandatory Addy Osmani skills |
|---|---|
| Page, component, responsive layout, state, or interaction implementation | `/agent-skills:frontend-ui-engineering`, `/agent-skills:incremental-implementation`, `/agent-skills:test-driven-development` |
| Live browser validation, DOM/network/console investigation, or P0 journey verification | `/agent-skills:browser-testing-with-devtools` |
| Accessibility and Core Web Vitals work | `/agent-skills:frontend-ui-engineering`, `/agent-skills:performance-optimization`; use the installed accessibility/performance references |
| Login, admin, quota, safe-trace, sensitive data, or external-content UI | `/agent-skills:security-and-hardening` |
| UI failure or unexplained behaviour | `/agent-skills:debugging-and-error-recovery` |
| Merge readiness | `/agent-skills:code-review-and-quality` |

Screenshots or visual inspection alone are not acceptance evidence. UI work must include automated tests and runtime browser evidence required by the selected skill workflows.

---

## 1. Purpose

Define the recommended information architecture, visual direction, interaction patterns, page inventory, accessibility requirements, and UX acceptance criteria for AurumIQ.

---

## 2. Product Experience Goal

Help users answer:

1. What is the latest available Chennai gold rate?
2. How did it change?
3. How fresh and trustworthy is the data?
4. What factors most likely caused the movement?
5. What cautious action may be reasonable for a jewellery-purchase objective?

The interface separates market facts from AI interpretation. An AI-generated inference is never styled as a verified fact.

---

## 3. UX Principles

- Trust before decoration.
- Facts before AI commentary.
- Progressive disclosure for advanced evidence and trace metadata.
- Credible financial-information design rather than a generic chatbot aesthetic.
- Cautious decision support instead of BUY/SELL command language.
- Visible uncertainty and data-quality limitations.
- WCAG 2.2 AA target.
- Provider-neutral normal-user language; model details only where operationally useful.

---

## 4. Personas

Guest, Registered User/Jewellery Buyer, Market Learner, Analyst, and Administrator remain the primary personas.

---

## 5. Information Architecture

```text
Public
├── Home / Current Rate
├── Rate History Preview
├── Methodology and Sources
├── Login
└── Register

Authenticated User
├── Dashboard
├── Market Rates
├── AI Analysis
│   ├── Simple Analysis
│   ├── Detailed Analysis
│   └── Analysis History
├── News and Market Drivers
├── Alerts
├── Reports
├── Usage and Quota
└── Profile and Preferences

Administrator
├── Operations Overview
├── Data Providers
├── Data Quality
├── Agent Traces
├── AI Quality and Evaluations
├── Tokens and Costs
├── Users and Roles
├── Prompts and Model Configuration
├── Feature Flags
└── Audit Logs
```

---

## 6. Dashboard

Show 22K/24K rate cards, daily movement, freshness, 30-day trend, key drivers, Simple Analysis, cautious guidance, global/FX/MCX context, events, alerts, latest report, and remaining analysis quota.

Rate cards must show source, market time, retrieval time, fallback status, and observation type.

---

## 7. AI Analysis Experience

### 7.1 Modes

**Simple Analysis:** concise summary, daily change, top drivers, counter-factor, confidence, cautious guidance, sources, and timestamps.

**Detailed Analysis:** deterministic calculations, international gold, USD/INR, MCX, news/macro events, ranked drivers, counter-analysis, source disagreement, limitations, confidence rationale, and cautious guidance.

### 7.2 Request form

Inputs include analysis mode, purity, unit, comparison period, purchase objective, and optional question. Do not request income, portfolio, or risk profile in the MVP.

### 7.3 Processing stages

```text
1. Validating market data
2. Comparing historical rates
3. Reviewing market drivers
4. Validating evidence and calculations
5. Preparing the report
```

These are safe workflow stages, not hidden reasoning.

### 7.4 Result anatomy

1. Market conclusion.
2. Deterministic comparison.
3. Primary drivers.
4. Counter-factors and uncertainty.
5. Cautious guidance.
6. Sources and freshness.
7. Methodology and disclaimer.

### 7.5 Model wording

Normal users see labels such as “AI analysis” and “validated analysis,” not vendor branding. Methodology may state that AurumIQ currently uses OpenAI `gpt-5.4-mini`. Administrators see the exact model, reasoning policy, prompt version, tokens, cost, retries, and validation result.

---

## 8. Usage and Quota

- Basic rate checks do not call OpenAI and consume no AI quota.
- Reused validated Simple Analysis consumes no new detailed-analysis quota.
- A newly generated Detailed Analysis consumes one unit.
- Show used, reserved, remaining, and IST reset time.
- Avoid pressure or dark patterns when quota is exhausted.

---

## 9. Safe Agent Trace

Display trace ID, request type, nodes/tools, providers, start/end time, retries, fallback usage, OpenAI model ID, reasoning-effort policy, prompt/schema versions, token usage, estimated cost, validation score, and rule failures.

Never display hidden chain-of-thought, API keys, auth headers, secrets, or unredacted sensitive content.

---

## 10. Administrator UX

### 10.1 Operations overview

Show API/provider health, last ingestion, freshness, queue depth, OpenAI API failure/rate-limit/timeout rate, validation pass rate, daily cost, and budget utilisation.

### 10.2 Prompt and model configuration

Use versioned, reviewed configuration:

- active model by task;
- reasoning effort;
- output limit;
- timeout/retry policy;
- prompt and schema version;
- rollout status;
- rollback version;
- effective date.

Production prompt/model edits require evaluation and approval.

---

## 11. Degraded States

### OpenAI unavailable

Preserve deterministic facts and show: current rate, comparison, calculations, evidence list when available, a notice that narrative analysis is unavailable, and an appropriate retry/status action. Public facts must continue working.

### Provider conflict or stale data

Show selected source, competing range, freshness state, and limitations. Disable wording that implies a current causal conclusion when required data is stale.

### Quota reached

Show reset time, cached report access, and basic facts that remain available.

---

## 12. Accessibility and Responsive Behaviour

Maintain keyboard operation, visible focus, semantic structure, chart text/table alternatives, sufficient contrast, reduced-motion support, 200% zoom, accessible live regions for job completion, and functional mobile layouts down to 360 px.

---

## 13. UX Acceptance Criteria

1. Users can identify 22K/24K rates, movement, source, time, and freshness immediately.
2. Facts and AI inference are visually separated.
3. Delayed, stale, fallback, conflicting, estimated, and unavailable states are explained.
4. Detailed-analysis progress is visible and resumable.
5. Supporting sources and timestamps are inspectable.
6. P0 journeys meet WCAG 2.2 AA targets.
7. Mobile P0 journeys avoid unintended horizontal page scrolling.
8. Quota behaviour is understandable.
9. No guaranteed or personalised trading instruction is presented.
10. Safe trace excludes hidden reasoning and secrets.
11. OpenAI outage leaves current rates and history usable.
12. Model branding does not dominate the consumer experience.

---

## 14. Model-Migration UI Changes

| Previous UI wording | Revised wording |
|---|---|
| Claude analysis | AI analysis / OpenAI-powered analysis in methodology only |
| Claude unavailable | AI analysis temporarily unavailable |
| Claude calls by model | OpenAI calls by model/task |
| Claude failure rate | OpenAI API failure rate |
| Newly generated Claude analysis | Newly generated Detailed Analysis |
| Claude model selector | OpenAI model policy selector |

---

## 15. Approval Gate

Approve facts-versus-inference layout, analysis modes, quota messages, asynchronous status, degraded OpenAI behaviour, safe trace metadata, and administrator model-policy controls before implementation.

## 16. Approval Decision

The recommendation is approved in full for the MVP baseline. Implementation must preserve the facts-first hierarchy, explicit freshness and source metadata, provider-neutral consumer wording, asynchronous job feedback, accessible degraded states, safe trace boundaries, and administrator release controls.

Changes to information architecture, quota semantics, financial-guidance wording, accessibility target, or safe-trace disclosure require a documented UX decision and corresponding PRD/TRD update.
