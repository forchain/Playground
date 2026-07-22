import sqlite3
import unittest
from pathlib import Path


CASES = [{'tables': {'departments': (['dept_id', 'dept_name'], [[1, 'Engineering'], [2, 'HR'], [3, 'Marketing']]), 'employees': (['emp_id', 'emp_name', 'salary', 'dept_id'], [[1, 'Alice', 60000, 1], [2, 'Bob', 55000, 1], [3, 'Carol', 40000, 1], [4, 'David', 45000, 2], [5, 'Eve', 50000, 2], [6, 'Frank', 48000, 3], [7, 'Grace', 52000, 3]])}, 'expected': [['Engineering', 3, 3, 0], ['HR', 2, 2, 0], ['Marketing', 2, 2, 0]]}, {'tables': {'departments': (['dept_id', 'dept_name'], [[1, 'Sales'], [2, 'Support']]), 'employees': (['emp_id', 'emp_name', 'salary', 'dept_id'], [[1, 'John', 75000, 1], [2, 'Kelly', 80000, 1], [3, 'Liam', 70000, 1], [4, 'Morgan', 50000, 2], [5, 'Nina', 45000, 2]])}, 'expected': [['Sales', 3, 0, 3], ['Support', 2, 2, 0]]}]


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
