import sqlite3
import unittest
from pathlib import Path


CASES = [{'tables': {'departments': (['dept_id', 'dept_name'], [[1, 'Engineering'], [2, 'HR'], [3, 'Marketing']]), 'employees': (['emp_id', 'emp_name', 'dept_id', 'performance_score'], [[1, 'Alice', 1, 85], [2, 'Bob', 1, 92], [3, 'Carol', 1, 85], [4, 'David', 2, 88], [5, 'Eve', 2, 80], [6, 'Frank', 2, 88], [7, 'Grace', 3, 90], [8, 'Hannah', 3, 85], [9, 'Ian', 3, 75]])}, 'expected': [['Engineering', 'Bob', 92], ['Engineering', 'Alice', 85], ['HR', 'David', 88], ['HR', 'Frank', 88], ['Marketing', 'Grace', 90], ['Marketing', 'Hannah', 85]]}, {'tables': {'departments': (['dept_id', 'dept_name'], [[1, 'Sales'], [2, 'Support']]), 'employees': (['emp_id', 'emp_name', 'dept_id', 'performance_score'], [[1, 'John', 1, 95], [2, 'Kelly', 1, 80], [3, 'Liam', 1, 95], [4, 'Morgan', 2, 87], [5, 'Nina', 2, 87], [6, 'Oliver', 2, 85]])}, 'expected': [['Sales', 'John', 95], ['Sales', 'Liam', 95], ['Support', 'Morgan', 87], ['Support', 'Nina', 87]]}]


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
