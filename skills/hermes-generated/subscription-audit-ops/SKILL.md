---
name: subscription-audit-ops
description: Evidence-first recurring-charge and subscription audit workflow for Hermes. Use when auditing personal spend across cards, recurring merchants, and cancellation candidates under time or cash pressure.
metadata:
  hermes:
    tags: [generated, finance, subscriptions, recurring-charges, credit-karma, email, verification]
---

# Subscription Audit Ops

Use this when the user asks to audit subscriptions, recurring charges, monthly software spend, or cancellation candidates across personal cards and accounts.

## Skill Stack

Pull these imported skills into the workflow when relevant:
- `continuous-agent-loop` for bounded multi-step audits with explicit stop conditions when proof is partial
- `agentic-engineering` for exact done conditions and the one-to-three-change scope discipline
- `market-research` when the user wants vendor or plan comparisons before canceling
- `deep-research` and `exa-search` when outside pricing, cancellation flows, or market alternatives need current verification
- `search-first` before inventing a custom scraper, parser, or finance helper
- `eval-harness` mindset for proof tiers, timestamps, and exact confidence labels

## When To Use

- user says `audit my subscriptions`, `what can i cancel`, `find recurring charges`, or similar
- the user wants a ruthless keep/cancel pass before a move, budget cut, or runway review
- direct card exports are missing and you need to assemble evidence from multiple partial sources

## Workflow

1. Start with the freshest finance snapshot available:
   - read `/Users/affoon/.hermes/workspace/business/financial-status.md`
   - use it as the source of truth for last verified recurring-charge evidence, card balances, and snapshot timestamp
   - if it references Credit Karma or other live sources, preserve the exact timestamp in the final answer
2. If live Credit Karma is accessible, use browser tools to confirm:
   - net worth page for balances and recent transactions
   - manage accounts page for linked institutions and account names
   - use `browser_vision` on screenshots when the DOM/snapshot truncates or hides account details
   - distinguish `visible recurring charge`, `recent transaction`, and `linked account` clearly
3. If direct transaction exports are unavailable, use fallback evidence layers:
   - search prior session logs for saved Credit Karma findings and merchant names
   - inspect known finance files in workspace and memory for previous subscription analyses
   - use email search for billing/receipt subjects only if it is likely to surface merchant proof
   - use a passwords export only as account-existence evidence, never as billing proof
4. Classify findings into proof tiers:
   - tier 1: live transaction or current finance snapshot with amount/date
   - tier 2: prior saved note with explicit price and service
   - tier 3: account-existence evidence only, needs billing verification
5. Build the recommendation set:
   - `cancel now` for low-value tools with explicit prior cost evidence or obvious move-related services
   - `verify this week` for plausible subscriptions without live billing proof
   - `keep for now` for core infra or tools still likely in active use
   - call out the biggest unresolved swing item, usually the highest-cost ambiguous plan
6. Report exact confidence:
   - say `first-pass audit` if the evidence is partial
   - never pretend you have a complete ledger unless you saw a full recurring-charge screen or statement export
   - separate `billing proof`, `account evidence`, and `inference`

## Heuristics That Worked

- `financial-status.md` may contain the freshest recurring-charge evidence even when live browser access later fails
- prior Apple Notes / knowledge-base subscription analyses are useful for cost baselines, but they are not live proof
- Credit Karma `Manage accounts` can expose linked institutions even when transaction detail is sparse
- passwords export is good for finding likely paid surfaces like gym, utilities, hosting, SaaS, and media, but should never be used to claim a subscription is active
- move-related audits should explicitly check internet, gym, phone, and location-bound services first

## Pitfalls

- do not claim `every single subscription` unless you have a current recurring-charge list or statement export
- do not turn passwords-export hits into confirmed charges
- do not mix `recent transaction` with `recurring subscription`
- do not hide stale timestamps
- do not miss the biggest swing item just because it is ambiguous, flag it as the top verification priority

## Verification

- answer includes the freshest verified finance timestamp
- each recommendation is labeled by evidence strength
- final output separates `cancel now`, `verify this week`, and `keep for now`
- if coverage is partial, the answer explicitly says so and names the fastest path to full certainty
