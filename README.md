# AurumIQ

Chennai-first Gold Market AI Agent. Provides current and historical Chennai 22K and 24K gold rates,
deterministic comparisons, and evidence-based explanations of price movements using international spot
gold, USD/INR, MCX futures, macroeconomic events, and financial news.

AurumIQ provides cautious, non-personalised decision support. It does not issue guaranteed or
personalised buy/sell trading instructions.

## Status

Phase 0, Sprint 0 — repository scaffold. Not yet functional.

## Documentation

The specification lives in `docs/controlled/` and is **read-only**. Start with
[CLAUDE.md](CLAUDE.md) for the working contract: document precedence, protected files, the mandatory
engineering workflow, and approved commands.

## Quick start

Prerequisites: Python 3.12+, Node.js LTS, Docker, [uv](https://docs.astral.sh/uv/), pnpm.

```bash
uv sync          # Python dependencies
pnpm install     # JS dependencies
docker compose up -d
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full setup, quality gates, and contribution workflow.

## Architecture

Modular monolith with independently scalable workers. Next.js frontend, FastAPI backend, LangGraph
agent orchestration over OpenAI `gpt-5.4-mini`, Supabase PostgreSQL with pgvector, Valkey cache and
broker, Celery background jobs. Financial calculations are deterministic and never delegated to the
model. See `docs/controlled/Gold_Market_AI_Agent_TRD.md`.

## Licence

Not yet determined.
