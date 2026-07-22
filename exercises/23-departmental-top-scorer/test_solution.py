import sqlite3
import unittest
from pathlib import Path


CASES = [{'tables': {'employees': (['emp_id', 'emp_name', 'department'], [[1, 'Alice', 'Engineering'], [2, 'Bob', 'Engineering'], [3, 'Cathy', 'HR']]), 'performance': (['record_id', 'emp_id', 'score', 'hours_worked'], [[1, 1, 95, 40], [2, 1, 90, 50], [3, 2, 95, 45], [4, 2, 95, 55], [5, 3, 85, 60], [6, 3, 80, 50]])}, 'expected': [['Engineering', 'Bob', 190, 100], ['HR', 'Cathy', 165, 110]]}, {'tables': {'employees': (['emp_id', 'emp_name', 'department'], [[1, 'Ethan', 'Sales'], [2, 'Frank', 'Sales'], [3, 'Grace', 'Marketing']]), 'performance': (['record_id', 'emp_id', 'score', 'hours_worked'], [[1, 1, 88, 30], [2, 1, 92, 40], [3, 2, 90, 50], [4, 2, 90, 45], [5, 3, 85, 70], [6, 3, 85, 60]])}, 'expected': [['Marketing', 'Grace', 170, 130], ['Sales', 'Frank', 180, 95]]}]


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
