---
name: terminal-ops
description: Evidence-first terminal and repo execution workflow for Hermes. Use when fixing CI or build failures, running commands in a repo, applying code changes, or proving what was actually executed, verified, and pushed.
metadata:
  hermes:
    tags: [generated, terminal, coding, ci, repo, workflow, verification]
---

# Terminal Ops

Use this when the user asks Hermes to fix code, resolve CI failures, run terminal commands in a repo, inspect git state, or push verified changes.

## Skill Stack

Pull these imported skills into the workflow when relevant:
- `continuous-agent-loop` for multi-step execution with scope freezes, recovery gates, and progress checkpoints
- `agentic-engineering` for scoped decomposition and explicit done conditions
- `plankton-code-quality` for write-time quality expectations and linter discipline
- `eval-harness` for pass/fail verification after each change
- `search-first` before inventing a new helper, dependency, or abstraction
- `security-review` when secrets, auth, external inputs, or privileged operations are touched

## When To Use

- user says `fix`, `debug`, `run this`, `check the repo`, `push it`, or similar
- the task references CI failures, lint errors, build errors, tests, scripts, or a local repo path
- the answer depends on what a command, diff, branch, or verification step actually shows

## Workflow

1. Resolve the exact working surface first:
   - use the user-provided absolute repo path when given
   - if the target is not a git repo, do not reach for git-only steps
   - prefer `/Users/affoon/GitHub/...` over any iCloud or Documents mirror
2. Inspect before editing:
   - read the failing command, file, test, or CI error first
   - check current branch and local state before changing or pushing anything
   - if the prompt already includes loaded-file markers or a compaction summary, use that evidence instead of re-reading blindly
3. Keep fixes narrow and evidence-led:
   - solve one dominant failure at a time
   - prefer repo-local scripts, package scripts, and checked-in helpers over ad hoc one-liners
   - if a dependency or helper is needed, use `search-first` before writing custom glue
4. Verify after each meaningful change:
   - rerun the smallest command that proves the fix
   - escalate to the broader build, lint, or test only after the local failure is addressed
   - if the same proving command keeps failing with the same signature, freeze the broader loop, reduce scope to the failing unit, and stop repeating the same retry
   - review the diff before any commit or push
5. Push only when the requested state is real:
   - distinguish `changed locally`, `verified locally`, `committed`, and `pushed`
   - if push is requested, use a non-interactive git flow and report the branch and result
6. Report exact status words:
   - drafted, changed locally, verified locally, committed, pushed, blocked, awaiting verification

## Pitfalls

- do not guess the failure from memory when logs or tests can settle it
- do not work in `/Users/affoon/Documents/...` clones when `/Users/affoon/GitHub/...` exists
- do not use destructive git commands or revert unrelated local work
- do not claim `fixed` if the proving command was not rerun
- do not claim `pushed` if the change only exists locally
- do not keep rerunning broad verification after the same unchanged failure, narrow the loop or report the blocker

## Verification

- the response names the proving command or test and its result
- the response names the repo path and branch when git was involved
- any push claim includes the target branch and exact status
