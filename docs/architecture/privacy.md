# Privacy and support access

## Data minimization

Store only data required to provide the selected feature. Raw receipt images and voice messages are deleted after successful processing unless the user explicitly chooses a short retention window. Finance data, downloader jobs, and study documents are isolated by product boundary.

## User controls

Users can:

- export their data;
- see active consent and support grants;
- revoke a support grant early;
- permanently delete their account and product data;
- control coaching intensity and notification categories.

## Administration

Routine administrators may see internal identifiers, account state, subscriptions, payments, credit-ledger entries, referral qualification, abuse flags, and redacted errors. They may not routinely see transaction descriptions, income, balances, voice, receipts, or documents.

Sensitive support access requires explicit user consent, a narrow scope, a short expiry, revocation, and an audit record of every access. Secrets and sensitive user content are forbidden in logs.

## AI providers

Before enabling an external AI, OCR, or speech provider, record what data is sent, retention terms, processing location, deletion behavior, and the fallback when the user declines. Provider use must be configurable and quota-limited.
