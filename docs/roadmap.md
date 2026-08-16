# Sequential roadmap and phase loops

## The phase loop

Every phase uses the same loop:

1. **Goal** — state one measurable outcome.
2. **Inputs** — list owner decisions, credentials, research, or dependencies required.
3. **Build** — implement only the smallest scope needed for the goal.
4. **Check** — run automated tests, security/privacy checks, and a product acceptance scenario.
5. **Evaluate** — compare evidence against written acceptance criteria.
6. **Close or repeat** — close only when criteria pass; otherwise log the gap and repeat the phase.

Credentials are requested only when the relevant phase needs them and must never be pasted into tracked files or committed.

## Bot 1 — goal-based finance coach

### F1. Product contract and executable backlog — current phase

- **Goal:** freeze the MVP promise, boundaries, metrics, dependencies, and acceptance scenarios.
- **Inputs:** completed Grill Me decisions.
- **Build:** product, architecture, monetization, privacy, metrics, and roadmap documents.
- **Check:** internal consistency and traceability from promise to backlog.
- **Acceptance:** every MVP capability belongs to a later phase; out-of-scope work is explicit; later bots remain gated.

### F2. Repository foundation and local runtime

- **Goal:** one-command local startup for API, bot, PostgreSQL, Redis, worker, and web app.
- **Inputs:** development Bot Token may be requested for live polling; a fake adapter must work without it.
- **Build:** monorepo skeleton, configuration, Docker Compose, health checks, migrations, CI, linting, and test harness.
- **Acceptance:** clean checkout starts locally; tests and migrations pass; no secrets are tracked.

### F3. Identity, onboarding, and consent

- **Goal:** a Telegram user can progressively onboard and manage consent/preferences.
- **Build:** Telegram identity, income/payday/target steps, coaching mode, timezone, Solar Hijri presentation, consent versioning.
- **Acceptance:** steps can be resumed or skipped; incomplete data is clearly marked; tests cover state transitions.

### F4. Deterministic transaction ledger

- **Goal:** safely capture, confirm, edit, delete, and list text transactions.
- **Build:** integer-toman ledger, wallets, categories, Persian parser, previews, recurring entries, idempotency.
- **Acceptance:** money invariants and duplicate-message tests pass; ambiguous input never commits silently.

### F5. Savings goal and coaching engine

- **Goal:** turn income, fixed expenses, and target into explainable daily/weekly allowances.
- **Build:** deterministic budget rules, thresholds, unusual-spend detection, recovery options, coaching modes.
- **Acceptance:** golden financial scenarios pass; every alert cites the data/rule that caused it.

### F6. Finance Mini App and reports

- **Goal:** users can inspect and correct their financial state in a mobile-first RTL interface.
- **Build:** Telegram auth validation, dashboard, transaction history/editing, goal progress, reports, accessibility states.
- **Acceptance:** key journeys pass component and end-to-end tests at common Telegram viewport sizes.

### F7. Billing, subscription, credits, and referrals

- **Goal:** safely meter paid value and fulfill verified payments exactly once.
- **Inputs:** Zibal documentation and later owner-supplied credentials; local fake provider remains available.
- **Build:** plans, trial, orders, Zibal adapter, subscription state, credit ledger, staged referrals, abuse controls.
- **Acceptance:** success/failure/cancel/retry/duplicate/refund scenarios pass; no callback can double-fulfill.

### F8. Privacy, administration, and operations

- **Goal:** provide export/deletion, least-privilege administration, recovery, and privacy-safe observability.
- **Build:** admin UI, support grants, audit log, export/deletion workflows, backup/restore, redaction, rate limits.
- **Acceptance:** deletion and restore drills pass; routine admins cannot read sensitive finance content.

### F9. Closed beta and validation loop

- **Goal:** run a reliable closed beta and measure the written 50-user gate.
- **Inputs:** production bot, domain/server, Zibal readiness, privacy/support contacts, and a recruitment channel will be requested here.
- **Build:** production deployment, onboarding analytics, feedback flow, incident runbook, controlled experiments.
- **Acceptance:** evidence is collected for every metric without raw sensitive analytics data.

### F10. Launch decision and release

- **Goal:** make an evidence-based launch, iterate, or stop decision and ship the approved release.
- **Build:** fix gate-blocking issues, finalize pricing/support/legal copy, release checklist, cost dashboard, rollback plan.
- **Acceptance:** product owner signs off; critical security/payment tests pass; decision report records metrics and costs.

**Hard gate:** after F10, stop. Do not begin Bot 2 until the product owner explicitly approves it.

## Bot 2 — creator downloader (planned only)

1. **D1 Market/legal feasibility:** validate creator workflow, sources, platform constraints, and acceptable use.
2. **D2 Source spike:** prove reliable retrieval for only two or three approved high-demand sources.
3. **D3 Job platform:** build isolated queues, quotas, cleanup, cancellation, and job observability.
4. **D4 Media delivery:** safe Telegram delivery, size handling, caching policy, and retention deletion.
5. **D5 Creator transforms:** format selection, audio extraction, compression, and splitting.
6. **D6 Creator UX:** fast link intake, job progress, output choices, and accessible error recovery.
7. **D7 Metering/billing:** credit estimates, subscriptions, fair-use limits, and staged referrals.
8. **D8 Abuse/security:** SSRF defenses, malware/content checks, rate limits, and resource isolation.
9. **D9 Closed beta:** measure successful-job rate, cost per job, repeat use, and willingness to pay.
10. **D10 Launch gate:** release only if reliability, unit economics, and policy review pass.

No D phase may begin before the finance F10 approval gate.

## Bot 3 — Persian study/document assistant (planned only)

1. **S1 Research/privacy contract:** validate study workflows, source rights, retention, and grounded-answer expectations.
2. **S2 Typed PDF ingestion:** parse Persian/English typed PDFs with page provenance.
3. **S3 Printed scan OCR:** process printed scans/images, quality scores, and correction workflows.
4. **S4 Document index:** create isolated, deletable document storage and page-grounded retrieval.
5. **S5 Study outputs:** summaries, key points, translation, flashcards, and editable exports.
6. **S6 Grounded Q&A:** answer from the document with page citations and explicit insufficient-evidence behavior.
7. **S7 Study UX:** upload/estimate/confirm/process/review flows in Telegram and Mini App.
8. **S8 Credits/billing:** page-based estimates, quotas, subscriptions, purchases, and referral credits.
9. **S9 Closed beta:** measure OCR accuracy, grounded-answer quality, cost, retention, and payment intent.
10. **S10 Launch gate:** ship only when quality, privacy, unit economics, and support readiness pass.

No S phase may begin before the downloader D10 approval gate.
