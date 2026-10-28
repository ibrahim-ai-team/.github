"""Unit tests for scripts/. Run: python -m unittest discover -s tests"""

import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import check_state_drift  # noqa: E402
import validate_repo  # noqa: E402

STATES = [
    ("Backlog", "BACKLOG"),
    ("Ready", "READY"),
    ("In Progress", "IN_PROGRESS"),
    ("In Review", "IN_REVIEW"),
    ("Changes Requested", "CHANGES_REQUESTED"),
    ("Approved — Awaiting Human Merge", "APPROVED_AWAITING_HUMAN_MERGE"),
    ("Blocked", "BLOCKED"),
    ("Done", "DONE"),
]


class StateDriftTest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.tmp = Path(tmp.name)

    def run_check(self, board, enum_values, internal=("CLAIMED", "CANCELLED")):
        workflow = self.tmp / "WORKFLOW.md"
        workflow.write_text(
            "### Canonical board status mapping\n"
            + "".join(f"- {label} → `{value}`\n" for label, value in board)
            + "\nImplementation-only task states: "
            + ", ".join(f"`{v}`" for v in internal)
            + ".\n",
            encoding="utf-8",
        )
        model = self.tmp / "status.py"
        model.write_text(
            "from enum import Enum\n\n\nclass TaskStatus(str, Enum):\n"
            + "".join(f'    {v} = "{v}"\n' for v in enum_values),
            encoding="utf-8",
        )
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return check_state_drift.check(workflow, model)

    def test_aligned(self):
        values = [v for _, v in STATES] + ["CLAIMED", "CANCELLED"]
        self.assertEqual(self.run_check(STATES, values), 0)

    def test_board_state_missing_from_model(self):
        values = [v for _, v in STATES if v != "READY"] + ["CLAIMED", "CANCELLED"]
        self.assertEqual(self.run_check(STATES, values), 1)

    def test_undocumented_model_state(self):
        values = [v for _, v in STATES] + ["CLAIMED", "CANCELLED", "ARCHIVED"]
        self.assertEqual(self.run_check(STATES, values), 1)

    def test_duplicate_enum_mapping(self):
        board = STATES + [("Finished", "DONE")]
        values = [v for _, v in STATES] + ["CLAIMED", "CANCELLED"]
        self.assertEqual(self.run_check(board, values), 1)

    def test_real_workflow_doc_parses(self):
        mapping = check_state_drift.parse_board_mapping(validate_repo.WORKFLOW_DOC)
        self.assertEqual(list(mapping.items()), STATES)


class ValidateRepoTest(unittest.TestCase):
    def test_repository_passes(self):
        for checks in validate_repo.GROUPS.values():
            for check in checks:
                self.assertEqual(check(), [], check.__name__)

    def test_ruleset_context_must_match_ci_job(self):
        with mock.patch.object(validate_repo, "ci_job_names", return_value={"yaml-lint"}):
            errors = validate_repo.check_ruleset()
        self.assertTrue(any("not produced by ci.yml" in e for e in errors), errors)

    def test_odd_indentation_and_tabs(self):
        path = validate_repo.ROOT / "x.yml"
        errors = validate_repo.check_indentation(path, "a:\n   b: 1\n\tc: 2\n")
        self.assertEqual(len(errors), 2, errors)


if __name__ == "__main__":
    unittest.main()
