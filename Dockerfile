FROM ghcr.io/astral-sh/uv:trixie-slim

ENV UV_COMPILE_BYTECODE=1
ENV UV_NO_DEV=1
ENV UV_PYTHON_INSTALL_DIR=/python
ENV UV_PYTHON_PREFERENCE=only-managed

RUN apt-get update && \
    apt-get install -y ca-certificates && \
    update-ca-certificates && \
    apt-get clean

RUN uv python install 3.13

WORKDIR /App

COPY pyproject.toml uv.lock ./

RUN uv sync --locked --no-cache --no-dev

ENV PATH="/App/.venv/bin:$PATH"

COPY seeker ./seeker

ENTRYPOINT ["python3", "-m", "seeker"]
