#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path


root = Path(__file__).parent
tests = sorted(root.glob("*/test_solution.py"))
failures = 0
for test in tests:
    print(f"\n==> {test.parent.name}", flush=True)
    failures += subprocess.run([sys.executable, str(test), "-v"], check=False).returncode != 0
print(f"\nRan {len(tests)} exercise test suites; failures: {failures}")
raise SystemExit(1 if failures else 0)
