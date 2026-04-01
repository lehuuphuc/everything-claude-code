---
description: List all configured hookify rules
---

Find and display all hookify rules in a formatted table.

## Steps

1. Find all `.claude/hookify.*.local.md` files using Glob
2. Read each file's frontmatter (name, enabled, event, action, pattern)
3. Display as table:

| Rule | Enabled | Event | Pattern | File |
|------|---------|-------|---------|------|

4. Show count and helpful footer about `/hookify-configure` for modifications
