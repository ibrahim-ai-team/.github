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
- Human maintainers retain final merge authority. Do not assume approval or merge permission from automated checks alone.
- Never force-push shared branches or bypass required review/checks.

## Quality and security

- Run the relevant tests, linters, and validation scripts before requesting review; report anything you could not run.
- Update documentation when behavior, setup, or operating procedures change.
- Never commit passwords, access tokens, private keys, production data, or other secrets. Use fake data in tests.
- Request only the permissions needed for a workflow, and pin third-party GitHub Actions to trusted versions or full commit SHAs according to repository policy.
- Do not claim that a security control or runtime behavior is verified unless there is observable evidence.

## Atomic task claiming

The implementation repository uses Git refs under `refs/claims/*` as a test-and-set primitive: competing workers attempt to create the same task claim, and only one should acquire it. Do not reproduce or maintain the claim implementation in this repository; the implementation and payload contract live in [`scripts/claim_task.py`](https://github.com/ibrahim-ai-team/ai-software-team/blob/main/scripts/claim_task.py).

Typical invocation from an `ai-software-team` checkout:

```sh
python scripts/claim_task.py --task-id TASK-123 --run-id run-456 --remote origin
```

Exit codes: `0` means acquired or already held by the same run; `1` means another run holds the claim; `2` means invalid task ID; `3` means a retryable remote/Git operation failed. `--dry-run` prints the payload and example ref update without acquiring the claim.

## Review readiness

A pull request should include:
- [ ] A clear problem statement and bounded scope.
- [ ] A link to the related issue, when applicable.
- [ ] Tests or checks run, with results.
- [ ] Documentation updates or a note explaining why none are needed.
- [ ] Security, compatibility, and migration considerations where relevant.

Be respectful, specific, and constructive in discussions. If a change is blocked, explain the missing decision or evidence rather than guessing.
