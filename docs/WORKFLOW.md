# Organization Work and Delivery

This repository owns organization-level community health, shared defaults, cross-repository coordination, and organization governance. It does not own the implementation of agents, skills, code, tests, or runtime behavior.

## Repository boundaries

- **Organization-wide:** organization profile, repository inventory, contribution/support/security reporting guidance, reusable issue/PR defaults, cross-repository delivery conventions, and settings-verification tracking.
- **AI Software Team:** agent/skill implementation, engineering standards, Claude instructions and permissions, validation scripts, CI workflows, and implementation-specific handover/release/ADR procedures.
- **Other repositories:** product-specific implementation and delivery rules.

Keep one authoritative copy of implementation guidance in its owning repository. Link to it rather than copying it here. Use cross-repository issues when one change requires work in both places.

## Issue readiness and delivery

Actionable issues should describe the problem and intended outcome, scope, testable acceptance criteria, priority, dependencies/risks, and evidence required for closure. Do not include credentials, tokens, private data, or public exploit details.

Use the organization Project for a cross-repository view when configured. Project status is a field, not a label or a sentence in an issue body. Suggested meanings:

- **Backlog:** identified, not ready.
- **Ready:** scope, acceptance criteria, priority, dependencies, and next action are clear.
- **In Progress:** actively being worked.
- **In Review:** PR or deliverable awaits review.
- **Blocked:** blocker and next action are recorded.
- **Done:** acceptance criteria are met and evidence is linked.

Suggested priority: **P0** urgent security/data/service impact; **P1** foundation; **P2** important; **P3** later. Priority is not a delivery-date promise.

## Issue metadata

Each kind of metadata has one home. Don't record the same fact in two places.

| Metadata | Where it lives | Convention |
| --- | --- | --- |
| Kind of work | Native **Issue Type** (Bug, Feature, Task) | Set it after the issue is created; issue forms cannot set it. Issue Types are enabled: [#15](https://github.com/ibrahim-ai-team/.github/issues/15) has the `Feature` type (VERIFIED 2026-10-20). The organization's full type list could not be read (API 403), so whether `Bug` and `Task` exist is NOT VERIFIED. |
| Topic | Labels | Use GitHub's default labels: `bug` and `enhancement` (applied by the Bug and Feature forms), `documentation`, `question`, `duplicate`, `invalid`, `wontfix`, `good first issue`, `help wanted`, `accessibility`. These are the only labels on `.github` as of 2026-10-20. Don't add priority, status, or type labels. |
| Priority | Issue form field (P0–P3), and the Project field when configured | Meanings are listed above. |
| Status | Organization Project **Status** field | Values are listed above. Don't track status in labels or titles. |

Repositories may add their own labels for work that only concerns them. Add an organization-wide label only if it is needed across repositories, and propose it in a `.github` issue first.

## Pull requests and completion

1. Use a focused branch for non-trivial work; do not commit directly to `main`.
2. Link the issue and explain the change, validation performed, risks, and follow-up work.
3. Request review and resolve feedback before merging.
4. Keep final merge authority with the human maintainer.
5. Close work only when accepted, with a merged PR, commit, verified settings evidence, or a clear not-planned rationale.

## Triage

Review the organization backlog monthly and before sprint planning. Identify duplicates carefully, update stale priorities, record blockers and next actions, and avoid opening repeated issues for the same work. For implementation-specific procedures, use the [AI Software Team repository](https://github.com/ibrahim-ai-team/ai-software-team).
