# Security Policy

## Current reporting-channel status

**Status as of 2026-10-20: NOT CONFIGURED.** The security baseline inspection recorded GitHub private vulnerability reporting as disabled for `ibrahim-ai-team/.github`. This is a dated observation, not confirmation of the current live setting; current status requires authenticated GitHub verification.

**Private fallback:** Contact the organization owner through the [Ibrahim AI Team GitHub profile](https://github.com/ibrahim-ai-team) and request a private reporting channel. Do not publish exploit details, credentials, or sensitive security information in an issue or pull request. If you cannot establish a private channel, do not disclose sensitive reproduction details publicly.

## Reporting a vulnerability

Please do **not** report exploitable vulnerabilities, credentials, or sensitive security details in a public issue or pull request.

1. If GitHub's **Security** tab offers **Report a vulnerability** for the affected repository, use that private reporting route.
2. If private vulnerability reporting is unavailable, contact the organization owner through the [Ibrahim AI Team GitHub profile](https://github.com/ibrahim-ai-team) and ask for a private channel. Do not post exploit details or secrets publicly while waiting.
3. Include only the information needed to understand and reproduce the issue safely. Use redacted logs and synthetic examples; never send real credentials or customer data.

Please include, where possible:
- The affected repository, file, workflow, or component.
- The impact and conditions required to reproduce the issue.
- A minimal proof of concept using non-sensitive test data.
- Any suggested mitigation.

## Handling and scope

- The organization will review reports as capacity permits; this document does not promise a specific response time or service-level agreement.
- Do not access, modify, or exfiltrate data that is not yours, disrupt services, or perform destructive testing.
- Do not publish details before coordinating a safe disclosure with the maintainer.
- If a secret is exposed, revoke or rotate it immediately and remove it from active use. Deleting it from a commit alone does not invalidate it.

## Security controls

Repository workflows, secret scanning, dependency alerts, branch rules, and AI-agent permissions may differ by repository and plan. The presence of documentation or a workflow file is not proof that a control is enabled or enforced. Verify repository settings and observed behavior before relying on a control.
