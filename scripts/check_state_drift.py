#!/usr/bin/env python3
"""Compare .github's board mapping with ai-software-team TaskStatus enum."""

import argparse
import re
import sys
from pathlib import Path


def parse_board_mapping(workflow_path: Path) -> dict[str, str]:
    text = workflow_path.read_text(encoding="utf-8")
    section = re.search(
        r"### Canonical board status mapping\s*(.*?)(?=\n## |\Z)", text, re.S
    )
    if not section:
        raise ValueError(
            f"{workflow_path}: missing '### Canonical board status mapping' section"
        )
    mapping: dict[str, str] = {}
    for label, enum_value in re.findall(
        r"^-\s+(.+?)\s+→\s+`([A-Z_]+)`\s*$",
        section.group(1),
        re.M,
    ):
        mapping[label.strip()] = enum_value
    if not mapping:
        raise ValueError(f"{workflow_path}: no '<label> → `ENUM_VALUE`' mappings found")
    return mapping


def parse_task_status_values(model_path: Path) -> set[str]:
    text = model_path.read_text(encoding="utf-8")
    match = re.search(r"^class TaskStatus\([^\n]+\):\s*(.*?)(?=^class |\Z)", text, re.M | re.S)
    if not match:
        raise ValueError(f"{model_path}: TaskStatus enum not found")
    return set(re.findall(r"^\s+[A-Z][A-Z0-9_]*\s*=\s*['\"]([A-Z_]+)['\"]", match.group(1), re.M))


def documented_internal_only(workflow_path: Path) -> set[str]:
    text = workflow_path.read_text(encoding="utf-8")
    match = re.search(r"Implementation-only task states:\\s*([^\\n]+)", text, re.I)
    if not match:
        return set()
    return set(re.findall(r"`([A-Z_]+)`", match.group(1)))


def check(workflow_path: Path, model_path: Path) -> int:
    mapping = parse_board_mapping(workflow_path)
    model_values = parse_task_status_values(model_path)
    mapped_values = set(mapping.values())
    documented_internal = documented_internal_only(workflow_path)

    missing_in_model = mapped_values - model_values
    undocumented_extra = model_values - mapped_values - documented_internal
    duplicate_values = sorted(value for value in mapped_values if list(mapping.values()).count(value) > 1)

    if not missing_in_model and not undocumented_extra and not duplicate_values:
        print(
            f"PASS: {len(mapping)} board labels map to TaskStatus; "
            f"documented implementation-only states: {', '.join(sorted(documented_internal)) or 'none'}."
        )
        return 0

    print("FAIL: cross-repository status drift detected.", file=sys.stderr)
    if missing_in_model:
        print("  Board mappings absent from models/status.py: " + ", ".join(sorted(missing_in_model)), file=sys.stderr)
    if undocumented_extra:
        print("  Implementation states not mapped or documented as internal-only: " + ", ".join(sorted(undocumented_extra)), file=sys.stderr)
    if duplicate_values:
        print("  Duplicate enum mappings in WORKFLOW.md: " + ", ".join(duplicate_values), file=sys.stderr)
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--impl-repo", type=Path, default=Path("../ai-software-team"))
    parser.add_argument("--workflow", type=Path, default=Path("docs/WORKFLOW.md"))
    args = parser.parse_args()
    model = args.impl_repo / "models" / "status.py"
    if not args.workflow.is_file():
        print(f"ERROR: workflow document not found: {args.workflow}", file=sys.stderr)
        return 2
    if not model.is_file():
        print(f"ERROR: implementation model not found: {model}", file=sys.stderr)
        return 2
    try:
        return check(args.workflow, model)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
