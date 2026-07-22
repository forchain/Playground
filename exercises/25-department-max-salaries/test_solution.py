import sqlite3
import unittest
from pathlib import Path


CASES = [{'tables': {'departments': (['dept_id', 'dept_name'], [[1, 'Marketing'], [2, 'Engineering'], [3, 'Finance']]), 'employees': (['emp_id', 'emp_name', 'salary', 'dept_id'], [[1, 'Alice Johnson', 60000, 1], [2, 'Bob Williams', 70000, 1], [3, 'Carol Smith', 52000, 2], [4, 'David Andrews', 48000, 2], [5, 'Ellen Reeves', 75000, 3], [6, 'Frank Nelson', 76000, 3], [7, 'Gary Thompson', 55000, 3]])}, 'expected': [['Marketing', 70000], ['Finance', 76000]]}, {'tables': {'departments': (['dept_id', 'dept_name'], [[1, 'HR'], [2, 'Operations'], [3, 'Design']]), 'employees': (['emp_id', 'emp_name', 'salary', 'dept_id'], [[1, 'Hannah Clark', 51000, 1], [2, 'Ian Davis', 52000, 1], [3, 'Jack Erickson', 80000, 2], [4, 'Laura Foster', 82000, 2], [5, 'Mona Gray', 49000, 2], [6, 'Nick Howard', 53000, 3]])}, 'expected': [['HR', 52000], ['Operations', 82000]]}]


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
