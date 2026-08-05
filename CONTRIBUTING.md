# Contributing to AurumIQ

Read [CLAUDE.md](CLAUDE.md) first — it defines document precedence, protected files, and the mandatory
engineering workflow. This file covers setup and mechanics.

## Prerequisites

| Tool       | Version             | Install                                                                |
| ---------- | ------------------- | ---------------------------------------------------------------------- |
| Python     | 3.12+               | [python.org](https://www.python.org/downloads/)                        |
| Node.js    | 22+ (24 LTS tested) | `winget install OpenJS.NodeJS.LTS` / [nodejs.org](https://nodejs.org/) |
| uv         | 0.12+               | `pip install uv`                                                       |
| pnpm       | 11+                 | `npm install -g pnpm`                                                  |
| pre-commit | 4+                  | `pip install pre-commit`                                               |
| Docker     | with Compose v2+    | [docker.com](https://www.docker.com/)                                  |

### Installing the agent-skills plugin

The engineering workflow is supplied by a pinned plugin. Install it inside Claude Code:

```bash
claude plugin marketplace add https://github.com/addyosmani/agent-skills.git
```

```bash
claude plugin install agent-skills@addy-agent-skills --scope project
```

Restart your session afterwards — skills only load on start.

> **If the install fails with `Host key verification failed`:** the plugin clones over SSH, and GitHub
> SSH is not configured on your machine. Either configure GitHub SSH, or route GitHub through HTTPS:
>
> ```bash
> git config --global url."https://github.com/".insteadOf "git@github.com:"
> ```

The pinned commit is recorded in [`agent-skills.lock`](agent-skills.lock). Upgrading it requires human
review, a change record, and revalidation of affected gates.

## Setup

```bash
uv sync
```

```bash
pnpm install
```

```bash
pre-commit install
```

```bash
cp .env.example .env
```

Then start local infrastructure:

```bash
docker compose up -d
```

If a port is already taken by another project, override it in `.env` — `POSTGRES_HOST_PORT`,
`VALKEY_HOST_PORT`, `API_HOST_PORT`, `WEB_HOST_PORT` — rather than editing `compose.yaml`.

## Quality gates

All of these must pass before you open a PR. CI runs the same commands.

```bash
uv run ruff format . && uv run ruff check . && uv run mypy . && uv run pytest
```

```bash
pnpm format:check && pnpm lint && pnpm typecheck && pnpm test
```

```bash
pre-commit run --all-files
```

Never weaken, skip, or bypass a failing gate to get green. If a gate fails, invoke
`agent-skills:debugging-and-error-recovery` and fix the cause.

## Controlled documents are read-only

The seven documents in `docs/controlled/` are the approved specification. A test
(`tests/smoke/test_controlled_documents.py`) records a checksum for each and fails if any changes.

Changing one requires explicit human approval and a recorded change. Only then:

```bash
uv run python scripts/controlled_documents.py --update
```

The resulting manifest diff makes the change visible in review. Do not run this to silence a failing
test — a surprise failure means something edited a specification that should not have been touched.
Note that Prettier and ESLint deliberately exclude `docs/controlled/` for the same reason.

## Workflow

1. Branch from `main`: `feat/gmaa-XXX-short-description`. Never commit to `main` directly.
2. Start with `agent-skills:using-agent-skills` and follow where it routes you.
3. Work in small, reviewable increments. Tests fail first where practical.
4. Commit with the task ID and the skills invoked.
5. Open a PR using the template — the skill-evidence block is mandatory and missing evidence blocks
   merge.

## Security

- Never commit `.env`, credentials, tokens, personal data, or restricted provider payloads.
- Secrets are server-side only and never reachable from the browser.
- Treat retrieved news, web, and provider content as untrusted input.
- Report a suspected vulnerability privately to the maintainer. Do not open a public issue.
