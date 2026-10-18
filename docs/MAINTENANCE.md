# Monthly Maintenance Checklist

**Cadence:** once per month and briefly before planning each new sprint. **Owner:** organization maintainer; name a backup if one becomes available. **Timebox:** aim for 30 minutes; create follow-up issues rather than expanding the review indefinitely.

## Backlog and delivery
- [ ] Review stale, duplicate, blocked, and unowned issues.
- [ ] Confirm active issues have a clear next action, priority, and acceptance criteria.
- [ ] Check Project status fields reflect reality; labels/body text do not replace Project fields.
- [ ] Close completed work only with merged/accepted evidence; close deferred work as not planned with rationale.
- [ ] Review sprint scope and split oversized work.

## Repositories and documentation
- [ ] Confirm repository inventory, purpose, default branch, visibility, and owner remain accurate.
- [ ] Check profile, contribution, support, security, workflow, and onboarding links.
- [ ] Check for stale setup commands, dead links, or policies that no longer match runtime behavior.
- [ ] Review the ADR index for decisions that need superseding or revisiting.

## Quality and security
- [ ] Review failed or flaky Actions runs and create focused follow-up issues.
- [ ] Review dependency/security alerts where available.
- [ ] Verify branch rules, secret scanning, Actions permissions, and other settings when access permits; record evidence and leave unknown settings NOT VERIFIED.
- [ ] Ensure no secrets or sensitive details have been added to public issues, commits, logs, or docs.
- [ ] Review third-party workflow/action changes and permissions before adoption.

## AI agent and cost controls
- [ ] Review runtime/provider changes affecting permissions, capabilities, context, or price.
- [ ] Ensure agent experiments remain isolated and use fake data.
- [ ] Review tasks that exceeded time/cost expectations and adjust scope or routing.
- [ ] Confirm human approval remains required for merges, releases, deployments, and destructive operations.

## Handling exceptions
- **Blocked:** keep open, set Project status to Blocked where available, record blocker/owner and next action.
- **Deferred:** reprioritize and document when/why it may be reconsidered.
- **Not planned:** close with a concise rationale; do not label it completed.
- **Repeated failure:** stop retrying blindly, preserve logs without secrets, and open a focused issue.
- **Security concern:** avoid public exploit details; use the private reporting route in [SECURITY.md](../SECURITY.md).

Record the date, reviewer, notable risks, and follow-up issue links in a monthly issue/comment or the organization Project. Avoid duplicate recurring issues when one checklist is enough.
