import sqlite3
import unittest
from pathlib import Path


CASES = [{'tables': {'employees': (['emp_id', 'emp_name', 'manager_id', 'salary'], [[1, 'Alice', None, 50000], [2, 'Bob', 1, 60000], [3, 'Carol', 1, 45000], [4, 'David', 2, 70000], [5, 'Eve', 2, 55000]])}, 'expected': [['Bob'], ['David']]}, {'tables': {'employees': (['emp_id', 'emp_name', 'manager_id', 'salary'], [[1, 'Frank', None, 80000], [2, 'Grace', 1, 75000], [3, 'Heidi', 1, 85000], [4, 'Ivan', 3, 70000], [5, 'Judy', 3, 90000]])}, 'expected': [['Heidi'], ['Judy']]}]


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
