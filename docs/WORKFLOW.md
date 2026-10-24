# Organization Work and Delivery

> The canonical state definitions and transition validation are defined in [`models/status.py`](https://github.com/ibrahim-ai-team/ai-software-team/blob/main/models/status.py). This document is a cross-repo summary; if there is a discrepancy, the code is authoritative. The board transition/evidence contract is documented in [`workflows/project-status-transitions.md`](https://github.com/ibrahim-ai-team/ai-software-team/blob/main/workflows/project-status-transitions.md).

This repository owns organization-level community health, shared defaults, cross-repository coordination, and organization governance. It does not own the implementation of agents, skills, code, tests, or runtime behavior.

## Repository boundaries

- **Organization-wide:** organization profile, repository inventory, contribution/support/security reporting guidance, reusable issue/PR defaults, cross-repository delivery conventions, and settings-verification tracking.
- **AI Software Team:** agent/skill implementation, engineering standards, Claude instructions and permissions, validation scripts, CI workflows, and implementation-specific handover/release/ADR procedures.
- **Other repositories:** product-specific implementation and delivery rules.

Keep one authoritative copy of implementation guidance in its owning repository. Link to it rather than copying it here. Use cross-repository issues when one change requires work in both places.

## Issue readiness and delivery

Actionable issues should describe the problem and intended outcome, scope, testable acceptance criteria, priority, dependencies/risks, and evidence required for closure. Do not include credentials, tokens, private data, or public exploit details.

### Canonical board status mapping

The organization board uses the following eight display labels, mapped to the implementation's `TaskStatus` enum. The complete enum and allowed transitions remain authoritative in `models/status.py` and `workflows/project-status-transitions.md`.

- Backlog → `BACKLOG`
- Ready → `READY`
- In Progress → `IN_PROGRESS`
- In Review → `IN_REVIEW`
- Changes Requested → `CHANGES_REQUESTED`
- Approved — Awaiting Human Merge → `APPROVED_AWAITING_HUMAN_MERGE`
- Blocked → `BLOCKED`
- Done → `DONE`

Implementation-only task states: `CLAIMED`, `CANCELLED`. These are intentionally not organization-board labels. Do not infer board status from issue titles, labels, or body text.

Readiness meanings: **Ready** means scope, acceptance criteria, priority, dependencies, and next action are clear. **In Progress** means work is active. **In Review** means a PR or deliverable awaits review. **Blocked** means the blocker and next action are recorded. **Done** requires accepted completion evidence and verified human merge, as defined in the implementation workflow.

Priority uses the organization's native **Priority** issue field: **Urgent** for security, data, or service impact; **High** for foundation work; **Medium** for important work; **Low** for later. Priority is not a delivery-date promise.

## Issue metadata

Each kind of metadata has one home. Don't record the same fact in two places.

| Metadata | Where it lives | Convention |
| --- | --- | --- |
| Kind of work | Native **Issue Type** (Bug, Feature, Task) | The Bug, Feature, and Task forms set it automatically; set it by hand for issues created another way. Issue Types are enabled. `Bug`, `Feature`, and `Task` are VERIFIED as of 2026-10-20: `Feature` on [#15](https://github.com/ibrahim-ai-team/.github/issues/15), `Task` on [#26](https://github.com/ibrahim-ai-team/.github/issues/26), and `Bug` preset by the Bug form in the web UI. |
| Topic | Labels | Use GitHub's default labels: `bug` and `enhancement` (applied by the Bug and Feature forms), `documentation`, `question`, `duplicate`, `invalid`, `wontfix`, `good first issue`, `help wanted`, `accessibility`. These are the only labels on `.github` as of 2026-10-20. Don't add priority, status, or type labels. |
| Priority | Native **Priority** issue field (Urgent, High, Medium, Low) | Meanings are listed above. A maintainer sets it in the issue sidebar while creating the issue or during triage. The issue forms don't ask for it. |
| Effort | Native **Effort** issue field (High, Medium, Low) | Set by a maintainer during triage. |
| Dates | Native **Start date** and **Target date** issue fields | Optional; use them only when a date is committed. |
| Status | Organization Project **Status** field | Use the eight-label mapping above. Don't track status in labels or titles. |

Repositories may add their own labels for work that only concerns them. Add an organization-wide label only if it is needed across repositories, and propose it in a `.github` issue first.

## Pull requests and completion

1. Use a focused branch for non-trivial work; do not commit directly to `main`.
2. Link the issue and explain the change, validation performed, risks, and follow-up work.
3. Request review and resolve feedback before merging.
4. Keep final merge authority with the human maintainer.
5. Close work only when accepted, with a merged PR, commit, verified settings evidence, or a clear not-planned rationale.

## Triage

Review the organization backlog monthly and before sprint planning. Identify duplicates carefully, update stale priorities, record blockers and next actions, and avoid opening repeated issues for the same work. For implementation-specific procedures, use the [AI Software Team repository](https://github.com/ibrahim-ai-team/ai-software-team).
