import sqlite3
import unittest
from pathlib import Path


CASES = [{'tables': {'employees': (['emp_id', 'emp_name'], [[1, 'Alice'], [2, 'Bob'], [3, 'Carol'], [4, 'David'], [5, 'Ethan'], [6, 'Frank']]), 'hierarchy': (['emp_id', 'manager_id'], [[2, 1], [3, 1], [4, 2], [5, 2], [6, 3]])}, 'expected': [[1, 'Alice', 6], [2, 'Bob', 3], [3, 'Carol', 2]]}, {'tables': {'employees': (['emp_id', 'emp_name'], [[1, 'Grace'], [2, 'Hannah'], [3, 'Ian'], [4, 'Jack'], [5, 'Kate']]), 'hierarchy': (['emp_id', 'manager_id'], [[2, 1], [3, 1], [4, 2], [5, 2]])}, 'expected': [[1, 'Grace', 5], [2, 'Hannah', 3]]}]


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
