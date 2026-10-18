# AI Agent Governance, Permissions, and Cost Controls

**Purpose:** Set cautious defaults for AI-assisted engineering. This document is team policy; it does not by itself enforce tool permissions, runtime limits, model capabilities, or provider billing limits.

## Human approval boundaries

Human approval is required before merging pull requests, publishing releases, deploying to shared/production environments, deleting repositories/branches/data/resources, changing security settings or permissions, sending external communications, or running destructive experiments outside an isolated test environment. Agents may prepare changes and evidence, but must not claim approval until the authorized human or system confirms it.

## Least-privilege access

- Prefer read-only access for discovery, planning, and review.
- Grant write access only to the repository and operation needed.
- Never put tokens, passwords, private keys, cookies, or other secrets in prompts, issues, logs, commits, or handover notes.
- Use narrowly scoped credentials and secret stores where needed.
- Do not expose secrets to untrusted pull-request code or execute unreviewed commands with privileged credentials.
- Separate planning/review agents from agents authorized to modify files or call external services.

## Enforced controls versus policy

- **Enforced:** demonstrated by a platform/runtime setting or reproducible test.
- **Policy:** required by this document but not technically enforced.
- **Advisory:** recommendation or estimate that can be overridden.
- **Unverified:** not yet tested or effective setting is unknown.

This repository documents policy. Actual Claude Code permissions, model routing, context limits, token consumption, and stop behavior must be verified in the installed runtime before being called enforced. See the runtime-verification issue in the AI Software Team repository.

## Task budgets and checkpoints

For non-trivial tasks, record one goal, acceptance criteria, a reasonable timebox (start with 25–50 minutes for a focused work block), bounded scope (normally one issue and one small PR), a checkpoint before broad edits, stop conditions, and handover behavior. Stop for unclear scope, missing access, security-sensitive changes, repeated tool failures, unexpected cost, or scope growth. Token budgets are advisory unless the runtime exposes and enforces a measurable limit. Prefer targeted file reads, incremental diffs, and one reviewable lot at a time.

## Model and tool routing

Use the least costly capable tool/model, subject to verified availability. Routine documentation and deterministic edits need less reasoning than multi-file implementation; security boundaries, architecture, migrations, and ambiguous failures require stronger review. Verify current provider capabilities, context sizes, and prices before budgeting. Do not send sensitive content to a provider unless project policy permits it.

## Safe experimentation and completion

Test permission blocks only in disposable repositories or isolated environments with fake data. Record runtime/version, test case, expected and observed behavior, and evidence. Distinguish mocked tests from real runtime tests; a configuration linter does not prove runtime enforcement. Before handover, report changed files, branch/PR, checks actually run, gaps, and one next action. Review this policy quarterly and whenever runtime, permissions, or pricing materially changes.
