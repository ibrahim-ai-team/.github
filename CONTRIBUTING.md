# Contributing to Ibrahim AI Team

Thank you for helping improve the organization's repositories and AI-assisted engineering workflows.

## Before starting

1. Check the repository README and open issues to understand the scope.
2. For non-trivial work, open or update an issue before implementation so the goal, acceptance criteria, and dependencies are clear.
3. Confirm that the issue belongs in the repository you are changing. The `.github` repository provides organization profile and community-health guidance; reusable agents and engineering standards live in [ai-software-team](https://github.com/ibrahim-ai-team/ai-software-team).

## Branches and pull requests

- Do not commit directly to `main`; create a focused branch and open a pull request.
- Keep each pull request small and related to one issue or coherent change.
- Describe the motivation, important changes, validation performed, risks, and any follow-up work.
- Link the relevant issue using `Closes #123` only when the pull request fully resolves that issue.
- Require explicit human approval before merge; automated checks do not replace human review. See the [organization delivery workflow](docs/WORKFLOW.md).
- Never force-push shared branches or bypass required review/checks.

## Quality and security

- Run the relevant tests, linters, and validation scripts before requesting review; report anything you could not run.
- Update documentation when behavior, setup, or operating procedures change.
- Never commit passwords, access tokens, private keys, production data, or other secrets. Use fake data in tests.
- Request only the permissions needed for a workflow, and pin third-party GitHub Actions to trusted versions or full commit SHAs according to repository policy.
- Do not claim that a security control or runtime behavior is verified unless there is observable evidence.

## Local checks

Run these from the repository root before opening a pull request:

```sh
python scripts/validate_repo.py
python -m unittest discover -s tests
python scripts/check_state_drift.py --impl-repo ../ai-software-team  # needs a sibling checkout
```

## Review readiness

Fill in every section of the [pull request template](.github/PULL_REQUEST_TEMPLATE.md). If a change is blocked, explain the missing decision or evidence rather than guessing.

Task-claiming and other agent runtime procedures are documented in [ai-software-team](https://github.com/ibrahim-ai-team/ai-software-team); they are intentionally not copied here.

Be respectful, specific, and constructive in discussions.
