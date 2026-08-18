FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1     PYTHONUNBUFFERED=1     PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /workspace

RUN addgroup --system app && adduser --system --ingroup app app

COPY pyproject.toml alembic.ini ./
COPY services ./services
COPY packages ./packages
COPY apps/finance-bot ./apps/finance-bot
COPY tests ./tests
RUN pip install --no-cache-dir .

USER app