# Security Baseline and Verification Register

**Last reviewed:** 2026-10-24  
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
| Repositories visible in connected organization listing | VERIFIED | Listing returned `.github` and `ai-software-team`; this is a point-in-time connected-account view, not proof that no other repositories exist |

## Checks performed on 2026-10-20

The 2026-10-20 inspection below supersedes the NOT VERIFIED results here for `.github` branch protection and rulesets.

- A read of the repository rulesets endpoint returned an empty list in the connected view. This does **not** prove that no inherited organization rules or other enforcement mechanisms apply.
- The branch-protection endpoint for `main` returned HTTP 403 (Resource not accessible by integration). Branch protection, required reviews, required checks, and force-push/deletion restrictions therefore remain **NOT VERIFIED**.
- The available repository tree contains no local GitHub Actions workflow files. This does not verify organization-wide Actions policy or settings.
- No credentials or obvious secrets were identified during the limited file-content review. This was not a comprehensive secret scan and is not a security guarantee.
- The default branch had no `LICENSE` before 2026-10-18; an MIT license for the shared documentation and templates was added in #24 (consistent with `ai-software-team`, which GitHub reports as MIT).

## `ibrahim-ai-team/.github` settings inspected on 2026-10-20

Read with an admin-scoped integration token through the GitHub REST API. No settings were changed.

| Control | Status | Evidence | How to fix |
| --- | --- | --- | --- |
| Branch protection on `main` | NOT CONFIGURED | `GET /branches/main/protection` → 404 "Branch not protected"; `GET /branches/main` reports `protected: false` | Apply `../.github/rulesets/main-protection.json` using the branch-protection steps below. |
| Rulesets, including inherited organization rulesets | NOT CONFIGURED | `GET /rulesets?includes_parents=true` → `[]`; `GET /rules/branches/main` → `[]` | **Settings → Rules → Rulesets → New ruleset → Import a ruleset**; activate a ruleset targeting `refs/heads/main`. |
| Required pull request reviews and status checks | NOT CONFIGURED | No protection or ruleset applied to `main` at inspection time | In the imported ruleset, require pull requests and the `yaml-lint`, `markdown-lint`, and `protection-check` checks; resolve the single-admin approval-count risk before activation. |
| Force-push and branch-deletion restrictions | NOT CONFIGURED | No protection or ruleset applied to `main` at inspection time | In **Settings → Rules → Rulesets**, enable **Block force pushes** and **Restrict deletions**. |
| Secret scanning | NOT CONFIGURED | `security_and_analysis.secret_scanning.status: disabled` | **Settings → Security → Code security → Secret scanning → Enable**. |
| Secret scanning push protection | NOT CONFIGURED | `security_and_analysis.secret_scanning_push_protection.status: disabled` | **Settings → Security → Code security → Push protection → Enable**. |
| Dependabot security updates | NOT CONFIGURED | `security_and_analysis.dependabot_security_updates.status: disabled` | **Settings → Security → Code security → Dependabot security updates → Enable**. |
| Dependabot alerts | NOT VERIFIED | `GET /vulnerability-alerts` was blocked for the reviewing integration (403) | Open **Settings → Security → Code security**, enable **Dependabot alerts**, then verify with the admin CLI/API or settings page. |
| Code scanning default setup | NOT CONFIGURED | `GET /code-scanning/default-setup` → `state: not-configured`; no analyzable code existed at inspection time | Reassess when the repository gains analyzable code; if applicable, open **Settings → Security → Code security → Code scanning** and configure default setup. |
| Private vulnerability reporting | NOT CONFIGURED | `GET /private-vulnerability-reporting` → `enabled: false` | **Settings → Security → Code security → Private vulnerability reporting → Enable**. |
| GitHub Actions permissions and allowed-actions policy | NOT VERIFIED | `GET /actions/permissions` was blocked for the reviewing integration (403) | Use an admin account to inspect **Settings → Actions → General**; set least-privilege workflow permissions and an explicit allowed-actions policy, then record evidence. |
| GitHub Actions workflows | VERIFIED | `GET /actions/workflows` returned a workflow after this PR; baseline inspection on 2026-10-20 had `total_count: 0` | Review the new CI workflow and its permissions as part of this PR; no additional fix required if least privilege remains in place. |
| Repository collaborators | VERIFIED | One collaborator, `IbrhimGhorafi`, with the `admin` role | Add a second trusted owner/admin only after confirming the person's identity and need; follow **Bus factor mitigation** below. |

### Gaps and proposed actions

