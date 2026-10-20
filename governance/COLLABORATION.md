# Collaboration between chats and contributors

GitHub is the shared coordination surface. Chats cannot see another chat's unsaved edits or messages. These rules reduce collisions; they are not a distributed lock or an enforced branch-protection setting.

1. Fetch current main, open PRs and work-board.json before starting. Describe the work item, branch, paths, base SHA and status in the work board or a PR. Claims are advisory; check for conflicting scope.
2. Use a separate branch per work item. Do not make piecemeal structural writes to main. Never force-push main or overwrite a remote file from a stale local copy.
3. Shared agents/workflows belong to the core maintainer scope. Business content work stays in its business folder. Campaign work stays in its campaign folder. Shared registry and migration work need sequential integration.
4. For overlapping work, reuse existing content and agree scope through the shared board/PR. Do not create another role/template merely because a filename differs. Search by responsibility and stable ID first.
5. Before merging, refresh main and compare all changed paths. Preserve unrelated new files. Resolve overlapping content deliberately, rerun checks, then merge against the expected PR head SHA.
6. If main moved after validation, refresh/reconcile and rerun relevant checks. Do not force an outdated migration into place. A PR may remain open until reconciliation is complete.
7. Close or update the work item after merge. Record the merge commit and any follow-up work. Never assume the other chat adopted this protocol until it reads the current repository.

## Suggested split

- Shared system work: core/, scripts/, tests/ and governance/ architecture.
- Erudience content work: businesses/erudience/ knowledge, offers, campaign briefs, approved message strategy and memory.
- Integration implementation: one separate work item per provider, with no credentials committed.

The owner can give both chats this instruction: "Refresh sales-os main. Read AGENTS.md and governance/COLLABORATION.md. Check open PRs and the work board. Reuse existing roles and templates; change only your claimed scope on a branch."
