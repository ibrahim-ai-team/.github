#!/usr/bin/env python3
"""Stdlib-only structural checks for this repository's config and docs.

Run all checks:      python scripts/validate_repo.py
Run one group:       python scripts/validate_repo.py yaml|markdown
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ISSUE_FORMS = ROOT / ".github" / "ISSUE_TEMPLATE"
RULESET = ROOT / ".github" / "rulesets" / "main-protection.json"
DEPENDABOT = ROOT / ".github" / "dependabot.yml"
CI_WORKFLOW = ROOT / ".github" / "workflows" / "ci.yml"
WORKFLOW_DOC = ROOT / "docs" / "WORKFLOW.md"

MAPPING_LINE = re.compile(r"^-\s+.+?\s+→\s+`[A-Z_]+`\s*$", re.M)
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)[^)]*\)")


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def check_indentation(path: Path, text: str) -> list[str]:
    errors = []
    if "\t" in text:
        errors.append(f"{rel(path)}: tab character found; YAML indentation must use spaces")
    for number, line in enumerate(text.splitlines(), 1):
        indent = len(line) - len(line.lstrip(" "))
        if line.strip() and indent % 2:
            errors.append(f"{rel(path)}:{number}: indentation is not a multiple of two")
    return errors


def check_issue_forms() -> list[str]:
    errors = []
    files = sorted(ISSUE_FORMS.glob("*.yml"))
    if not files:
        return [f"{rel(ISSUE_FORMS)}: no issue-form YAML files found"]
    for path in files:
        text = path.read_text(encoding="utf-8")
        if not text.strip():
            errors.append(f"{rel(path)}: empty file")
            continue
        errors += check_indentation(path, text)
        if path.name == "config.yml":
            continue
        for key in ("name", "description", "body"):
            if not re.search(rf"(?m)^{key}:", text):
                errors.append(f"{rel(path)}: missing top-level issue-form key '{key}'")
        ids = re.findall(r"(?m)^\s+id:\s*(\S+)", text)
        for dup in sorted({i for i in ids if ids.count(i) > 1}):
            errors.append(f"{rel(path)}: duplicate field id '{dup}'")
    return errors


def ci_job_names() -> set[str]:
    text = CI_WORKFLOW.read_text(encoding="utf-8")
    return set(re.findall(r"(?m)^    name:\s*(\S+)\s*$", text))


def check_ruleset() -> list[str]:
    try:
        data = json.loads(RULESET.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{rel(RULESET)}: {exc}"]
    errors = []
    if data.get("target") != "branch":
        errors.append(f"{rel(RULESET)}: target must be 'branch'")
    if data.get("enforcement") != "active":
        errors.append(f"{rel(RULESET)}: enforcement must be 'active'")
    if data.get("conditions", {}).get("ref_name", {}).get("include") != ["refs/heads/main"]:
        errors.append(f"{rel(RULESET)}: must target only refs/heads/main")
    rules = {rule.get("type"): rule for rule in data.get("rules", [])}
    expected = {"pull_request", "required_status_checks", "non_fast_forward", "deletion", "required_linear_history"}
    if missing := expected - rules.keys():
        errors.append(f"{rel(RULESET)}: missing rules: {', '.join(sorted(missing))}")
    # Required check contexts must match real CI job names, or merges block forever.
    contexts = {
        check["context"]
        for check in rules.get("required_status_checks", {}).get("parameters", {}).get("required_status_checks", [])
    }
    if unknown := contexts - ci_job_names():
        errors.append(f"{rel(RULESET)}: required checks not produced by ci.yml: {', '.join(sorted(unknown))}")
    return errors


def check_dependabot() -> list[str]:
    text = DEPENDABOT.read_text(encoding="utf-8")
    errors = check_indentation(DEPENDABOT, text)
    for item in ("version: 2", "updates:", "package-ecosystem: github-actions", "interval: weekly"):
        if item not in text:
            errors.append(f"{rel(DEPENDABOT)}: missing '{item}'")
    return errors


def markdown_files() -> list[Path]:
    return sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.relative_to(ROOT).parts)


def check_markdown_links() -> list[str]:
    errors = []
    for doc in markdown_files():
        for target in MARKDOWN_LINK.findall(doc.read_text(encoding="utf-8")):
            target = target.split("#", 1)[0]
            if not target or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("//"):
                continue
            if not (doc.parent / target).exists():
                errors.append(f"{rel(doc)}: broken relative link: {target}")
    return errors


def check_mapping_not_duplicated() -> list[str]:
    duplicates = [
        rel(path)
        for path in markdown_files()
        if path != WORKFLOW_DOC and len(MAPPING_LINE.findall(path.read_text(encoding="utf-8"))) >= 2
    ]
    if duplicates:
        return ["Board-state mapping duplicated outside docs/WORKFLOW.md: " + ", ".join(duplicates)]
    return []


GROUPS = {
    "yaml": (check_issue_forms, check_ruleset, check_dependabot),
    "markdown": (check_markdown_links, check_mapping_not_duplicated),
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("groups", nargs="*", help=f"check groups to run: {', '.join(GROUPS)} (default: all)")
    args = parser.parse_args()
    if unknown := set(args.groups) - GROUPS.keys():
        parser.error(f"unknown group(s): {', '.join(sorted(unknown))}")
    failed = False
    for group in args.groups or GROUPS:
        for check in GROUPS[group]:
            errors = check()
            label = check.__name__.removeprefix("check_")
            if errors:
                failed = True
                print(f"FAIL: {label}", file=sys.stderr)
                for error in errors:
                    print(f"  {error}", file=sys.stderr)
            else:
                print(f"PASS: {label}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
