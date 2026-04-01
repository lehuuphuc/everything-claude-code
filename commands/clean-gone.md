---
description: Cleans up all git branches marked as [gone] (branches deleted on remote but still exist locally), including removing associated worktrees
---

Clean up stale local branches that have been deleted on the remote.

## Steps

1. Fetch and prune remote tracking refs:
   ```bash
   git fetch --prune
   ```

2. Find branches marked as [gone]:
   ```bash
   git branch -vv | grep ': gone]' | awk '{print $1}'
   ```

3. For each gone branch, remove associated worktrees if any:
   ```bash
   git worktree list
   git worktree remove <path> --force
   ```

4. Delete the gone branches:
   ```bash
   git branch -D <branch-name>
   ```

5. Report what was cleaned up
