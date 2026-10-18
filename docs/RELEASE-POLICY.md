# Release, Changelog, and Compatibility Policy

**Scope:** Reusable AI agents, skills, prompts, templates, standards, and workflows maintained by Ibrahim AI Team.

## Release model by repository

- **`.github`** — community-health files, organization profile, templates, and governance docs can be delivered continuously through reviewed PRs. Tag a release only when a set of changes needs a stable, named reference.
- **`ai-software-team`** — changes to shared agents, skills, commands, validation, and engineering standards should be traceable to merged PRs. Use Git tags/releases when consumers need a stable snapshot; do not create a release ceremony for every documentation-only change.
- **Project repositories** — choose release cadence based on the product's deployment needs and document it in that repository. This organization policy does not assume any specific application stack or deployment model.

## Versioning

Use semantic versioning (MAJOR.MINOR.PATCH) for a published bundle when a stable compatibility contract exists:
- **MAJOR:** intentional breaking change to documented agent/skill inputs, outputs, file paths, permissions, workflow interfaces, or required configuration.
- **MINOR:** backward-compatible capability, skill, template, or workflow addition.
- **PATCH:** backward-compatible correction, clarification, or fix.

Until a stable public contract exists, commits and merged PRs are the authoritative change history. Do not invent a version number just to label an ordinary commit.

## Changelog

For a GitHub Release, summarize user-visible changes under:
- Added
- Changed
- Fixed
- Security
- Breaking changes / migration

Link merged PRs or issues for substantive entries. Omit empty sections. Keep the notes understandable to a maintainer who did not participate in the change. Avoid copying every trivial commit into a user-facing changelog.

## Compatibility and migration

A change is potentially breaking if it changes:
- required agent inputs or expected outputs;
- skill names, locations, or invocation conventions;
- shared instructions or template fields that consumers depend on;
- permission defaults, tool allow/deny rules, or security boundaries;
- reusable workflow inputs, secrets, permissions, or required checks.

For a breaking change, the PR must document affected consumers, migration steps, validation evidence, and rollback/recovery notes. Prefer a transition period or compatibility shim when practical. Update the relevant docs and create follow-up issues for consumer migrations.

## Rollback

- Prefer reverting the merged PR when the change is isolated and a revert is safe.
- For a published release, document the affected tag/version and issue a corrective patch or clearly mark the release as withdrawn when necessary.
- If a change alters permissions or security behavior, restore a known-safe configuration and verify it; do not rely solely on reverting documentation.
- Never delete tags or rewrite shared history as a routine rollback.

## Minimum release checklist

- [ ] Changes and linked PRs are summarized.
- [ ] Compatibility impact and breaking changes are stated.
- [ ] Migration and rollback instructions are included when relevant.
- [ ] Validation evidence is recorded.
- [ ] Version/tag is used only when a stable snapshot is useful.
