# Organization Repository Inventory

**Last reviewed:** 2026-10-20  
**Scope:** Repositories returned by the connected GitHub account's organization-filtered repository listing.

## Catalog

| Repository | Purpose | Visibility | Default branch | Archived | License | Ownership |
| --- | --- | --- | --- | --- | --- | --- |
| [ai-software-team](https://github.com/ibrahim-ai-team/ai-software-team) | Reusable AI agent and skill infrastructure, engineering standards, and delivery workflows. | Public | main | No | MIT | Admin and operational owner NOT VERIFIED |
| [.github](https://github.com/ibrahim-ai-team/.github) | Organization profile, community-health guidance, issue/PR templates, and shared workflow documentation. | Public | main | No | MIT | Sole collaborator and admin: [@IbrhimGhorafi](https://github.com/IbrhimGhorafi) (VERIFIED 2026-10-20). Their acceptance as operational owner is NOT VERIFIED |

## Known gaps

- **`.github` repository description is wrong.** GitHub shows "AI-powered software engineering team: reusable agents, skills, automation, and Agile delivery workflows." That describes `ai-software-team` and contradicts this repository's boundary. Proposed description, which an admin changes in **Settings → General**: "Organization profile, shared issue/PR templates, and community-health and governance docs for Ibrahim AI Team."
- **Ownership:** the maintainer should either confirm the named owner for each repository or explicitly accept the gap.

## Maintenance

For each repository, record purpose, visibility, default branch, archived status, named maintainer, lifecycle state, and whether security settings were independently verified. Do not infer security posture from visibility or policy documents. Mark unverified controls as NOT VERIFIED.

## Limitations

On 2026-10-20, a repository search for `org:ibrahim-ai-team` returned the same two repositories, both unarchived, public, and on `main`. Confirm the list against the organization repository page during maintenance. The listing does not show private repositories the reviewing account cannot see. Branch protection and security settings are tracked in [SECURITY-BASELINE.md](SECURITY-BASELINE.md). This is a snapshot and may become stale.
