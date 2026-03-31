FROM ghcr.io/astral-sh/uv:trixie-slim

ENV UV_COMPILE_BYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /App

COPY pyproject.toml uv.lock ./

RUN uv sync --no-dev --no-cache

COPY seeker ./seeker

ENTRYPOINT ["uv", "run", "python", "-m", "seeker"]
