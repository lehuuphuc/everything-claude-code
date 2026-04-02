# Changelog

## 2.0.0 - 2026-04-01

### Highlights

- Public ECC 2.0 preview release surface aligned across root package metadata, docs, and release collateral.
- Hermes is now part of the public ECC story via a sanitized setup guide, generated-skills surface, and operator workflow documentation.
- Launch pack added for same-day rollout: release notes, X thread, LinkedIn post, article outline, launch checklist, and short-form video scripts.
- Repo version drift fixed between `package.json`, `package-lock.json`, `.opencode/package.json`, `AGENTS.md`, and `VERSION`.

### New Docs

- `docs/HERMES-SETUP.md` — sanitized public guide for running Hermes with ECC as the operator surface
- `docs/releases/2.0.0-preview/release-notes.md`
- `docs/releases/2.0.0-preview/x-thread.md`
- `docs/releases/2.0.0-preview/linkedin-post.md`
- `docs/releases/2.0.0-preview/video-shorts.md`
- `docs/releases/2.0.0-preview/article-outline.md`
- `docs/releases/2.0.0-preview/launch-checklist.md`

### Positioning

- ECC 2.0 is framed as a cross-harness operating system for agentic work, not only a Claude Code plugin.
- Hermes is positioned as the opinionated operator shell sitting on top of ECC skills, MCPs, hooks, crons, and workflow assets.
- The public preview intentionally ships the documented setup and launch assets first; additional private/local integrations can land incrementally.

## 1.9.0 - 2026-03-20

### Highlights

- Selective install architecture with manifest-driven pipeline and SQLite state store.
- Language coverage expanded to 10+ ecosystems with 6 new agents and language-specific rules.
- Observer reliability hardened with memory throttling, sandbox fixes, and 5-layer loop guard.
- Self-improving skills foundation with skill evolution and session adapters.

### New Agents

- `typescript-reviewer` — TypeScript/JavaScript code review specialist (#647)
- `pytorch-build-resolver` — PyTorch runtime, CUDA, and training error resolution (#549)
- `java-build-resolver` — Maven/Gradle build error resolution (#538)
- `java-reviewer` — Java and Spring Boot code review (#528)
- `kotlin-reviewer` — Kotlin/Android/KMP code review (#309)
- `kotlin-build-resolver` — Kotlin/Gradle build errors (#309)
- `rust-reviewer` — Rust code review (#523)
- `rust-build-resolver` — Rust build error resolution (#523)
- `docs-lookup` — Documentation and API reference research (#529)

### New Skills

- `pytorch-patterns` — PyTorch deep learning workflows (#550)
- `documentation-lookup` — API reference and library doc research (#529)
- `bun-runtime` — Bun runtime patterns (#529)
- `nextjs-turbopack` — Next.js Turbopack workflows (#529)
- `mcp-server-patterns` — MCP server design patterns (#531)
- `data-scraper-agent` — AI-powered public data collection (#503)
- `team-builder` — Team composition skill (#501)
- `ai-regression-testing` — AI regression test workflows (#433)
- `claude-devfleet` — Multi-agent orchestration (#505)
- `blueprint` — Multi-session construction planning
- `everything-claude-code` — Self-referential ECC skill (#335)
- `prompt-optimizer` — Prompt optimization skill (#418)
- 8 Evos operational domain skills (#290)
- 3 Laravel skills (#420)
- VideoDB skills (#301)

### New Commands

- `/docs` — Documentation lookup (#530)
- `/aside` — Side conversation (#407)
- `/prompt-optimize` — Prompt optimization (#418)
- `/resume-session`, `/save-session` — Session management
- `learn-eval` improvements with checklist-based holistic verdict

### New Rules

- Java language rules (#645)
- PHP rule pack (#389)
- Perl language rules and skills (patterns, security, testing)
- Kotlin/Android/KMP rules (#309)
- C++ language support (#539)
- Rust language support (#523)

### Infrastructure

- Selective install architecture with manifest resolution (`install-plan.js`, `install-apply.js`) (#509, #512)
- SQLite state store with query CLI for tracking installed components (#510)
- Session adapters for structured session recording (#511)
- Skill evolution foundation for self-improving skills (#514)
- Orchestration harness with deterministic scoring (#524)
- Catalog count enforcement in CI (#525)
- Install manifest validation for all 109 skills (#537)
- PowerShell installer wrapper (#532)
- Antigravity IDE support via `--target antigravity` flag (#332)
- Codex CLI customization scripts (#336)

### Bug Fixes

- Resolved 19 CI test failures across 6 files (#519)
- Fixed 8 test failures in install pipeline, orchestrator, and repair (#564)
- Observer memory explosion with throttling, re-entrancy guard, and tail sampling (#536)
- Observer sandbox access fix for Haiku invocation (#661)
- Worktree project ID mismatch fix (#665)
- Observer lazy-start logic (#508)
- Observer 5-layer loop prevention guard (#399)
- Hook portability and Windows .cmd support
- Biome hook optimization — eliminated npx overhead (#359)
- InsAIts security hook made opt-in (#370)
- Windows spawnSync export fix (#431)
- UTF-8 encoding fix for instinct CLI (#353)
- Secret scrubbing in hooks (#348)

### Translations

- Korean (ko-KR) translation — README, agents, commands, skills, rules (#392)
- Chinese (zh-CN) documentation sync (#428)

### Credits

- @ymdvsymd — observer sandbox and worktree fixes
- @pythonstrup — biome hook optimization
- @Nomadu27 — InsAIts security hook
- @hahmee — Korean translation
- @zdocapp — Chinese translation sync
- @cookiee339 — Kotlin ecosystem
- @pangerlkr — CI workflow fixes
- @0xrohitgarg — VideoDB skills
- @nocodemf — Evos operational skills
- @swarnika-cmd — community contributions

## 1.8.0 - 2026-03-04

### Highlights

- Harness-first release focused on reliability, eval discipline, and autonomous loop operations.
- Hook runtime now supports profile-based control and targeted hook disabling.
- NanoClaw v2 adds model routing, skill hot-load, branching, search, compaction, export, and metrics.

### Core

- Added new commands: `/harness-audit`, `/loop-start`, `/loop-status`, `/quality-gate`, `/model-route`.
- Added new skills:
  - `agent-harness-construction`
  - `agentic-engineering`
  - `ralphinho-rfc-pipeline`
  - `ai-first-engineering`
  - `enterprise-agent-ops`
  - `nanoclaw-repl`
  - `continuous-agent-loop`
- Added new agents:
  - `harness-optimizer`
  - `loop-operator`

### Hook Reliability

- Fixed SessionStart root resolution with robust fallback search.
- Moved session summary persistence to `Stop` where transcript payload is available.
- Added quality-gate and cost-tracker hooks.
- Replaced fragile inline hook one-liners with dedicated script files.
- Added `ECC_HOOK_PROFILE` and `ECC_DISABLED_HOOKS` controls.

### Cross-Platform

- Improved Windows-safe path handling in doc warning logic.
- Hardened observer loop behavior to avoid non-interactive hangs.

### Notes

- `autonomous-loops` is kept as a compatibility alias for one release; `continuous-agent-loop` is the canonical name.

### Credits

- inspired by [zarazhangrui](https://github.com/zarazhangrui)
- homunculus-inspired by [humanplane](https://github.com/humanplane)
