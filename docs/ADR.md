# Architecture Decision Records

Use an Architecture Decision Record (ADR) to preserve consequential decisions and the reasoning behind them. Keep each record short and link it to the issue and PR where the decision was discussed or implemented.

## When to write an ADR

Write an ADR when a decision affects more than one repository or is costly to reverse, especially:
- architecture or repository boundaries;
- security, permissions, secret handling, or agent autonomy;
- language, framework, model/provider, or major tooling choices;
- shared agent/skill contracts or compatibility expectations;
- release/versioning policy or significant CI/CD design.

Do not write an ADR for routine implementation details that are easy to change.

## Lifecycle

- **Proposed** — open for discussion; not yet authoritative.
- **Accepted** — decision approved and currently in effect.
- **Rejected** — considered and not selected; retain the rationale.
- **Superseded** — replaced by a later ADR; link the replacement.

Never silently rewrite an accepted decision's meaning. Create a new ADR and mark the old one Superseded.

## Workflow

1. Copy [the ADR template](ADR-TEMPLATE.md) into `docs/adr/NNNN-short-title.md`, choosing the next available number.
2. Link the motivating issue and relevant PR(s).
3. Explain context, alternatives, trade-offs, and consequences in plain language.
4. Discuss the proposal in the issue/PR; update its status after a decision.
5. Add the ADR to the index below.
6. When a decision changes, add a replacement ADR and cross-link both records.

## Index

| ID | Title | Status | Related work |
| --- | --- | --- | --- |
| [0000](adr/0000-example-lightweight-process.md) | Example: keep the decision process lightweight | Example only — not an accepted technical decision | Demonstrates the format |

The example is illustrative and does not establish a binding architecture choice.
