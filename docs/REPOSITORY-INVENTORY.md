# Organization Repository Inventory

**Last reviewed:** 2026-10-24  
**Scope:** Repositories returned by the connected GitHub account's organization-filtered repository listing.

## Catalog

| Repository | Purpose | Visibility | Default branch | Archived | License | Ownership |
| --- | --- | --- | --- | --- | --- | --- |
| [ai-software-team](https://github.com/ibrahim-ai-team/ai-software-team) | Reusable AI agent and skill infrastructure, engineering standards, and delivery workflows. | Public | main | No | MIT | Admin and operational owner NOT VERIFIED |
| [.github](https://github.com/ibrahim-ai-team/.github) | Organization profile, community-health guidance, issue/PR templates, and shared workflow documentation. | Public | main | No | MIT | Sole collaborator and admin: [@IbrhimGhorafi](https://github.com/IbrhimGhorafi) (VERIFIED 2026-10-20). Their acceptance as operational owner is NOT VERIFIED |

## Known gaps

- **Repository description: ACTION REQUIRED (not yet corrected).** GitHub currently has the description "AI-powered software engineering team: reusable agents, skills, automation, and Agile delivery workflows." Change it in **Settings → General → Description** to: "Organization defaults, templates, and governance docs for Ibrahim AI Team — not the implementation repo." This is under 160 characters and clearly distinguishes this repository from `ai-software-team`. Tracked in [issue #26](https://github.com/ibrahim-ai-team/.github/issues/26); issue closure does not prove the setting changed. After changing it, verify with `gh api repos/ibrahim-ai-team/.github --jq .description`.
- **Secondary admin: NOT VERIFIED — to fill after invite acceptance.** Secondary admin: <à remplir>. Record the verified GitHub login and verification date only after confirming the organization role in **Settings → People** or with `gh api orgs/ibrahim-ai-team/memberships/<user> --jq '{state: .state, role: .role}'`.
- **Ownership:** the maintainer should either confirm the named owner for each repository or explicitly accept the gap.

## Maintenance

For each repository, record purpose, visibility, default branch, archived status, named maintainer, lifecycle state, and whether security settings were independently verified. Do not infer security posture from visibility or policy documents. Mark unverified controls as NOT VERIFIED.

## Limitations

On 2026-10-20, a repository search for `org:ibrahim-ai-team` returned the same two repositories, both unarchived, public, and on `main`. Confirm the list against the organization repository page during maintenance. The listing does not show private repositories the reviewing account cannot see. Branch protection and security settings are tracked in [SECURITY-BASELINE.md](SECURITY-BASELINE.md). This is a snapshot and may become stale.
