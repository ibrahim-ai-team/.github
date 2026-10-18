# Security Baseline and Verification Register

**Last reviewed:** 2026-10-18  
**Purpose:** Track what is known versus what still requires an authenticated settings check. Documentation alone does not enable or prove a GitHub security control.

## Status vocabulary

- **VERIFIED** — directly observed in repository/org metadata or a settings page, with date and evidence.
- **NOT VERIFIED** — not inspected or no adequate evidence was captured.
- **NOT CONFIGURED** — inspected and confirmed absent/disabled.
- **NOT AVAILABLE** — control is unavailable for this repository/plan or inaccessible to the reviewer; explain why.

## Observed repository metadata

| Control / property | Status | Evidence |
| --- | --- | --- |
| `ibrahim-ai-team/.github` visibility | VERIFIED | Repository listing reports public |
| `ibrahim-ai-team/.github` default branch | VERIFIED | Repository listing reports main |
| `ibrahim-ai-team/.github` archived | VERIFIED | Repository listing reports no |
| `ibrahim-ai-team/ai-software-team` visibility | VERIFIED | Repository listing reports public |
| `ibrahim-ai-team/ai-software-team` default branch | VERIFIED | Repository listing reports main |
| `ibrahim-ai-team/ai-software-team` archived | VERIFIED | Repository listing reports no |

## Controls requiring direct verification

These controls remain **NOT VERIFIED** until settings or authoritative API responses are reviewed:

- Branch protection or repository rulesets for `main`
- Pull request review requirements and required status checks
- Restrictions on force pushes and branch deletion
- Secret scanning and push protection
- Dependabot alerts and security updates
- Code scanning / CodeQL coverage
- GitHub Actions permissions and allowed actions policy
- Third-party Actions pinned to full commit SHAs where required
- Private vulnerability reporting availability and configuration
- Organization-level defaults that may override repository settings

## Verification procedure

1. Open each repository's **Settings → Rules** (and branch protection settings where shown); inspect rules applying to `main`.
2. Open **Settings → Security** / **Code security and analysis** and record the state of each available security feature.
3. Open **Settings → Actions → General** and record workflow permissions and action restrictions.
4. Inspect recent pull requests and workflow runs to confirm that required checks actually run and are enforced.
5. Record the repository, control, observed state, date, and evidence link in the relevant issue. Do not include secrets, tokens, private keys, or sensitive values in comments.
6. If a control cannot be inspected with current permissions, keep it **NOT VERIFIED**; do not treat missing access as proof that the control is disabled.

## Completion rule

Issue ORG-06 is complete only when the inventory is reviewed and each repository has a confirmed named owner or an explicit accepted ownership gap. Issue ORG-07 (security defaults) is complete only after applicable controls have been inspected and gaps have owners/actions. Merging this document does not itself configure any security setting.
