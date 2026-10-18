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

## Pull requests and completion

1. Use a focused branch for non-trivial work; do not commit directly to `main`.
2. Link the issue and explain the change, validation performed, risks, and follow-up work.
3. Request review and resolve feedback before merging.
4. Keep final merge authority with the human maintainer.
5. Close work only when accepted, with a merged PR, commit, verified settings evidence, or a clear not-planned rationale.

## Triage

Review the organization backlog monthly and before sprint planning. Identify duplicates carefully, update stale priorities, record blockers and next actions, and avoid opening repeated issues for the same work. For implementation-specific procedures, use the [AI Software Team repository](https://github.com/ibrahim-ai-team/ai-software-team).
