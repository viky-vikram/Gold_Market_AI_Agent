# AurumIQ — Claude Code Implementation Kickstart

**Purpose:** Start and continue the AurumIQ implementation using Claude Code and Addy Osmani's `agent-skills` workflow.

**Runtime AI architecture:** AurumIQ runtime agents use OpenAI `gpt-5.4-mini`.  
**Development assistant:** Claude Code.  
**Engineering workflow:** Addy Osmani's `addyosmani/agent-skills`.

---

## 1. One-Time Setup Before Using the Prompt

Run Claude Code from the repository root:

```bash
cd <PATH_TO_AURUMIQ_REPOSITORY>
claude --permission-mode plan
```

Inside Claude Code, install and verify the plugin:

```text
/plugin marketplace add addyosmani/agent-skills
/plugin install agent-skills@addy-agent-skills
/reload-plugins
/plugin
/help
```

The seven controlled documents must be available in the repository, preferably under:

```text
docs/controlled/
├── Gold_Market_AI_Agent_PRD.md
├── Gold_Market_AI_Agent_TRD.md
├── Gold_Market_AI_Agent_UI_UX_Recommendations.md
├── Gold_Market_AI_Agent_Application_Flow.md
├── Gold_Market_AI_Agent_Backend_Database_Schema.md
├── Gold_Market_AI_Agent_API_Event_Provider_Contracts.md
└── Gold_Market_AI_Agent_Detailed_Implementation_Plan.md
```

Do not add real secrets. Use `.env.example` and local placeholder values only.

---

## 2. First-Session Kickstart Prompt

Copy the complete prompt below into Claude Code while it is in **Plan mode**.

