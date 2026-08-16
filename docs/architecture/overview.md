# Architecture overview

## Shape

Start with a modular monolith and separate workers for background work. The repository is a monorepo with intended top-level areas:

```text
apps/
  finance-bot/
  finance-miniapp/
  downloader-bot/       # gated; no implementation yet
  document-bot/         # gated; no implementation yet
services/
  api/
  worker/
packages/
  auth/
  billing/
  referrals/
  notifications/
  telegram/
  observability/
infra/
docs/
```

Directories for gated products may remain documentation-only until their gate opens.

## Stack

- Python, FastAPI, aiogram
- PostgreSQL, SQLAlchemy, Alembic
- Redis and background workers
- React, TypeScript, Vite
- Docker Compose for local development

## Bounded modules

- Identity and consent
- Finance ledger and recurring entries
- Savings goals and deterministic budgets
- Coaching policy and notification preferences
- Billing, subscription, and credit ledger
- Referrals and abuse controls
- Administration and time-bound support grants
- Product analytics and privacy-safe observability

## Reliability rules

- Financial and credit mutations are transactional.
- External callbacks and jobs are idempotent.
- Retries use stable event identifiers.
- Deletion is a tracked workflow with an auditable completion state.
- Raw user content never appears in normal application logs.
