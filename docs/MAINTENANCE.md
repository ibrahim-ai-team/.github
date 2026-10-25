# Organization Maintenance

**Cadence:** monthly and briefly before sprint planning. **Timebox:** about 30 minutes; create focused follow-up issues rather than expanding the review indefinitely.

This document is the single source of truth for organization-level review cadence; other organization documents should link here rather than restating the schedule.

- [ ] Review organization-level issues for duplicates, stale scope, missing acceptance criteria, blockers, and next actions.
- [ ] Confirm repository inventory, purpose, visibility, default branch, and named owner where known.
- [ ] Check profile and contribution, support, and security links.
- [ ] Review failed organization-level workflows and security findings where applicable.
- [ ] Verify repository settings when permissions allow; otherwise leave them explicitly NOT VERIFIED.
- [ ] Check that the organization Project reflects real status and that closed work has evidence.
- [ ] Link to the owning repository for implementation-specific agent, skill, CI, release, ADR, and handover maintenance.
- [ ] Run `python scripts/check_state_drift.py --impl-repo ../ai-software-team` from a workspace where both repositories are siblings. Investigate any missing/extra state report; if the implementation checkout is absent, record the warning and rerun once available.
- [ ] Record the review date, material risks, and follow-up issue links in an existing issue or Project item; avoid creating duplicate recurring issues.

## Evidence rules

Distinguish VERIFIED, NOT VERIFIED, NOT CONFIGURED, and NOT AVAILABLE. A policy document does not prove a setting is enabled. Do not include secrets or sensitive vulnerability details in public issues.

For agent runtime, permission, validation, and implementation procedures, use the [AI Software Team repository](https://github.com/ibrahim-ai-team/ai-software-team).
