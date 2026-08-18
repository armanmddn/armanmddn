# Repository instructions

## Product order

This repository contains a shared platform for three Telegram products. Work on them in this order:

1. Finance coach (`finance`)
2. Creator downloader (`downloader`)
3. Persian study/document assistant (`documents`)

Do not start implementation of the downloader until all ten finance phases are complete and the product owner explicitly approves moving on. Apply the same gate before starting the document assistant.

## Engineering conventions

- Backend: Python, FastAPI, aiogram, SQLAlchemy, Alembic, PostgreSQL, and Redis.
- Frontend: React, TypeScript, and Vite, with mobile-first RTL support.
- Begin as a modular monolith. Preserve module boundaries; do not introduce networked microservices without measured need.
- Store monetary amounts as integers with an explicit currency/unit. Never use floating point for money.
- Store timestamps in UTC and localize only at presentation boundaries.
- AI may propose interpretations and language, but deterministic code owns financial calculations, billing, credits, limits, and referrals.
- Never commit secrets. Keep real credentials out of examples, logs, fixtures, screenshots, and documentation.
- Sensitive finance data, downloader jobs, and document contents must remain logically isolated.
- Every behavior change requires tests. Payment, ledger, referral, and deletion flows require integration tests.

## Phase loop

Each phase follows the loop documented in `docs/roadmap.md`: define the measurable goal, identify required inputs, implement the smallest scope, run checks, compare results with acceptance criteria, and either close the phase or repeat it. Do not silently relax acceptance criteria.
