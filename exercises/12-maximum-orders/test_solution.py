import sqlite3
import unittest
from pathlib import Path


CASES = [{'tables': {'customers': (['id', 'name'], [[1, 'Lewis Carroll'], [2, 'Isaac Newton'], [3, 'Richard Dawkins'], [4, 'Roger Penrose'], [5, 'Euclid']]), 'orders': (['id', 'amount', 'customer_id'], [[1, 200, 1], [2, 450, 3], [3, 375, 1], [4, 200, 2], [5, 375, 2], [6, 500, 2], [7, 650, 3], [8, 1000, 5], [9, 800, 4], [10, 1000, 4], [11, 375, 2]])}, 'expected': [['Isaac Newton']]}, {'tables': {'customers': (['id', 'name'], [[1, 'Lewis Carroll'], [2, 'Isaac Newton'], [3, 'Richard Dawkins'], [4, 'Roger Penrose'], [5, 'Euclid']]), 'orders': (['id', 'amount', 'customer_id'], [[1, 200, 3], [2, 450, 3], [3, 375, 1], [4, 200, 3], [5, 375, 2], [6, 500, 3], [7, 650, 3], [8, 1000, 5], [9, 800, 4], [10, 1000, 4], [11, 375, 2]])}, 'expected': [['Richard Dawkins']]}]


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