```text
You are the implementation lead for the AurumIQ Gold Market AI Agent.

This is the first controlled implementation session. Work from the repository root and follow the seven controlled Markdown documents listed below. Do not begin by writing code.

CONTROLLED DOCUMENTS

1. docs/controlled/Gold_Market_AI_Agent_PRD.md
2. docs/controlled/Gold_Market_AI_Agent_TRD.md
3. docs/controlled/Gold_Market_AI_Agent_UI_UX_Recommendations.md
4. docs/controlled/Gold_Market_AI_Agent_Application_Flow.md
5. docs/controlled/Gold_Market_AI_Agent_Backend_Database_Schema.md
6. docs/controlled/Gold_Market_AI_Agent_API_Event_Provider_Contracts.md
7. docs/controlled/Gold_Market_AI_Agent_Detailed_Implementation_Plan.md

If these files are stored elsewhere, locate them by exact filename and report their resolved paths before proceeding.

AUTHORITATIVE PRECEDENCE

Apply this precedence when interpreting the documents:

1. PRD controls product scope, users, business requirements, quotas, and acceptance outcomes.
2. TRD controls architecture, technology, security, reliability, deployment, and non-functional requirements.
3. Backend Database Schema controls persistence, migrations, constraints, indexes, partitions, RLS, audit, and data ownership.
4. API, Event and Provider Contracts controls REST contracts, event envelopes, provider interfaces, errors, idempotency, and compatibility.
5. Application Flow controls success, failure, fallback, recovery, quota, and administrative flows.
6. UI/UX Recommendations controls interface behaviour, accessibility, responsive states, trust indicators, and presentation.
7. Detailed Implementation Plan controls implementation order, sprint gates, required skills, test evidence, and exit criteria.

Do not silently resolve a genuine contradiction. Report the contradiction with document names and sections, propose the smallest safe resolution, and stop for human approval.

MANDATORY AGENT-SKILLS WORKFLOW

The phrase agent-skills means only Addy Osmani's installed `addyosmani/agent-skills` plugin.

Before analysing or implementing the task:

1. Verify that the `agent-skills@addy-agent-skills` plugin is installed and enabled.
2. Verify that namespaced commands are visible.
3. Invoke `/agent-skills:using-agent-skills`.
4. Follow the actual installed skill instructions, not a generic summary.
5. Invoke all task-specific skills required by the implementation plan.
6. Do not skip a skill because the work appears simple.
7. If a command is unavailable, stop and report the exact missing command rather than substituting an unrelated built-in skill.

GLOBAL RULES

- The seven controlled documents are read-only unless I explicitly approve a controlled-document change.
- Claude Code is the development assistant. Do not replace the runtime OpenAI `gpt-5.4-mini` architecture with Claude models.
- Do not integrate live providers, use paid APIs, or make real OpenAI calls during Sprint 0.
- Never commit `.env`, tokens, credentials, personal data, generated secrets, or provider payloads containing restricted data.
- Never weaken or bypass a failing test, lint rule, migration check, security gate, or skill checkpoint.
- Use decimal types for financial values and timezone-aware UTC timestamps.
- Preserve provider independence and deterministic calculation boundaries.
- Use small, reviewable increments.
- Do not execute all sixteen sprints in one session.
- Work on only the next approved task.
- Do not use bypass-permissions mode.
- Do not modify `main` directly.
- Do not create a pull request or push remotely unless I explicitly ask.

INITIAL SCOPE

Begin with Phase 0, Sprint 0 from the Detailed Implementation Plan.

The first work item is:

GMAA-001 — Governance and repository scaffold.

Do not start Sprint 1 or later work.

CONTEXT-LOADING METHOD

Use context economically:

1. Read the implementation plan's objective, agent-skills mandate, delivery governance, Phase 0, Sprint 0, definition of done, and initial ticket order.
2. Read only the relevant sections of the other six controlled documents needed for GMAA-001.
3. Inspect the current repository tree, Git status, existing configuration, package manifests, lock files, CI files, and documentation.
4. Do not load unrelated sections into working context unless needed to resolve a dependency.
5. Before editing an existing file, read it and identify its role.
6. Locate an existing project pattern before introducing a new pattern, when one exists.

FIRST RESPONSE — PLAN ONLY

Remain in Plan mode. Do not create, edit, delete, rename, install, commit, or push anything yet.

Return:

1. Environment verification
   - repository root
   - current branch
   - Git working-tree state
   - Claude Code version
   - installed agent-skills plugin status
   - exact namespaced commands verified

2. Controlled-document verification
   - resolved path for each of the seven documents
   - document version/status
   - missing or conflicting documents
   - sections loaded for GMAA-001

3. Skill routing
   - exact skills invoked
   - why each skill applies
   - checkpoints required by each skill

4. GMAA-001 interpretation
   - objective
   - prerequisites
   - in-scope deliverables
   - explicitly out-of-scope work
   - acceptance criteria
   - exit criteria

5. Proposed implementation plan
   - ordered, atomic tasks
   - files and directories expected to be created or changed
   - setup/build/lint/type-check/test/security commands
   - CI jobs
   - rollback strategy
   - evidence to capture
   - risks and decisions requiring approval

6. Proposed branch name and commit boundaries

7. A final approval gate:
   "Approve GMAA-001 plan, request changes, or stop."

Do not implement until I approve the plan.

AFTER I APPROVE

After approval, perform only GMAA-001 using the mandatory skills.

Use this lifecycle:

1. `/agent-skills:using-agent-skills`
2. `/agent-skills:spec-driven-development`
3. `/agent-skills:planning-and-task-breakdown`
4. `/agent-skills:git-workflow-and-versioning`
5. `/agent-skills:incremental-implementation`
6. `/agent-skills:test-driven-development`
7. `/agent-skills:ci-cd-and-automation`
8. `/agent-skills:documentation-and-adrs`
9. `/agent-skills:code-review-and-quality`

Also invoke `/agent-skills:debugging-and-error-recovery` immediately if any command, test, build, migration, or integration fails. Add other installed skills when their trigger conditions apply.

Implementation requirements:

- Create a short-lived branch for GMAA-001.
- Establish the approved monorepo skeleton from the TRD.
- Create a concise root `CLAUDE.md` that points to the seven controlled documents, records precedence, lists approved commands, protects controlled documents, and requires namespaced agent-skills.
- Create `agent-skills.lock` with the installed plugin version or commit SHA and verification date.
- Create `.env.example` without real credentials.
- Add contribution, pull-request evidence, ADR, threat-model, and runbook templates required by the implementation plan.
- Establish deterministic setup, format, lint, type-check, test, security, and documentation-validation commands.
- Establish local service definitions and empty/smoke checks only to the extent required by Sprint 0.
- Create CI workflow skeletons required by Sprint 0.
- Establish requirement-to-test traceability from the seven controlled documents.
- Add tests before or alongside implementation as required by the TDD skill.
- Make small commits aligned to the approved commit boundaries.
- Do not push or open a pull request unless instructed.

At the end of GMAA-001, return:

1. Summary of completed work.
2. Files created, modified, and deleted.
3. Skills invoked and checkpoints completed.
4. Commands run with pass/fail results.
5. Test and security evidence.
6. `git status` and commit list.
7. Deviations from the approved plan.
8. Remaining risks or manual actions.
9. GMAA-001 exit-criteria checklist.
10. Recommendation to accept, remediate, or reject the work.
11. The next task identifier, but do not start it.
```

