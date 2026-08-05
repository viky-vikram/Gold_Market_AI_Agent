# AurumIQ — Claude Code Project Instructions

AurumIQ is a Chennai-first Gold Market AI Agent. This file is the entry contract for Claude Code
sessions and human contributors. Keep it short — it points to authority, it does not restate it.

## Controlled documents

These seven documents under `docs/controlled/` are the specification. Read only the sections a task
actually needs.

| # | Document | Owns |
|---|---|---|
| 1 | `Gold_Market_AI_Agent_PRD.md` | Product scope, users, quotas, acceptance outcomes |
| 2 | `Gold_Market_AI_Agent_TRD.md` | Architecture, technology, security, reliability, NFRs |
| 3 | `Gold_Market_AI_Agent_Backend_Database_Schema.md` | Persistence, migrations, constraints, RLS, audit |
| 4 | `Gold_Market_AI_Agent_API_Event_Provider_Contracts.md` | REST, events, provider interfaces, idempotency |
| 5 | `Gold_Market_AI_Agent_Application_Flow.md` | Success, failure, fallback, recovery, quota flows |
| 6 | `Gold_Market_AI_Agent_UI_UX_Recommendations.md` | Interface behaviour, accessibility, trust indicators |
| 7 | `Gold_Market_AI_Agent_Detailed_Implementation_Plan.md` | Build order, sprint gates, test evidence, exit criteria |

**Precedence on conflict:** approved ADR → 1 → 2 → 3 → 4 → 5 → 6 → 7.

Do not silently resolve a genuine contradiction. Report it with document names and sections, propose
the smallest safe resolution, and stop for human approval.

## Protected files

`docs/controlled/**` is **read-only**. Changing any of it requires explicit human approval and a
controlled change record. A test enforces this — see `apps/api/tests/test_controlled_documents.py`.

Never commit `.env`, tokens, credentials, personal data, or provider payloads containing restricted
data. Use `.env.example` with placeholders.

## Engineering workflow

`agent-skills` means only the pinned `addyosmani/agent-skills` plugin — never a project-local summary,
and never a similarly named bundled skill. The installed commit is recorded in `agent-skills.lock`.

1. Begin every implementation, design, migration, test, review, or release task with
   `agent-skills:using-agent-skills` and let it route the work.
2. Follow the actual installed `SKILL.md` workflow. Do not implement directly when a skill applies.
3. `agent-skills:git-workflow-and-versioning` for every code change;
   `agent-skills:code-review-and-quality` before every merge.
4. `agent-skills:debugging-and-error-recovery` immediately when a command, test, build, migration, or
   integration fails. Never weaken or bypass a failing gate to continue.
5. Record skill evidence on the work item or PR — the template in
   `.github/PULL_REQUEST_TEMPLATE.md` is the required format.

## Approved commands

```bash
uv sync                      # install Python deps (apps/api)
uv run ruff format .         # format Python
uv run ruff check .          # lint Python
uv run mypy .                # type-check Python
uv run pytest                # test Python
pnpm install                 # install JS deps
pnpm lint                    # lint JS/TS
pnpm typecheck               # type-check JS/TS
pnpm test                    # test JS/TS
pre-commit run --all-files   # all pre-commit hooks
docker compose up -d         # local Postgres+pgvector, Valkey, api, worker, web
```

## Non-negotiables

- **Runtime model is OpenAI `gpt-5.4-mini` via the Responses API.** Claude Code is the development
  assistant only — never substitute Claude models into the runtime architecture.
- Financial values use decimal types; timestamps are timezone-aware UTC. Quota resets display in IST.
- Financial calculations are deterministic. The LLM interprets evidence; it never invents prices or
  performs authoritative arithmetic.
- Deterministic rate and history features must keep working when OpenAI is unavailable.
- Never expose hidden chain-of-thought, credentials, or unredacted sensitive content.
- Provider independence: external integrations go behind typed provider interfaces.
- Small, reviewable increments. Do not modify `main` directly. Do not push or open a PR unless asked.

## Current state

Phase 0, Sprint 0. See the Detailed Implementation Plan for ticket order (`GMAA-001` onward).
