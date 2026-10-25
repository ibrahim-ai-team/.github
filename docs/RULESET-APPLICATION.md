# Applying the Main Branch Ruleset

**Scope:** `ibrahim-ai-team/.github`, branch `main`.

**Authorization boundary:** This is procedural guidance, not authorization to change repository settings. Obtain explicit maintainer authorization before applying the ruleset or changing any live setting.

## Step 0 — Resolve the single-admin approval deadlock

The ruleset requires one approving review, while the recorded baseline identified only one repository administrator. Before applying it, either add a second trusted, qualified reviewer/admin and verify their access, or obtain explicit authorization for a temporary `required_approving_review_count: 0` exception. The exception must have a documented reason, authorizer, expiry date, and restoration plan. If neither option is authorized, stop.

## 1. Verify required status-check names

The intended workflow job IDs are `yaml-lint`, `markdown-lint`, and `protection-check`. Verify the exact job IDs and the check names reported by a successful GitHub Actions run before import:

```sh
grep -nE '^  (yaml-lint|markdown-lint|protection-check):|^    name:' .github/workflows/ci.yml
cat .github/rulesets/main-protection.json
```

The JSON file is a configuration input, not proof that the live checks exist or are required. Do not import if any required context is missing, renamed, or unverified.

## 2. Import through the GitHub UI

1. Open the repository and go to **Settings → Rules → Rulesets**.
2. Select **New ruleset → Import a ruleset** (labels may vary).
3. Import `.github/rulesets/main-protection.json`, downloading it first if needed.
4. Verify target `refs/heads/main`, enforcement, required checks, review count, linear history, force-push restriction, and deletion restriction.
5. Apply only after the Step 0 decision is authorized.
6. Save and reopen the ruleset page to inspect the resulting live configuration.

## 3. Import through GitHub CLI

From a local checkout, first authenticate and inspect existing rulesets to avoid duplicates:

```sh
gh auth status
gh api repos/ibrahim-ai-team/.github/rulesets --jq '.[] | {id, name, enforcement}'
```

If the intended ruleset does not exist and application is authorized:

```sh
gh api --method POST repos/ibrahim-ai-team/.github/rulesets --input .github/rulesets/main-protection.json
```

This creates a ruleset; it does not update an existing one. Record the returned ID. If permissions are insufficient, stop and ask an authorized administrator. Never place credentials in the JSON file or command history.

## 4. Verify live configuration and behavior

```sh
gh api repos/ibrahim-ai-team/.github/rulesets --jq '.[] | {id, name, target, enforcement, source}'
gh api repos/ibrahim-ai-team/.github/rulesets/RULESET_ID
gh api repos/ibrahim-ai-team/.github/rules/branches/main
scripts/verify_repo_hardening.sh
```

Replace `RULESET_ID` with the actual ID. Verify target, enforcement, required contexts, review count, and other rule types. Then open a harmless throwaway PR against `main`: confirm checks run under the required names, failing/pending checks block merge, the approval requirement behaves as intended, and protections cannot be bypassed. Close the test PR without merging if no longer needed. Do not perform a test that requires an unauthorized setting change or risky merge; record that behavior as NOT VERIFIED instead.

## 5. If a required check name changes

1. Inspect `.github/workflows/ci.yml` and identify the changed job ID.
2. Run the workflow and inspect the check names GitHub reports.
3. Update the corresponding `required_status_checks[].context` in `.github/rulesets/main-protection.json`.
4. Validate JSON and run applicable CI checks.
5. Obtain explicit authorization before updating the live ruleset.
6. Update the live ruleset through the UI or the appropriate authenticated API operation, then verify it and test a disposable PR.

Do not remove a required check merely because its name is stale; establish and approve a replacement first.

## Evidence and completion

Record the date, ruleset ID, enforcement state, required-check names, approval count, and verification evidence in the relevant maintenance record or issue. Mark a control VERIFIED only after observing its live state and relevant behavior. This document does not authorize settings changes or establish that any control is currently enabled.
