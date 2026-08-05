# AurumIQ FastAPI backend and Celery workers.
#
# Sprint 0 skeleton: installs the locked dependency set so the image is real and
# buildable. The CMD becomes a uvicorn entrypoint in GMAA-002 when app/main.py
# exists.

FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

COPY --from=ghcr.io/astral-sh/uv:0.12.1 /uv /usr/local/bin/uv

WORKDIR /srv

# Dependency layer: copy manifests first so edits to source do not invalidate it.
COPY pyproject.toml uv.lock ./
COPY apps/api/pyproject.toml ./apps/api/
RUN uv sync --frozen --no-install-project

COPY apps/api ./apps/api
RUN uv sync --frozen

ENV PATH="/srv/.venv/bin:$PATH"

# Non-root by default.
RUN useradd --create-home --uid 10001 aurumiq && chown -R aurumiq:aurumiq /srv
USER aurumiq

EXPOSE 8000

CMD ["python", "-c", "print('AurumIQ API image built. Application entrypoint arrives in GMAA-002.')"]