---

## 3. Approval Reply After Claude Produces the Plan

Review Claude's proposed plan. When it is correct, reply:

```text
Approve the GMAA-001 plan.

Exit Plan mode and implement only GMAA-001 according to the approved plan and the mandatory Addy Osmani agent-skills lifecycle.

Pause immediately if:
- a controlled-document contradiction is discovered;
- a required skill or command is unavailable;
- a destructive or irreversible operation is required;
- a secret, paid account, external provider, or production environment is required;
- a test or security gate cannot be satisfied without changing the approved scope.

Do not begin GMAA-002 or any later work.
```

---

## 4. Continuation Prompt for Later Sessions

Use this prompt when opening a new Claude Code session after one or more tasks are complete.

```text
Continue the AurumIQ implementation from the repository's current verified state.

Before making changes:

1. Read the root `CLAUDE.md`.
2. Verify the installed `agent-skills@addy-agent-skills` plugin and `agent-skills.lock`.
3. Invoke `/agent-skills:using-agent-skills`.
4. Read the seven controlled documents only to the depth required for the next incomplete approved task.
5. Inspect Git status, recent commits, task evidence, test results, and unfinished work.
6. Identify the next incomplete task from the Detailed Implementation Plan.
7. Verify that every prerequisite and previous sprint exit criterion is satisfied.
8. Enter or remain in Plan mode and propose a plan for that one task only.

Do not assume the previous session completed successfully. Verify using repository evidence and commands.

Do not modify controlled documents, start a later task, push, open a pull request, access production, use real secrets, or enable paid providers without explicit approval.

Return:

- verified current state;
- previous task closure evidence;
- next task and prerequisites;
- required namespaced agent-skills;
- atomic implementation plan;
- tests and verification commands;
- risks and approval questions;
- final approval gate.

Do not implement until I approve.
```

---

## 5. Recommended Day-to-Day Command Sequence

Use one implementation task at a time:

```text
/agent-skills:using-agent-skills
/agent-skills:spec
/agent-skills:plan
```

Review and approve the plan, then:

```text
/agent-skills:build
/agent-skills:test
/agent-skills:review
/agent-skills:code-simplify
```

At a release boundary:

```text
/agent-skills:ship
```

Use `/agent-skills:build auto` only inside a small, already-approved task plan. Do not use it to execute the entire AurumIQ roadmap in one pass.

---

## 6. Expected Workflow Artifacts

The skill workflow may create or maintain:

```text
CLAUDE.md
agent-skills.lock
SPEC.md
tasks/plan.md
tasks/todo.md
docs/adr/
docs/runbooks/
docs/threat-models/
evidence/<TASK_ID>/
```

Keep `SPEC.md`, `tasks/plan.md`, and `tasks/todo.md` under version control while work is active unless the repository policy explicitly states otherwise.

Each task evidence record should include:

```text
Task ID:
Agent-Skills source:
Installed plugin version or commit SHA:
Skills invoked:
Skill checkpoints completed:
Controlled-document sections used:
Commands run:
Test results:
Security results:
Performance/observability impact:
Files changed:
Commits:
Deviations:
Unresolved risks:
Reviewer decision:
```

---

## 7. Human Control Points

Human approval is required before:

- leaving the first Plan-mode review for each task;
- changing any controlled document;
- resolving a material cross-document conflict;
- adding a dependency not already approved;
- applying a database migration outside local test environments;
- enabling a live provider or paid service;
- using real API credentials;
- changing security or RLS boundaries;
- performing destructive operations;
- pushing, creating a pull request, merging, deploying, or releasing.
