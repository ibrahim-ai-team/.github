#!/usr/bin/env bash
# Exit codes: 0 = PASS or intentional CI SKIPPED; 1 = live controls failed;
# 2 = local prerequisites unavailable or unauthenticated. SKIPPED means live
# controls were not verified, not that they passed.
set -u

REPO="${REPO:-ibrahim-ai-team/.github}"
CI_MODE=0
if [[ "${1:-}" == "--ci" ]]; then CI_MODE=1; fi

warn_ci_or_exit() {
  local message="$1"
  if [[ "$CI_MODE" -eq 1 ]]; then
    printf 'WARN: %s; skipping live settings checks in CI mode.\n' "$message"
    printf 'RESULT: SKIPPED — live controls NOT verified (reason: %s)\n' "$message"
    exit 0
  fi
  printf 'ERROR: %s\n' "$message" >&2
  printf 'RESULT: SKIPPED (reason: %s)\n' "$message"
  exit 2
}

if ! command -v gh >/dev/null 2>&1; then
  warn_ci_or_exit "GitHub CLI (gh) is not installed"
fi
if ! gh auth status >/dev/null 2>&1; then
  warn_ci_or_exit "gh is not authenticated; run 'gh auth login' and retry"
fi

failures=0
pass() { printf 'PASS: %s\n' "$1"; }
fail() {
  printf 'FAIL: %s\n' "$1"
  printf '  How to fix: %s\n' "$2"
  failures=$((failures + 1))
}

rules="$(gh api "repos/$REPO/rules/branches/main" 2>/dev/null)" || rules=""
if [[ -n "$rules" ]] && printf '%s' "$rules" | grep -q '"type"[[:space:]]*:[[:space:]]*"pull_request"' &&
   printf '%s' "$rules" | grep -q '"type"[[:space:]]*:[[:space:]]*"required_status_checks"'; then
  pass "main protection: pull request and required status-check rules are active"
else
  fail "main protection" "Settings → Rules → Rulesets: create/activate main-protection.json targeting refs/heads/main; require PRs and CI status checks."
fi

if [[ -n "$rules" ]] && printf '%s' "$rules" | grep -q '"type"[[:space:]]*:[[:space:]]*"non_fast_forward"' &&
   printf '%s' "$rules" | grep -q '"type"[[:space:]]*:[[:space:]]*"deletion"'; then
  pass "main force-push and deletion restrictions"
else
  fail "main force-push/deletion restrictions" "Settings → Rules → Rulesets: enable Block force pushes and Restrict deletions (rule types non_fast_forward and deletion)."
fi

security="$(gh api "repos/$REPO" --jq '.security_and_analysis.secret_scanning.status // "disabled"' 2>/dev/null)" || security="api-error"
if [[ "$security" == "enabled" ]]; then pass "secret scanning"; else fail "secret scanning (current: $security)" "Settings → Security → Code security: enable Secret scanning."; fi

push_protection="$(gh api "repos/$REPO" --jq '.security_and_analysis.secret_scanning_push_protection.status // "disabled"' 2>/dev/null)" || push_protection="api-error"
if [[ "$push_protection" == "enabled" ]]; then pass "secret scanning push protection"; else fail "secret scanning push protection (current: $push_protection)" "Settings → Security → Code security: enable Secret scanning push protection."; fi

dependabot="$(gh api "repos/$REPO" --jq '.security_and_analysis.dependabot_security_updates.status // "disabled"' 2>/dev/null)" || dependabot="api-error"
if [[ "$dependabot" == "enabled" ]]; then pass "Dependabot security updates"; else fail "Dependabot security updates (current: $dependabot)" "Settings → Security → Code security: enable Dependabot security updates. .github/dependabot.yml configures version updates only."; fi

if [[ "$failures" -gt 0 ]]; then
  printf 'RESULT: FAIL (%s control(s) failed)\n' "$failures"
  exit 1
fi
printf 'RESULT: PASS (all checked controls are active)\n'
