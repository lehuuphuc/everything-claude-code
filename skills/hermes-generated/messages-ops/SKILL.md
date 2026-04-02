---
name: messages-ops
description: Evidence-first live messaging workflow for Hermes. Use when reading iMessage threads, checking X DMs, pulling recent local MFA codes, or proving which thread or message was actually reviewed.
metadata:
  hermes:
    tags: [generated, messages, imessage, dm, mfa, workflow, verification]
---

# Messages Ops

Use this when the user wants Hermes to read texts or DMs, recover a recent one-time code, inspect a live thread before replying, or prove which message source was checked.

## Skill Stack

Pull these imported skills into the workflow when relevant:
- `continuous-agent-loop` when the task spans source resolution, retrieval, and a follow-up draft or action
- `continuous-learning-v2` when the live message task turns into a cross-session memory or pattern-capture issue
- `search-first` before inventing a new message lookup path or raw database query
- `eval-harness` mindset for exact source attribution and blocked-state reporting

## When To Use

- user says `read my messages`, `check texts`, `look in iMessage`, `check DMs`, or similar
- the task depends on a live local Messages thread, an X DM thread, or a recent code delivered to Messages
- the user asks whether Hermes already checked a specific thread, sender, or service
- the prompt mixes live message retrieval with a likely handoff into `email-ops` or `knowledge-ops`

## Workflow

1. Resolve the source first:
   - iMessage thread
   - recent local code in Messages
   - X DM or another browser-gated message source
   - email or persistent memory handoff
2. For iMessage threads:
   - use `imsg chats` when the chat id is unclear
   - use `imsg history --chat-id <ID> --limit <N>` for the actual read
   - known chat ids can save turns when they match the ask, for example Alejandro=`458` and Haley/Henry=`364`
3. For recent one-time codes from local Messages:
   - use `python3 $HERMES_HOME/scripts/messages_recent_codes.py --limit 8 --minutes 20`
   - add `--query <service>` when the sender or brand is known
   - do not jump to ad hoc `sqlite3`, `python3 -c`, or other inline database reads before the helper path is tried
   - if one focused resend plus one fresh helper check still shows no match, report `blocked on missing MFA code` and stop
4. For X DMs or other browser-gated message sources:
   - use the logged-in browser path first
   - verify the active account before reading or drafting
   - if auth or MFA blocks access, do the focused code-check path once, then report the exact blocker instead of wandering into side work
5. Hand off cleanly when the task is really another workflow:
   - use `email-ops` when the dominant task is mailbox triage, folder moves, replies, or Sent proof
   - use `knowledge-ops` when the user says `openclaw memory`, `not in this session`, or the prompt already provides loaded context plus a memory-retrieval hint
6. Report exact evidence:
   - name the source tool and thread or chat id when possible
   - include sender, service, timestamp window, or blocker
   - use exact status words such as `read`, `drafted`, `blocked`, or `awaiting verification`

## Pitfalls

- do not say `I can't retrieve` when `imsg`, the browser session, or the checked helper script can settle the question
- do not confuse live message retrieval with mailbox work, hand off to `email-ops` when email is the real surface
- do not burn turns on raw database one-liners before the checked helper path for local codes
- do not keep re-reading the current session after the user already pointed to OpenClaw or another persistent store
- do not claim a thread was checked without naming the source tool, thread, or service behind the claim

## Verification

- the response names the source store or tool used
- the response includes a thread id, sender, service, or explicit blocker
- MFA/code checks end with either a concrete match or the exact blocked status
