---
name: finance-billing-ops
description: Evidence-first Stripe sales, billing incident, and team-pricing workflow for Hermes. Use when pulling sales, investigating duplicate charges or failed payments, checking whether team billing is real in code, or benchmarking pricing.
metadata:
  hermes:
    tags: [generated, finance, billing, stripe, pricing, workflow, verification]
---

# Finance Billing Ops

Use this when the user asks about Stripe sales, refunds, failed payments, duplicate charges, org or team billing behavior, pricing strategy, or whether the product logic matches the marketing copy.

## Skill Stack

Pull these imported skills into the workflow when relevant:
- `market-research` for competitor pricing, billing models, and sourced market context
- `deep-research` or `exa-search` when the answer depends on current public pricing or enforcement behavior
- `search-first` before inventing a Stripe, billing, or entitlement path
- `eval-harness` mindset for exact status reporting and separating proof from inference
- `agentic-engineering` and `plankton-code-quality` when the answer depends on checked-in ECC billing or entitlement code

## When To Use

- user says `pull in stripe data`, `any new sales`, `why was he charged`, `refund`, `duplicate charge`, `team billing`, `per seat`, or similar
- the question mixes revenue facts with product truth, for example whether team or org billing is actually implemented
- the user wants a pricing comparison against Greptile or similar competitors

## Workflow

1. Start with the freshest revenue evidence available:
   - if a live Stripe pull exists, refresh it first
   - otherwise read `$HERMES_WORKSPACE/business/stripe-sales.md` and `$HERMES_WORKSPACE/business/financial-status.md`
   - always report the snapshot timestamp if the data is not live
2. Normalize the revenue picture before answering:
   - separate paid sales, failed attempts, successful retries, `$0` invoices, refunds, disputes, and active subscriptions
   - do not treat a transient decline as lost revenue if the same checkout later succeeded
   - flag any duplicate subscriptions or repeated checkouts with exact timestamps
3. For a customer billing incident:
   - identify the customer email, account login, subscription ids, checkout sessions, payment intents, and timing
   - determine whether extra charges are duplicates, retries, or real extra entitlements
   - if recommending refunds or consolidation, explain what product value the extra charges did or did not unlock
4. For org, seat, quota, or activation questions:
   - inspect the checked-in billing and usage code before making claims
   - verify checkout quantity handling, installation vs user usage keys, unit-count handling, seat registry or member sync, and quota stacking
   - inspect the live pricing copy too, so you can call out mismatches between marketing and implementation
5. For pricing and competitor questions:
   - use `market-research`, `deep-research`, or `exa-search` for current public evidence
   - separate sourced facts from inference, and call out stale or incomplete pricing signals
6. Report in layers:
   - current sales snapshot
   - customer-impact diagnosis
   - code-backed product truth
   - recommendation or next action
7. If the user wants fixes after diagnosis:
   - hand the implementation path to `agentic-engineering` and `plankton-code-quality`
   - keep the evidence trail so copy changes, refunds, and code changes stay aligned

## Pitfalls

- do not claim `new sales` without saying whether the data is live or a saved snapshot
- do not mix failed attempts into net revenue if the payment later succeeded
- do not say `per seat` unless the code actually enforces seat behavior
- do not assume extra subscriptions increase quotas without verifying the entitlement path
- do not compare competitor pricing from memory when current public sources are available

## Verification

- the answer includes a snapshot timestamp or an explicit live-pull statement
- the answer separates fact, inference, and recommendation
- code-backed claims cite file paths or code areas
- customer-impact statements name the exact payment or subscription evidence they rely on
