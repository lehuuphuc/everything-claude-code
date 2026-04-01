---
description: Commit, push, and open a PR
---

Commit all changes, push to remote, and create a pull request in one workflow.

## Steps

1. Run in parallel: `git status`, `git diff`, `git log --oneline -5`, check current branch tracking
2. Stage and commit changes following conventional commit format
3. Create a new branch if on main/master: `git checkout -b <descriptive-branch-name>`
4. Push to remote with `-u` flag: `git push -u origin <branch>`
5. Create PR using gh CLI:
   ```bash
   gh pr create --title "short title" --body "$(cat <<'EOF'
   ## Summary
   <1-3 bullet points>

   ## Test plan
   - [ ] Testing checklist items
   EOF
   )"
   ```
6. Return the PR URL

**Rules:**
- Keep PR title under 70 characters
- Analyze ALL commits in the branch (not just the latest)
- Never force push
- Never skip hooks