These controls need action by an organization/repository owner. The prior issue [#26](https://github.com/ibrahim-ai-team/.github/issues/26) is closed, but the settings described here must not be considered fixed until the verification script passes.

1. **Protect `main`.** Apply [`.github/rulesets/main-protection.json`](../.github/rulesets/main-protection.json). It requires a pull request, one approval, CI checks, linear history, and blocks force-push/deletion. There is currently only one verified admin; one required approval can deadlock merges until a second reviewer/admin is added. If you cannot add one now, change the ruleset approval count to 0 temporarily and record that exception.
2. **Enable secret scanning and push protection** using the exact steps below.
3. **Enable private vulnerability reporting.** [SECURITY.md](../SECURITY.md) names it as the first reporting route. Until enabled, reporters fall through to the second route (contacting the owner).
4. **Enable Dependabot alerts and security updates**, then verify both.
5. Revisit code scanning and Actions policy when the repository gains analyzable code or additional workflows.

## How to apply branch protection

### Option A — GitHub UI / ruleset import

1. Open [the `.github` repository](https://github.com/ibrahim-ai-team/.github).
2. Select **Settings → Rules → Rulesets**.
3. Select **New ruleset → Import a ruleset** (the label may appear as **Import ruleset**).
4. Select the file `.github/rulesets/main-protection.json` from the branch/checkout and upload/import it. If the UI does not accept a repository file directly, download that JSON file to your device first, then import the downloaded file.
5. Confirm the target is branch `main` (condition `refs/heads/main`), enforcement is **Active**, pull requests are required, the listed CI status checks match the checks reported by the new workflow, force pushes and deletion are blocked, and linear history is enabled.
6. **Before saving:** one approving review is configured. The inventory currently verifies only one admin. Add a second qualified reviewer/admin first, or change `required_approving_review_count` to `0` temporarily to avoid locking out the sole maintainer.
7. Save the ruleset. Open **Settings → Rules → Rulesets** again and confirm the ruleset appears with **Active** enforcement.

### Option B — GitHub CLI / REST API

Run from a local checkout of this repository after installing and authenticating GitHub CLI:

```sh
gh auth status
gh api --method POST repos/ibrahim-ai-team/.github/rulesets \
  --input .github/rulesets/main-protection.json
```

The API call creates the ruleset; it does not import it into a different repository. Check the response for an ID and active enforcement, then run `scripts/verify_repo_hardening.sh`. If the endpoint returns 403, use an owner/admin account with repository administration permission. Do not put a token in the JSON file or command line.

## How to enable secret scanning and push protection

1. Open [`.github` Settings](https://github.com/ibrahim-ai-team/.github/settings/security_analysis).
2. Select **Security → Code security** (or **Code security and analysis**).
3. Under **Secret scanning**, select **Enable** and confirm.
4. Under **Secret scanning push protection**, select **Enable** and confirm. If GitHub presents the two controls together, explicitly verify both show enabled after saving.
5. Reopen the page and verify both controls remain enabled.
6. Run `scripts/verify_repo_hardening.sh`; the **Secret scanning** and **Push protection** rows must say `PASS`.

If a control is unavailable in the UI, do not mark it enabled. Record the exact UI/API error and the repository plan/visibility, then leave it **NOT AVAILABLE** with that reason.

## How to enable Dependabot security updates

1. Open [`.github` Settings → Code security](https://github.com/ibrahim-ai-team/.github/settings/security_analysis).
2. Find **Dependabot alerts** and enable them first if disabled.
3. Find **Dependabot security updates** and select **Enable**.
4. Confirm the settings page reports enabled, then run `scripts/verify_repo_hardening.sh`.
5. The committed `.github/dependabot.yml` configures weekly GitHub Actions dependency-version updates; it does **not** turn on the separate Dependabot security-updates setting.

## Bus factor mitigation

1. Confirm the person is a trusted maintainer and has an individual GitHub account with appropriate MFA and recovery.
2. In the organization, open **Settings → People → Invite member** (or **People → Members**, then **Add member** depending on the current UI).
3. Invite the person and select the **Owner** role only if they need organization-wide administrative authority. Review least privilege before sending the invitation.
4. Have the invitee accept, then confirm the person appears under **Organization Settings → People** with role **Owner**.
5. Update [`docs/REPOSITORY-INVENTORY.md`](REPOSITORY-INVENTORY.md) with the verified GitHub login and date. Until then, its secondary-admin field remains **NOT VERIFIED**.

CLI alternative (run as an organization owner; replace `<user>` with the exact GitHub login):

```sh
gh api --method PUT orgs/ibrahim-ai-team/memberships/<user> -f role=admin
gh api orgs/ibrahim-ai-team/memberships/<user> --jq '{state: .state, role: .role}'
```

This grants organization **admin/owner-level** membership; it is a high-impact action. Use it only after explicitly authorizing that exact user. The first command is not a substitute for the invite/acceptance workflow where required by organization policy.

## Verification script

Run from the repository root:

```sh
chmod +x scripts/verify_repo_hardening.sh
scripts/verify_repo_hardening.sh
```

Each control prints `PASS` or `FAIL` and a `How to fix:` action. The script exits 1 if any control fails and exits 2 if `gh` is unavailable or unauthenticated. CI uses `--ci`, which prints an explicit warning and exits 0 if GitHub CLI/authentication is unavailable; settings failures with working authentication remain visible as failures.

## Verification procedure

1. Open each repository's **Settings → Rules** (and branch protection settings where shown); inspect rules applying to `main`.
2. Open **Settings → Security → Code security** and record the state of each available security feature.
3. Open **Settings → Actions → General** and record workflow permissions and action restrictions.
4. Inspect recent pull requests and workflow runs to confirm required checks actually run and are enforced.
5. Record repository, control, observed state, date, and evidence link in the relevant issue. Never include secrets, tokens, private keys, or sensitive values in comments.
6. If a control cannot be inspected with current permissions, keep it **NOT VERIFIED**; do not treat missing access as proof that it is disabled.

## Completion rule

Issue #6 is complete only when the inventory is reviewed and each repository has a confirmed named owner or an explicit accepted ownership gap. Issue #7 is complete only after applicable controls have been inspected and gaps have owners/actions. A merged document does not configure any setting.
