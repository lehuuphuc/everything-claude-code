---
description: Create hooks to prevent unwanted behaviors from conversation analysis or explicit instructions
---

Create hook rules to prevent unwanted Claude Code behaviors by analyzing conversation patterns or explicit user instructions.

## Usage

`/hookify [description of behavior to prevent]`

If no arguments provided, analyze the current conversation to find behaviors worth preventing.

## Workflow

### Step 1: Gather Behavior Info
- **With arguments**: Parse the user's description of the unwanted behavior
- **Without arguments**: Use the conversation-analyzer agent to find:
  - Explicit corrections ("no, don't do that", "stop doing X")
  - Frustrated reactions to repeated mistakes
  - Reverted changes
  - Repeated similar issues

### Step 2: Present Findings
Show the user what behaviors were identified and proposed hook rules:
- Behavior description
- Proposed event type (bash/file/stop/prompt/all)
- Proposed pattern/matcher
- Proposed action (block/warn)

### Step 3: Generate Rule Files
For each approved rule, create a file at `.claude/hookify.{name}.local.md`:

```yaml
---
name: rule-name
enabled: true
event: bash|file|stop|prompt|all
action: block|warn
pattern: "regex pattern"
---
Message shown when rule triggers.
```

### Step 4: Confirm
Report created rules and how to manage them (`/hookify-list`, `/hookify-configure`).
