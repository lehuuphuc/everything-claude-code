---
description: Comprehensive PR review using specialized agents
---

Run a comprehensive, multi-perspective review of a pull request.

## Usage

`/review-pr [PR-number-or-URL] [--focus=comments|tests|errors|types|code|simplify]`

If no PR specified, review the current branch's PR. If no focus specified, run all reviews.

## Steps

1. **Identify the PR**: Use `gh pr view` to get PR details, changed files, and diff
2. **Find project guidelines**: Look for CLAUDE.md, .eslintrc, tsconfig.json, etc.
3. **Launch specialized review agents** (in parallel where possible):

   | Agent | Focus |
   |-------|-------|
   | code-reviewer | Code quality, bugs, security, style guide adherence |
   | comment-analyzer | Comment accuracy, completeness, maintainability |
   | pr-test-analyzer | Test coverage quality and completeness |
   | silent-failure-hunter | Silent failures, inadequate error handling |
   | type-design-analyzer | Type design, invariants, encapsulation |
   | code-simplifier | Code clarity, consistency, maintainability |

4. **Aggregate results**: Collect findings, deduplicate, rank by severity
5. **Report**: Present organized findings grouped by severity (Critical > Important > Advisory)

## Confidence Scoring

Only report issues with confidence ≥ 80:
- **Critical (90-100)**: Bugs, security vulnerabilities, data loss risks
- **Important (80-89)**: Style violations, missing tests, code quality
- **Advisory (<80)**: Suggestions, nice-to-haves (only if explicitly requested)
