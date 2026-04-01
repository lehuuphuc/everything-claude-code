---
description: Get help with the hookify system
---

Display comprehensive hookify documentation.

## Hook System Overview

Hookify creates rule files that integrate with Claude Code's hook system to prevent unwanted behaviors.

### Event Types
- **bash**: Triggers on Bash tool use — match command patterns
- **file**: Triggers on Write/Edit tool use — match file paths
- **stop**: Triggers when session ends — final checks
- **prompt**: Triggers on user message submission — match input patterns
- **all**: Triggers on all events

### Rule File Format
Files are stored as `.claude/hookify.{name}.local.md`:

```yaml
---
name: descriptive-name
enabled: true
event: bash|file|stop|prompt|all
action: block|warn
pattern: "regex pattern to match"
---
Message to display when rule triggers.
Supports multiple lines.
```

### Commands
- `/hookify [description]` — Create new rules (auto-analyzes conversation if no args)
- `/hookify-list` — View all rules
- `/hookify-configure` — Toggle rules on/off

### Pattern Tips
- Use regex syntax (pipes for OR, brackets for groups)
- For bash: match against the full command string
- For file: match against the file path
- Test patterns before deploying
