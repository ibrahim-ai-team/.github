# Security Baseline and Verification Register

**Last reviewed:** 2026-10-20  
**Purpose:** Track what is known versus what still requires an authenticated settings check. Documentation alone does not enable or prove a GitHub security control.

## Status vocabulary

- **VERIFIED** — directly observed in repository/org metadata or a settings page, with date and evidence.
- **NOT VERIFIED** — not inspected or no adequate evidence was captured.
- **NOT CONFIGURED** — inspected and confirmed absent/disabled.
- **NOT AVAILABLE** — control is unavailable for this repository/plan or inaccessible to the reviewer; explain why.

## Observed repository metadata

| Control / property | Status | Evidence |
| --- | --- | --- |
| `ibrahim-ai-team/.github` visibility | VERIFIED | GitHub repository metadata reports public |
| `ibrahim-ai-team/.github` default branch | VERIFIED | GitHub repository metadata reports `main` |
| `ibrahim-ai-team/.github` archived | VERIFIED | GitHub repository metadata reports false |
| `ibrahim-ai-team/ai-software-team` visibility | VERIFIED | Connected repository listing reports public |
| `ibrahim-ai-team/ai-software-team` default branch | VERIFIED | Connected repository listing reports `main` |
| `ibrahim-ai-team/ai-software-team` archived | VERIFIED | Connected repository listing reports false |
| Repositories visible in connected organization listing | VERIFIED (snapshot) | Listing returned `.github` and `ai-software-team`; this is a point-in-time connected-account view, not proof that no other repositories exist |

## Checks performed on 2026-10-18

The 2026-10-20 inspection below supersedes the NOT VERIFIED results here for `.github` branch protection and rulesets.

- A read of the repository rulesets endpoint returned an empty list in the connected view. This does **not** prove that no inherited organization rules or other enforcement mechanisms apply.
- The branch-protection endpoint for `main` returned HTTP 403 (Resource not accessible by integration). Branch protection, required reviews, required checks, and force-push/deletion restrictions therefore remain **NOT VERIFIED**.
- The available repository tree contains no local GitHub Actions workflow files. This does not verify organization-wide Actions policy or settings.
- No credentials or obvious secrets were identified during the limited file-content review. This was not a comprehensive secret scan and is not a security guarantee.
- The public repository has no `LICENSE` on the reviewed default-branch snapshot; the proposed branch adds an MIT license for the shared documentation and templates. Review the license in the pull request before merge.

## `ibrahim-ai-team/.github` settings inspected on 2026-10-20

Read with an admin-scoped integration token through the GitHub REST API. No settings were changed.

| Control | Status | Evidence |
| --- | --- | --- |
| Branch protection on `main` | NOT CONFIGURED | `GET /branches/main/protection` → 404 "Branch not protected"; `GET /branches/main` reports `protected: false` |
| Rulesets, including inherited organization rulesets | NOT CONFIGURED | `GET /rulesets?includes_parents=true` → `[]`; `GET /rules/branches/main` (all active rules for the branch) → `[]` |
| Required pull request reviews and status checks | NOT CONFIGURED | No protection or ruleset applies to `main` (above) |
| Force-push and branch-deletion restrictions | NOT CONFIGURED | No protection or ruleset applies to `main` (above) |
| Secret scanning | NOT CONFIGURED | `security_and_analysis.secret_scanning.status: disabled` |
| Secret scanning push protection | NOT CONFIGURED | `security_and_analysis.secret_scanning_push_protection.status: disabled` |
| Dependabot security updates | NOT CONFIGURED | `security_and_analysis.dependabot_security_updates.status: disabled` |
| Dependabot alerts | NOT VERIFIED | `GET /vulnerability-alerts` was blocked for the reviewing integration (403) |
| Code scanning default setup | NOT CONFIGURED | `GET /code-scanning/default-setup` → `state: not-configured`; the repository has no analyzable code today |
| Private vulnerability reporting | NOT CONFIGURED | `GET /private-vulnerability-reporting` → `enabled: false` |
| GitHub Actions permissions and allowed-actions policy | NOT VERIFIED | `GET /actions/permissions` was blocked for the reviewing integration (403) |
| GitHub Actions workflows | VERIFIED | `GET /actions/workflows` → `total_count: 0`; no workflows exist, so action pinning does not apply yet |
| Repository collaborators | VERIFIED | One collaborator, `IbrhimGhorafi`, with the `admin` role |

### Gaps and proposed actions

Each item needs an organization owner decision in **Settings**; documentation does not change them.

1. **Protect `main` with a ruleset.** Block force pushes and deletion, and require changes to go through a pull request. With a single admin, requiring an approving review would block every merge; either set required approvals to 0 or give the admin a bypass, until a second maintainer exists.
2. **Enable secret scanning and push protection.** Both are free for public repositories.
3. **Enable private vulnerability reporting.** [SECURITY.md](../SECURITY.md) names it as the first reporting route. Until it is enabled, reporters fall through to the second route (contacting the owner).
4. **Enable Dependabot alerts**, and record their state once it can be read.
5. **Revisit code scanning and Actions policy** when the repository first gains a workflow or code.

## Controls still requiring direct verification

These remain **NOT VERIFIED** until settings or authoritative API responses are reviewed:

- Every security control for `ibrahim-ai-team/ai-software-team`. Its settings were not readable from the 2026-10-20 session, and its code-level controls are owned and documented in that repository.
- Dependabot alerts and GitHub Actions policy for `ibrahim-ai-team/.github` (see above).
- Organization-level defaults that apply to new repositories, and organization Actions policy.

## Verification procedure

1. Open each repository's **Settings → Rules** (and branch protection settings where shown); inspect rules applying to `main`.
2. Open **Settings → Security** / **Code security and analysis** and record the state of each available security feature.
3. Open **Settings → Actions → General** and record workflow permissions and action restrictions.
4. Inspect recent pull requests and workflow runs to confirm that required checks actually run and are enforced.
5. Record the repository, control, observed state, date, and evidence link in the relevant issue. Do not include secrets, tokens, private keys, or sensitive values in comments.
6. If a control cannot be inspected with current permissions, keep it **NOT VERIFIED**; do not treat missing access as proof that the control is disabled.

## Completion rule

Issue #6 is complete only when the inventory is reviewed and each repository has a confirmed named owner or an explicit accepted ownership gap. Issue #7 is complete only after applicable controls have been inspected and gaps have owners/actions. Merging this document does not itself configure any security setting.
