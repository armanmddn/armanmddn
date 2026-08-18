# Telegram Product Platform

A modular platform for three sequential Telegram products, beginning with a goal-based Persian finance coach. The downloader and study assistant remain gated until the preceding product completes all ten phases and receives explicit product-owner approval.

## Current status

- Finance F1: product contract and executable backlog complete.
- Finance F2: repository foundation and local runtime complete.
- Finance F3–F10: not started.
- Downloader and document assistant: planned only; implementation is locked.

See [`docs/roadmap.md`](docs/roadmap.md) for phase goals and approval gates.

## Local development

Prerequisites are Docker Engine, Docker Compose v2, and optionally GNU Make. A Telegram token is not required because the default adapter is local and fake.

```bash
make up
```

The command builds and starts PostgreSQL, Redis, migrations, FastAPI, the fake finance bot, the worker, and the Finance Mini App. Then open:

- API readiness: <http://localhost:8000/health/ready>
- Finance Mini App: <http://localhost:5173>

Useful commands:

```bash
make ps
make logs
make check
make down
make reset
```

Read the complete [local runtime guide](docs/development/local-runtime.md) for configuration, live polling, migrations, and acceptance checks.

## Stack

- Python 3.12, FastAPI, aiogram, SQLAlchemy, Alembic
- PostgreSQL and Redis
- React, TypeScript, and Vite
- Docker Compose

## Security

Copy `.env.example` to `.env` for local overrides. Never commit a real bot token, payment credential, database secret, or private key. Sensitive finance, downloader, and document data remain isolated by product boundary.