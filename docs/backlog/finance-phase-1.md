# Finance phase 1 backlog and acceptance

## Phase objective

Create an implementable contract for the first product without beginning later products or committing to unvalidated features.

## Personas and jobs

Primary persona: an Iranian Telegram user with recurring monthly income who wants to retain a specific amount but loses track of discretionary spending.

Core job:

> Given my income, payday, fixed expenses, and savings target, tell me what I can spend now, warn me before I leave the plan, and show how to recover without judging me.

## Primary journey

1. User starts the finance bot.
2. User progressively enters monthly income, payday, savings target, and coaching mode.
3. User records a first Persian text transaction.
4. Bot previews parsed facts and requests confirmation when needed.
5. Deterministic rules update remaining allowance and goal progress.
6. Bot delivers a coaching message only when the selected policy permits it.
7. User inspects or corrects details in the Mini App.
8. User sees a weekly report and measurable progress.
9. After the trial, free capture remains available while coaching requires subscription.

## Epics mapped to phases

| Epic | Phase |
| --- | --- |
| Local runtime, CI, configuration | F2 |
| Telegram identity, onboarding, consent | F3 |
| Transactions, wallets, recurring entries | F4 |
| Savings target, budgets, coaching policy | F5 |
| Mini App, history, reports | F6 |
| Trial, Zibal, credits, referrals | F7 |
| Admin, support grants, export/deletion, operations | F8 |
| Production beta and metrics | F9 |
| Launch decision and release | F10 |

## Cross-cutting definition of done

- Acceptance criteria and failure states are documented before implementation.
- Tests cover normal, boundary, retry, and unauthorized behavior.
- Money uses integer toman values; time is stored in UTC.
- Logs and analytics contain no raw sensitive content or secrets.
- User-facing Persian is RTL-safe, supportive, and non-judgmental.
- Security/privacy impact and deletion behavior are reviewed.
- Documentation and migrations are updated with code.

## Phase 1 acceptance evidence

- Product promise and delivery order are written in `docs/product/vision.md`.
- MVP and exclusions are written in `docs/product/mvp.md`.
- Pricing, payment, and referral rules are written in `docs/product/monetization.md`.
- Validation thresholds and events are written in `docs/product/metrics.md`.
- Architecture and privacy boundaries are written in `docs/architecture/`.
- Ten loop-based phases for each product and hard approval gates are written in `docs/roadmap.md`.

## Inputs deferred to the phase that needs them

- F2: optional development Bot Token for live polling; fake mode must not require it.
- F7: current Zibal integration documentation and later credentials via secret storage.
- F9: server, domain, production Bot Token, payment readiness, privacy/support contacts, and recruitment channel.

## Phase 1 result

The phase is complete when documentation checks pass, the repository is clean after commit, and the product owner can trace every MVP capability to exactly one implementation phase. Phase 2 is the next permitted implementation phase.
