---
name: hermes-generated
description: Index skill for Hermes-generated workflow packs. Use when the task clearly belongs to a Hermes-derived operator pattern and you need to choose the right generated subskill before acting.
origin: ECC
---

# Hermes Generated

This skill is the entrypoint for the Hermes-generated skill bucket.

Use it when the user is operating in a Hermes-style workflow and the task appears to map to one of the generated operator packs in this directory.

## Purpose

- route the request to the right Hermes-generated subskill
- avoid inventing a new workflow when a stable Hermes pattern already exists
- keep Hermes-derived operational behavior discoverable in the public ECC surface

## Available Subskills

- `automation-audit-ops`
- `content-crosspost-ops`
- `ecc-tools-cost-audit`
- `email-ops`
- `finance-billing-ops`
- `knowledge-ops`
- `messages-ops`
- `research-ops`
- `terminal-ops`

## Routing Guidance

Choose the narrowest matching subskill first:

- content and distribution -> `content-crosspost-ops`
- ECC Tools burn, PR recursion, quota bypass, or premium-model leakage -> `ecc-tools-cost-audit`
- inbox, triage, cleanup, and email sequencing -> `email-ops`
- billing, revenue, and payments -> `finance-billing-ops`
- memory and prior-session recovery -> `knowledge-ops`
- Telegram, chat, or messaging triage -> `messages-ops`
- research and source-backed investigation -> `research-ops`
- shell execution and terminal workflows -> `terminal-ops`
- cron, overlap, or automation hygiene -> `automation-audit-ops`

If no generated subskill fits cleanly, fall back to the closest standard ECC skill instead of forcing a Hermes-specific pattern.
