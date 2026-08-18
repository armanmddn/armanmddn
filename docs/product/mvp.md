# Finance coach MVP

## In scope

- Persian text-based income and expense capture.
- Suggested amount, direction, category, wallet, and transaction time.
- Preview and confirmation before an ambiguous transaction is committed.
- Transaction history, edit, and delete.
- A simple wallet and recurring monthly income/expenses.
- Progressive onboarding: income, payday, savings target, coaching mode, then first transaction.
- Monthly savings target and deterministic daily/weekly spending allowance.
- Calm, balanced, and strict coaching modes.
- Threshold and unusual-spend alerts with actionable recovery suggestions.
- Basic free reports and advanced weekly/monthly coaching reports.
- A mobile-first RTL Telegram Mini App.
- A 30-day coaching trial, subscription lifecycle, credit ledger, and staged referrals.
- Data export, account deletion, consent records, and time-limited support access.
- Local development through Docker Compose before public deployment.

## Beta after the core is stable

- Quota-limited speech-to-text transaction entry.
- Quota-limited receipt OCR.
- Immediate deletion of raw voice/image inputs after successful processing.

## Explicitly out of scope

- Direct bank connections.
- Investment, lending, legal, or tax advice.
- Group expense splitting and a full debt module.
- Multi-currency user interfaces and live market prices.
- Native mobile applications.
- Unbounded AI, speech, or OCR usage.
- Implementation of either later bot.

## AI boundary

AI may interpret ambiguous text, suggest a category, ask a clarification question, explain a report, or phrase recovery options. Deterministic code calculates balances, budgets, progress, dates, subscriptions, credits, payments, referral rewards, and limits. Important changes require user confirmation.

## Money and time

- User-facing finance values use integer toman amounts with an explicit `TOMAN` unit.
- Payment-provider unit conversions occur only inside provider adapters.
- Timestamps are persisted in UTC and presented using the user's timezone and the Solar Hijri calendar.
