---
name: content-crosspost-ops
description: Evidence-first crossposting workflow for Hermes. Use when adapting posts, threads, demos, videos, or articles across requested social destinations while keeping per-platform copy distinct and verified.
metadata:
  hermes:
    tags: [generated, content, crosspost, workflow, verification]
---

# Content Crosspost Ops

Use this when the user wants Hermes to crosspost or repurpose content across multiple platforms, especially from Telegram-driven publishing requests.

## Skill Stack

Pull these imported skills into the workflow when relevant:
- `content-engine` for platform-native rewrites
- `crosspost` for sequencing and destination-specific adaptation
- `article-writing` when the source asset is long-form
- `video-editing` or `fal-ai-media` when the post should lead with a clip, frame, or visual
- `continuous-agent-loop` when the task spans capability checks, multi-platform execution, and verification
- `search-first` before claiming a platform or API supports a format
- `eval-harness` mindset for publish verification and status reporting

## When To Use

- user says `crosspost`, `post everywhere`, `put this on linkedin too`, or similar
- the source asset is an X post/thread, quote tweet, article, demo video, screenshot, or YouTube post
- the destination is a community thread or showcase channel like Discord's `built-with-claude`, or another destination whose live support must be checked first
- the user asks whether a new destination or post type is supported

## Support Source Of Truth

Treat these live sources as authoritative for destination support:
- `/Users/affoon/.hermes/workspace/content/postbridge_publish.py`
- `/Users/affoon/.hermes/workspace/content/crosspost-verification-latest.md`

Examples in this skill are destination patterns, not a promise that every destination is live right now. If a destination has no current wrapper path or no recent verified publish record, report `unverified capability` or `blocked by unsupported capability` until checked.

## Capability Matrix

Resolve these as separate questions before you answer or execute:
- is the destination itself currently publishable or only `unverified capability`
- does the asked transport support it right now, for example PostBridge
- does another live path exist, such as browser publish or a different verified API
- what is the active blocker: unsupported transport, unsupported destination, auth, MFA, missing asset, or approval

Do not flatten these into one label. `PostBridge unsupported` can still mean `browser path available`, and `browser blocked on auth` does not mean the destination is fully unsupported.

## Workflow

1. Read the real source asset and any destination rules first. Do not draft from memory.
   - if the user pasted thread requirements, comply with those requirements before drafting
2. If the request depends on platform capability, API support, or quota behavior, verify it before answering.
   - if the user asks whether PostBridge can handle a destination or format, inspect the real wrapper, configs, or recent publish logs before promising support
   - treat `/Users/affoon/.hermes/workspace/content/postbridge_publish.py` plus recent verification records as the source of truth for current support
   - separate the destination question from the transport question, and answer both
   - if there is no current wrapper path or recent proof, report `unverified capability` before drafting
   - if PostBridge is unsupported but a browser path exists, say `PostBridge unsupported, browser path available` instead of flattening the whole destination to `unsupported`
   - if the destination itself is unsupported, say `blocked by unsupported capability` and give the next viable path
   - if the task started as a support question or `did you do it?`, settle that capability or verification answer before drafting or scheduling other destinations
3. Extract one core idea and a few specifics. Split multiple ideas into separate posts.
4. Write native variants instead of reusing the same copy:
   - X: fast hook, minimal framing
   - LinkedIn: strong first line, short paragraphs, explicit lesson or takeaway
   - Threads, Bluesky, or other short-form social destinations: shorter, conversational, clearly distinct wording
   - YouTube Community or other media-led destinations: lead with the result or takeaway, keep it media-friendly
5. Prefer native media when the user wants engagement:
   - for quote tweets, articles, or external links, prefer screenshots or media over a bare outbound link when the platform rewards native assets
   - if the user says the demo itself should lead, use the video or a frame from it instead of a generic screenshot
   - for community showcase threads, prefer the strongest demo clip or screenshot pair the user explicitly pointed to
6. Use link placement intentionally:
   - put external links in comments or replies when engagement is the goal and the platform supports it
   - otherwise use a platform-native CTA such as `comment for link` only when it matches the user's instruction
7. Resolve account and auth blockers early for browser-only destinations:
   - for Discord or other browser-only community shares, verify the active account and whether the destination is reachable before spending more turns on extra asset hunting or copy polish
   - verify the active account before typing into a community or social composer
   - if login is blocked by MFA or a missing verification code, use the checked-in helper path instead of ad hoc inline scripting and do at most one focused resend plus one fresh helper check
   - if that still returns no matching code, stop and report `blocked on missing MFA code`
8. Execute in order:
   - post the primary platform first
   - stagger secondary destinations when requested, defaulting to 4 hours apart unless the user overrides it
   - prefer PostBridge for supported platforms, browser flows only when required
   - if the asked transport is unavailable but another approved live path exists, say that explicitly and take that path next instead of doing unrelated side work
   - if the explicitly asked destination is unsupported or still unverified, report that exact state before moving to any secondary destination, and only continue with other requested platforms when the user asked for a multi-destination publish or approved the fallback order
9. Verify before claiming completion:
   - capture a returned post ID, URL, API response, or an updated verification log
   - when the user asks `did you do it?`, answer with the exact status for each platform: posted, queued, drafted, uploaded-only, blocked, or awaiting verification
   - when the user interrupts with `are you working?`, answer in one sentence with the exact current step or blocker on the explicitly asked destination before more tool use
   - lead with the explicitly asked destination first, and include the proof or blocker on that destination before mentioning any secondary platform work
   - if the asked destination is still unresolved, say that first instead of leading with successful side work on other platforms
   - record every attempt with `/Users/affoon/.hermes/workspace/content/log_crosspost.py` or `/Users/affoon/.hermes/workspace/content/postbridge_publish.py`
   - if the state is only drafted, uploaded-only, queued, blocked, or pending manual action, report that exact status

## Pitfalls

- do not post identical copy cross-platform
- do not assume platform support without checking
- do not ignore thread rules or platform-specific showcase requirements
- do not call a draft, composer state, or upload step `posted`
- do not keep searching unrelated systems after a login or MFA blocker is already the limiting step
- do not keep refining copy or looking for better assets once auth is the only blocker on a browser-only publish
- do not answer a support question with a guess when the wrapper, logs, or API response can settle it
- do not treat destination examples in this skill as a live support matrix
- do not collapse `transport unsupported` into `destination unsupported` when another live path still exists
- do not hide an unresolved asked destination behind progress on other supported destinations
- do not answer `did you do it?` by leading with successful secondary platforms while the explicitly asked destination is still unresolved
- do not keep scheduling or verifying secondary destinations after a status interrupt while the explicitly asked destination is still unresolved
- do not ignore the user's preference for screenshots or native media over raw links

## Verification

- `/Users/affoon/.hermes/workspace/content/crosspost-verification-latest.md` reflects the latest attempts
- each destination has an ID, URL, or explicit failure reason
- the copy and media logged match what was actually sent
