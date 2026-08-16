# Monetization and referrals

## Finance plans

- Basic text entry and basic reports remain free.
- New users receive a 30-day coaching trial.
- Coaching subscription target price: **149,000 toman per month**.
- Voice and OCR use separately metered credits.
- Annual plans wait until renewal and cost data are known.

The operational budget ceiling is 3,000,000 toman per month until revenue. Spending is reviewed monthly and is not an unlimited commitment.

## Payment

Zibal is the intended rial payment provider. The integration must:

- create server-side pending orders;
- verify callbacks directly with the provider;
- use idempotency to prevent duplicate fulfillment;
- validate amount and currency unit server-side;
- separate order, payment, fulfillment, and subscription states;
- represent refunds and manual corrections as compensating ledger entries;
- audit every privileged mutation;
- never store card details or payment secrets.

Local development uses a provider interface and a fake adapter until public callback infrastructure and owner-supplied credentials are available.

## Staged referral rewards

1. A valid first start earns a small voice/OCR credit.
2. Ten transactions across at least three days earn seven coaching days.
3. A successful paid subscription earns fifteen coaching days.

Rewards have monthly caps, unique event keys, abuse flags, and reversible ledger entries. Merely starting the bot does not earn the primary reward.

## Revenue evidence

- Payment evidence: at least three genuine customers.
- Early revenue signal: at least ten paying subscribers.
- Operating-cost coverage: recurring revenue at or above the monthly operating cost.
- Subscription evidence: meaningful renewal in the second paid month.
