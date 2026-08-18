# Product vision

## Portfolio

The portfolio consists of three independent Telegram products built on a shared technical platform:

1. **Goal-based finance coach** — helps Iranian users retain a chosen amount at the end of each month.
2. **Creator downloader** — retrieves media from a deliberately small set of sources and prepares it for publishing.
3. **Persian study and document assistant** — extracts, translates, summarizes, and answers grounded questions about typed or scanned documents.

Each product has its own bot identity, user experience, sensitive data boundary, and product metrics. Authentication, billing, credits, referrals, notifications, administration, and observability may be shared.

## Delivery constraint

Products are delivered sequentially. The finance coach is first. The creator downloader cannot enter implementation before all ten finance phases are complete and the product owner explicitly approves the transition. The same rule gates the document assistant behind the downloader.

## Finance product promise

> We do not merely show where the user's money went; we help the user finish the month with a chosen amount saved.

The initial audience is general Iranian Telegram users with recurring income who struggle to control discretionary spending and save consistently.

## Principles

- Optimize for a measurable user outcome, not feature count.
- Keep free basic text entry useful so the habit survives after a trial ends.
- Explain financial calculations with deterministic, testable rules.
- Use AI only behind confirmation and validation boundaries.
- Minimize sensitive data and make export and permanent deletion first-class capabilities.
- Validate willingness to pay before expanding scope.
