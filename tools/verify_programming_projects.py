#!/usr/bin/env python3
"""Verify every exported programming-question project independently."""

from __future__ import annotations

import py_compile
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ROOT / "programming-projects"
REQUIRED = {"README.md", "solution.py", "test_solution.py"}


def main() -> int:
    projects = sorted(path for path in PROJECTS.iterdir() if path.is_dir())
    expected = list(range(1, 86))
    actual = [int(project.name.split("-", 1)[0]) for project in projects]
    if actual != expected:
        print(f"Project numbering mismatch: {actual}", file=sys.stderr)
        return 1

    failures: list[str] = []
    for project in projects:
        missing = REQUIRED - {path.name for path in project.iterdir()}
        if missing:
            failures.append(f"{project.name}: missing {sorted(missing)}")
            continue

        try:
            py_compile.compile(project / "solution.py", doraise=True)
            py_compile.compile(project / "test_solution.py", doraise=True)
        except py_compile.PyCompileError as error:
            failures.append(f"{project.name}: {error}")
            continue

        result = subprocess.run(
            [sys.executable, "-m", "unittest", "-q", "test_solution.py"],
            cwd=project,
            text=True,
            capture_output=True,
        )
        if result.returncode:
            failures.append(f"{project.name}:\n{result.stdout}{result.stderr}")

    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1

    print(f"Verified {len(projects)} independent projects: all tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
