---
description: Create a git commit
---

Create a single git commit from staged and unstaged changes with an appropriate message.

## Steps

1. Run `git status` (never use `-uall` flag) and `git diff` in parallel to see all changes
2. Run `git log --oneline -5` to match commit message style
3. Analyze changes and draft a concise commit message following conventional commits format: `<type>: <description>`
   - Types: feat, fix, refactor, docs, test, chore, perf, ci
   - Focus on "why" not "what"
4. Stage relevant files (prefer specific files over `git add -A`)
5. Create the commit using a HEREDOC for the message:
   ```bash
   git commit -m "$(cat <<'EOF'
   type: description
   EOF
   )"
   ```
6. Run `git status` to verify success

**Rules:**
- Never skip hooks (--no-verify) or bypass signing
- Never amend existing commits unless explicitly asked
- Do not commit files that likely contain secrets (.env, credentials.json)
- If pre-commit hook fails, fix the issue and create a NEW commit
