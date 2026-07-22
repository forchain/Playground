import sqlite3
import unittest
from pathlib import Path


CASES = [{'tables': {'departments': (['dept_id', 'dept_name'], [[1, 'Research'], [2, 'Development'], [3, 'Marketing']]), 'tasks': (['task_id', 'dept_id', 'task_type', 'task_count'], [[1, 1, 'critical', 30], [2, 1, 'major', 20], [3, 1, 'minor', 10], [4, 2, 'critical', 25], [5, 2, 'major', 30], [6, 2, 'minor', 5], [7, 3, 'critical', 20], [8, 3, 'major', 15]])}, 'expected': [['Development', 60, 3, 'major', 30], ['Research', 60, 3, 'critical', 30]]}, {'tables': {'departments': (['dept_id', 'dept_name'], [[1, 'HR'], [2, 'IT'], [3, 'Finance']]), 'tasks': (['task_id', 'dept_id', 'task_type', 'task_count'], [[1, 1, 'critical', 40], [2, 1, 'major', 15], [3, 2, 'critical', 35], [4, 2, 'minor', 20], [5, 3, 'major', 30], [6, 3, 'minor', 25]])}, 'expected': [['Finance', 55, 2, 'major', 30], ['HR', 55, 2, 'critical', 40], ['IT', 55, 2, 'critical', 35]]}]


def create_case(case):
    db = sqlite3.connect(":memory:")
    for name, (headers, rows) in case["tables"].items():
        values_by_column = list(zip(*rows)) if rows else [[] for _ in headers]
        types = []
        for values in values_by_column:
            non_null = [value for value in values if value is not None]
            types.append("INTEGER" if all(isinstance(value, int) for value in non_null) else "TEXT")
        columns = ", ".join(f'"{header}" {kind}' for header, kind in zip(headers, types))
        db.execute(f'CREATE TABLE "{name}" ({columns})')
        placeholders = ", ".join("?" for _ in headers)
        db.executemany(f'INSERT INTO "{name}" VALUES ({placeholders})', rows)
    return db


class SolutionTests(unittest.TestCase):
    def test_sample_cases(self):
        sql = (Path(__file__).parent / "solution.sql").read_text(encoding="utf-8")
        statements = [statement.strip() for statement in sql.split(";") if statement.strip()]
        for index, case in enumerate(CASES, 1):
            with self.subTest(sample=index), create_case(case) as db:
                actual = []
                for statement in statements:
                    actual.extend([list(row) for row in db.execute(statement).fetchall()])
                self.assertEqual(case["expected"], actual)


if __name__ == "__main__":
    unittest.main()
