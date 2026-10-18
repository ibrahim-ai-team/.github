# Organization Work and Delivery Workflow

## Source of truth and repository boundaries

- Use issues in this `.github` repository for organization-wide process, governance, onboarding, and shared-policy work.
- Use issues in the relevant implementation repository for product/code changes, agent and skill implementation, tests, and repository-specific defects.
- Link related issues across repositories instead of duplicating the same work.
- Use the organization GitHub Project as the cross-repository view when available. A board is a view of the work, not a replacement for the issues.

## Status meanings

| Status | Meaning |
| --- | --- |
| Backlog | Identified, not yet ready to start. |
| Ready | Scope, acceptance criteria, dependencies, priority, and next action are clear. |
| In Progress | Someone is actively working on it. |
| In Review | A pull request or deliverable is awaiting review. |
| Changes Requested | Review found changes required before acceptance. |
| Blocked | Work cannot proceed; the blocker and owner are recorded. |
| Done | Acceptance criteria are met and evidence is linked in the issue or PR. |

These are workflow statuses, not labels or native GitHub Issue Types. Configure them as Project Status options where supported; do not imply that writing them in an issue body changes the Project field.

## Priority and size

- **P0 — Urgent:** immediate security, data-loss, or service-impacting issue.
- **P1 — Foundation:** required to establish safe and usable team infrastructure.
- **P2 — Important:** valuable improvement after foundation work.
- **P3 — Later:** optional improvement or sustainable maintenance.
- **Size:** XS (tiny), S (small), M (medium), L (large). Split work larger than L.

Priority and size are planning aids, not promises of delivery dates.

## Issue quality

Every actionable issue should state:
1. Problem or opportunity and intended outcome.
2. In-scope and out-of-scope work.
3. Testable acceptance criteria.
4. Priority, size, dependencies, and risks when relevant.
5. Owner or next action.
6. Evidence required before closure.

Never include credentials, tokens, private user data, or vulnerability exploit details in public issues.

## Branch and pull-request workflow

1. Start with an issue for non-trivial work.
2. Create a focused branch; never commit directly to `main`.
3. Keep each PR small enough to review and link it to the issue.
4. Include tests or validation evidence, documentation updates, risks, and rollback notes where applicable.
5. Request review and address feedback.
6. The human maintainer has final approval and merge authority.
7. Close the issue only after the deliverable is merged or otherwise demonstrably accepted. If work is deferred, close it as not planned with a rationale rather than claiming completion.

## Triage and handover

- Review the backlog monthly, and before planning a new sprint.
- Remove duplicates carefully, refresh priorities, identify blocked/stale issues, and ensure each Ready item has a clear next action.
- At session end, record the active issue, branch/PR, verified results, decisions, blockers, and next action in the issue or a linked handover note.
- Never place secrets in handover notes.

## Completion evidence

A closed issue must link to the merged PR, relevant commit, verified settings evidence, or an explicit rationale for a non-implementation outcome. A closed state alone is not proof that the Definition of Done was met.
