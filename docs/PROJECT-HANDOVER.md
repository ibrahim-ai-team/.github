# Project State and Session Handover

Use this short note when work pauses, a session ends, an agent fails, or a task is blocked. Keep GitHub Issues and PRs as the durable source of truth; this note is a compact pointer, not a duplicate history.

## Template

```markdown
# Handover — YYYY-MM-DD
- **Project/repository:** owner/repo
- **Goal:** one sentence
- **Active issue:** #123 (link)
- **Current branch/PR:** branch name and PR link, or None
- **Status:** In Progress / In Review / Blocked
- **Completed:** concise bullets with issue/PR/commit links
- **Validation evidence:** checks run and actual result; link logs where safe
- **Decisions:** accepted decisions with ADR/issue links
- **Assumptions / unverified:** list explicitly; do not present as facts
- **Blockers / needed decision:** who or what is needed
- **Next action:** one concrete action
- **Safety notes:** relevant constraints, never secrets or sensitive data
```

## Rules

- Keep the handover short enough to read on a phone; link to issues, PRs, commits, and docs instead of pasting long histories.
- Record exact repository, branch, issue, and PR identifiers so work can be resumed without guessing.
- Separate **verified**, **assumed**, and **not verified** information.
- State which commands/checks were actually run and their outcomes. Do not write "tests pass" if they were not run.
- Do not include access tokens, credentials, private keys, cookies, personal data, production records, or private vulnerability details.
- Do not treat a local uncommitted change as safely handed over; commit it to a reviewable branch or describe that it remains uncommitted and where it exists.
- If blocked, name the blocker, what was attempted, and the next safe action. Do not repeat destructive or costly actions blindly.
- The next session should first inspect the linked issue and branch/PR state, then verify the current repository state before changing anything.

## Handover checklist

- [ ] Active issue and current branch/PR are linked.
- [ ] Completed work is backed by commits or other observable evidence.
- [ ] Validation results are accurate.
- [ ] Decisions and unresolved assumptions are distinguished.
- [ ] One next action and any blocker are clear.
- [ ] No secrets or private data are included.
