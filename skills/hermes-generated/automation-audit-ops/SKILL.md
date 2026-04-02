---
name: automation-audit-ops
description: Evidence-first automation audit workflow for Hermes. Use when auditing cron jobs, tooling, connectors, auth wiring, MCP surfaces, local-system parity, or automation overlap before fixing or pruning anything.
metadata:
  hermes:
    tags: [generated, automation, cron, tooling, workflow, audit, verification, parity, auth, mcp]
---

# Automation Audit Ops

Use this when the user asks what automations are live, which jobs are broken, where overlap exists, or what tooling and connectors Hermes is actually benefiting from right now.

## Skill Stack

Pull these skills into the workflow when relevant:
- `continuous-agent-loop` for multi-step audits that cross cron, tooling, and config surfaces
- `agentic-engineering` for decomposing the audit into verifiable units with a clear done condition
- `terminal-ops` when the audit turns into a concrete local fix or command run
- `research-ops` when local inventory has to be compared against current docs, platform support, or missing-capability claims
- `search-first` before inventing a new helper, wrapper, or inventory path
- `eval-harness` mindset for exact failure signatures, proof paths, and post-fix verification

## When To Use

- user asks `what automations do i have set up?`
- user asks to audit cron overlap, redundancy, broken jobs, or job coverage
- user asks which tools, connectors, auth surfaces, MCP servers, or wrappers are actually live
- user asks what is ported from another local agentic system, what is still missing, or what should be wired next
- the task spans both local inventory and a small number of high-impact fixes

## Workflow

1. Start from prepared evidence when it exists:
   - read the prepared failure summary, request patterns, docs scan, and skill-sync notes before opening raw logs
   - if the prepared failure summary says there is no dominant cluster, do not spray-read raw log bundles anyway
2. Inventory the live local surface before theorizing:
   - for cron work, inspect `$HERMES_HOME/cron/jobs.json`, the latest relevant `$HERMES_HOME/cron/output/<job>/...` files, and matching `$HERMES_HOME/cron/delivery-state/*.json`
   - for tooling or connector parity, inspect live config, plugins, helper scripts, wrappers, auth files, and verification logs before claiming something is missing
   - when the user names another local system or repo, inspect that live source too before saying Hermes lacks or already has the capability
3. Classify each finding by failure class:
   - active broken logic
   - auth or provider outage
   - stale error that has not rerun yet
   - MCP or schema-level infrastructure break
   - overlap or redundancy
   - missing or unported capability
4. Classify each surfaced integration by live state:
   - configured
   - authenticated
   - recently verified
   - stale or broken
   - missing
5. Answer inventory questions with proof, not memory:
   - group automations by surface such as cron, messaging, content, GitHub, research, billing, or health
   - include schedules, current status, and the proof path behind each claim
   - for parity audits, separate `already ported`, `available but not wired`, and `missing entirely`
   - for overlap audits, end with `keep`, `merge`, `cut`, or `fix next`, plus the evidence path behind each call
6. Freeze audit scope before changing anything:
   - if the user asked for an inventory, audit table, comparison, or otherwise kept the task read-only, stay read-only until the user explicitly asks for fixes
   - collect evidence with config reads, logs, status files, and non-writing proving steps first
   - do not rewrite cron, config, wrappers, or auth surfaces just because a likely fix is visible
7. Fix only the highest-impact proved issues:
   - keep the pass bounded to one to three changes
   - prefer durable config, instruction, or helper-script fixes over one-off replies
   - if the prepared evidence shows a failure happened before a later config change, record that as stale-runtime or stale-status risk instead of rewriting the config blindly
8. Verify after any change:
   - rerun the smallest proving step
   - regenerate any affected context artifacts
   - record exact remaining risks when runtime state is outside the scope of the current pass

## Pitfalls

- do not treat `last_status=error` as proof of a current bug if the job has not rerun since recovery
- do not conflate a provider outage or MCP schema error with job-specific prompt logic
- do not claim a tool or connector is live just because a skill references it
- do not treat `present in config` as the same thing as `authenticated` or `recently verified`
- do not say Hermes is missing a capability before comparing the named local system or repo the user pointed at
- do not answer `what automations do i have set up?` from memory without reading the current local inventory
- do not open broad raw log bundles when the prepared summary already says there is no dominant cluster
- do not turn an audit-only inventory pass into config or cron edits unless the user expands scope
- do not fix low-value redundancy before resolving the concrete broken path the user actually asked about

## Verification

- each important claim points to a live file, log, config entry, or exact failure signature
- each surfaced integration is labeled `configured`, `authenticated`, `recently verified`, `stale/broken`, or `missing`
- each fix names the proving command, regenerated artifact, or re-read output that confirmed it
- remaining risks clearly distinguish stale status, runtime drift, and unresolved infrastructure blockers
