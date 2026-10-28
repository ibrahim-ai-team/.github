# Ibrahim AI Team — organization defaults

This repository contains the shared GitHub defaults and governance guidance for the **Ibrahim AI Team** organization. It helps contributors find the right repository, open actionable issues, prepare reviewable pull requests, and report security concerns safely.

It is **not** the implementation repository for the AI development team. Reusable agents, skills, Claude instructions, validation scripts, engineering standards, and implementation workflows live in [`ai-software-team`](https://github.com/ibrahim-ai-team/ai-software-team).

## Repository structure

- `.github/ISSUE_TEMPLATE/` — shared Bug, Feature, and Task issue forms, plus the form configuration.
- `.github/PULL_REQUEST_TEMPLATE.md` — shared pull-request description and review prompts.
- `profile/README.md` — the organization's public profile content.
- `docs/WORKFLOW.md` — cross-repository issue, priority, status, review, and completion conventions.
- `docs/REPOSITORY-INVENTORY.md` — repository purposes, visibility, default branches, and known ownership gaps.
- `docs/SECURITY-BASELINE.md` — evidence register for repository metadata and security settings that still require verification.
- `docs/MAINTENANCE.md` — lightweight maintenance checklist.
- `CONTRIBUTING.md`, `SUPPORT.md`, and `SECURITY.md` — contribution, support, and vulnerability-reporting guidance.
- `.github/workflows/ci.yml` — CI checks; `yaml-lint`, `markdown-lint`, and `protection-check` are required by the ruleset, while `state-drift` (also weekly) is informational.
- `.github/rulesets/main-protection.json` — importable branch ruleset for `main`.
- `.github/dependabot.yml` — weekly GitHub Actions version updates.
- `scripts/` — repository validation, cross-repo state-drift check, and live hardening verification; `tests/` covers them.
- `LICENSE` — MIT license for this repository's shared documentation and templates.

## How to use the shared defaults

1. **Choose the owning repository first.** Use [`.github` issues](https://github.com/ibrahim-ai-team/.github/issues) for organization profile, shared defaults, repository inventory, and cross-repository governance. Use [`ai-software-team` issues](https://github.com/ibrahim-ai-team/ai-software-team/issues) for agents, skills, Claude configuration, engineering standards, validation, and implementation workflows.
2. **Create an actionable issue.** Choose the Bug, Feature, or Task form. State the problem or goal, scope, observable acceptance criteria, dependencies, and next action. Do not include secrets or sensitive vulnerability details.
3. **Use metadata accurately.** The issue forms apply a label and the native Issue Type. Maintainers set the native Priority and Effort fields in the issue sidebar; see [the delivery workflow](docs/WORKFLOW.md).
4. **Work on a branch and open a pull request.** Link the issue, summarize the change, include validation evidence, and explain risks. Do not commit directly to `main`.
5. **Keep human review authoritative.** Automated checks do not replace maintainer review. Do not merge until the human maintainer explicitly approves.

## Workflow overview

Issue → scope and acceptance criteria → focused branch → pull request with validation evidence → human review → merge only after explicit approval → close the issue with evidence.

The organization backlog should be reviewed monthly and before sprint planning. Use the existing [maintenance checklist](docs/MAINTENANCE.md) rather than creating duplicate recurring issues. See [Organization Work and Delivery](docs/WORKFLOW.md) for status definitions and repository boundaries.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing changes. Keep pull requests small and reviewable, run applicable checks, document limitations, and never commit credentials, private keys, tokens, or private user data.

## Security

Read [SECURITY.md](SECURITY.md) for private vulnerability-reporting guidance. The [security baseline](docs/SECURITY-BASELINE.md) distinguishes observed facts from settings that remain unverified; documentation alone does not prove a security control is enabled.

## License

The shared documentation and templates in this repository are licensed under the [MIT License](LICENSE).
