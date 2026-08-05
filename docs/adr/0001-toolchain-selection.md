# ADR-0001: Repository toolchain selection

- **Status:** Accepted
- **Date:** 2026-08-05
- **Deciders:** Vikram M
- **Task:** GMAA-001

## Context

The TRD fixes the technology stack (FastAPI, Next.js, SQLAlchemy, LangGraph, pgvector) but does not
specify the Python package manager, the JavaScript monorepo tool, the linters, or how much of the
application should exist at the end of Sprint 0. TRD section 3.2 requires exact dependency versions
pinned through lock files. These choices bind every later sprint, so they are recorded here rather
than left implicit in configuration files.

## Decision

**Python:** `uv` for dependency management and locking, `ruff` for lint and format, `mypy` in strict
mode, `pytest` for tests. A `uv` workspace at the repository root with `apps/api` as a member, so
`uv sync` works from the root as documented in `CLAUDE.md`.

**JavaScript:** `pnpm` workspaces spanning `apps/*` and `packages/*`, with ESLint, Prettier,
TypeScript in strict mode, and Vitest configured at the root. Turborepo is deliberately not adopted
yet.

**Scaffold depth:** Sprint 0 delivers a skeleton with smoke checks. Directory structure, manifests,
lock files, quality gates, templates, compose and CI all run green on essentially empty projects.
Runtime dependencies (FastAPI, SQLAlchemy, LangGraph, `openai`, `langchain-openai`, Next.js) are
**not** added until the sprint that writes code using them.

## Alternatives considered

| Option                                         | Why not chosen                                                                                                                                                                |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Poetry instead of uv                           | Mature and more widely recognised, but materially slower in CI. `uv` covers venv, resolution and locking in one tool.                                                         |
| pip-tools + black + flake8                     | Most conservative, but the largest number of config surfaces and the slowest feedback loop.                                                                                   |
| pnpm + Turborepo                               | Turborepo's task orchestration and remote caching are not yet earning their configuration cost across two packages. Revisit when CI build time becomes a measured bottleneck. |
| npm workspaces                                 | Universally familiar, but slower installs and weaker dependency isolation than pnpm.                                                                                          |
| Scaffold runnable hello-world apps in Sprint 0 | Pulls GMAA-002 work forward and enlarges the review surface for a governance ticket.                                                                                          |

## Consequences

**Positive:**

- One fast tool per language rather than three overlapping ones.
- Lock files pin exact versions, satisfying TRD section 3.2.
- Runtime dependency versions get locked against code that actually exercises them, instead of being
  guessed months in advance and then silently drifting.
- The Sprint 0 review stays small enough to review honestly.

**Negative / accepted costs:**

- `uv` and `pnpm` are less familiar to some contributors than pip and npm. `CONTRIBUTING.md` documents
  installation.
- `apps/web` is an empty workspace slot with no Next.js until a later sprint. Anyone expecting a
  runnable frontend after GMAA-001 will not find one.
- Node.js 24 LTS, `uv`, `pnpm` and `pre-commit` are prerequisites a contributor must install.

**Reversibility:** High for the linters (config-only). Moderate for the package managers — switching
means regenerating lock files and CI steps, but no application code changes. Adding Turborepo later is
additive and does not invalidate the pnpm workspace layout.

## Verification

A clean clone runs `uv sync`, `pnpm install`, and every quality gate green without manual steps. This
was verified during GMAA-001 by cloning the branch into a temporary directory and running only the
commands documented in `CONTRIBUTING.md`.

Revisit this ADR if CI wall-clock time for the JS workspace exceeds roughly five minutes (consider
Turborepo), or if `uv` resolution proves unreliable against the pinned FastAPI and LangGraph stack.
