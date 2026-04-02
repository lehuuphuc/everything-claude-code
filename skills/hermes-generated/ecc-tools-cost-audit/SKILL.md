---
name: ecc-tools-cost-audit
description: Evidence-first ECC Tools burn and billing audit workflow. Use when investigating runaway PR creation, quota bypass, premium-model leakage, or GitHub App cost spikes in the ECC Tools repo.
origin: ECC
---

# ECC Tools Cost Audit

Use this when the user suspects the ECC Tools GitHub App is burning cost, over-creating PRs, bypassing usage limits, or routing free users into premium analysis paths.

## Skill Stack

Pull these imported skills into the workflow when relevant:
- `continuous-agent-loop` for scope freezes, recovery gates, and cost-aware tracing when audits are long or failure signatures repeat
- `terminal-ops` for repo-local inspection, narrow edits, and proving commands
- `finance-billing-ops` when customer-impact math has to be separated from repo behavior
- `agentic-engineering` for tracing entrypoints, queue paths, and fix sequencing
- `plankton-code-quality` for safer code changes and rerun behavior
- `eval-harness` mindset for exact root-cause evidence and post-fix verification
- `search-first` before inventing a new helper or abstraction
- `security-review` when auth, secrets, usage gates, or entitlement paths are touched

## When To Use

- user says ECC Tools burn rate, PR recursion, over-created PRs, usage-limit bypass, or expensive model routing
- the task is an audit or fix in `$PRIMARY_REPOS_ROOT/ECC/skill-creator-app`
- the answer depends on webhook handlers, queue workers, usage reservation, PR creation logic, or paid-gate enforcement

## Workflow

1. Freeze repo scope first:
   - use `$PRIMARY_REPOS_ROOT/ECC/skill-creator-app`
   - check branch and local diff before changing anything
2. Freeze audit mode before tracing:
   - if the user asked for `report only`, `audit only`, `review only`, or explicitly said `do not modify code`, keep the pass read-only until the user changes scope
   - gather evidence with reads, searches, git status/diff, and other non-writing proving commands first
   - do not patch `src/index.ts`, run generators, install dependencies, or stage changes during an audit-only pass
3. Trace ingress before suggesting fixes:
   - inspect webhook entrypoints in `src/index.ts`
   - search every `ANALYSIS_QUEUE.send(...)` or equivalent enqueue
   - map which triggers share a job type
4. Trace the queue consumer and its side effects:
   - inspect `handleAnalysisQueue(...)` or the equivalent worker
   - confirm whether queued analysis always ends in PR creation, file writes, or premium model calls
5. Audit PR multiplication:
   - inspect PR helpers and branch naming
   - check dedupe, branch skip logic, synchronize-event handling, and reuse of existing PRs
   - treat app-generated branches such as `ecc-tools/*` or timestamped branches as red-flag evidence paths
6. Audit usage and billing truth:
   - inspect rate-limit check and increment paths
   - if quota is checked before enqueue but incremented only in the worker, mark it as a real race
   - separate overrun risk, customer billing impact, and entitlement truth
7. Audit model routing:
   - inspect analyzer `fastMode` or equivalent flags, free-vs-paid tier branching, and actual provider/model calls
   - confirm whether free queued work can still hit Anthropic or another premium path when keys exist
8. Audit rerun safety and file updates:
   - inspect file update helpers for existing-file `sha` handling or equivalent optimistic concurrency
   - if reruns can spend analysis cost and then fail on PR or file creation, mark it as burn-with-broken-output
9. Fix in priority order only if the user asked for code changes:
   - stop automatic PR multiplication first
   - stop quota bypass second
   - stop premium leakage third
   - then close rerun/update safety gaps and missing entitlement gates
10. Answer status interrupts before more tracing:
   - if the user asks `did you do it?`, `are you working?`, or the session is near the tool budget, reply from the current verified repo state before more searching
   - lead with whether root causes are `found`, fixes are `changed locally`, `verified locally`, `pushed`, or still `blocked`
   - if the asked burn path is still unresolved, say that before side findings or lower-priority issues
11. Verify with the smallest proving commands:
   - rerun only the focused tests or typecheck that cover changed paths
   - report `changed locally`, `verified locally`, `pushed`, `deployed`, or `blocked` exactly

## High-Signal Failure Patterns

### 1. One queue type for all triggers
If pushes, PR syncs, and manual audits all enqueue the same analyze job and the worker always calls the PR-creation path, analysis equals PR spam.

### 2. Post-enqueue usage increment
If usage is reserved only inside the worker, concurrent requests can all pass the front-door check and exceed quotas.

### 3. Free tier on premium model path
If free queued jobs still set `fastMode: false` or equivalent while premium provider keys exist, free users can burn premium spend.

### 4. App-generated branches re-entering the webhook
If `pull_request.synchronize` or similar runs on `ecc-tools/*` branches, the app can analyze its own output and recurse.

### 5. Update-without-sha reruns
If generated files are updated without passing the existing file `sha`, reruns can fail after the expensive work already happened.

## Pitfalls

- do not start with broad repo wandering, settle webhook -> queue -> worker path first
- do not mix customer billing inference with code-backed product truth
- do not mutate the repo during an audit-only or `do not modify code` pass
- do not claim burn is fixed until the narrow proving command was rerun
- do not push or deploy unless the user asked
- do not ignore existing local changes in the repo, work around them or stop if they conflict
- do not keep tracing lower-priority repo paths after a budget warning or status interrupt when the main root-cause state is already known

## Verification

- root causes cite exact file paths and code areas
- fixes are ordered by burn impact, not code neatness
- proving commands are named
- final status distinguishes local change, verification, push, and deployment
