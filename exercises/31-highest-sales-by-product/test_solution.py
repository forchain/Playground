import sqlite3
import unittest
from pathlib import Path


CASES = [{'tables': {'sales': (['store_id', 'product', 'quantity', 'sale_date'], [[1, 'Apples', 50, '2024-12-20'], [2, 'Apples', 60, '2024-12-21'], [3, 'Apples', 60, '2024-12-21'], [1, 'Oranges', 30, '2024-12-20'], [2, 'Oranges', 50, '2024-12-21'], [1, 'Apples', 10, '2024-12-22']])}, 'expected': [['Apples', 1, 60], ['Apples', 2, 60], ['Apples', 3, 60], ['Oranges', 2, 50]]}, {'tables': {'sales': (['store_id', 'product', 'quantity', 'sale_date'], [[1, 'Bananas', 100, '2024-11-25'], [2, 'Bananas', 150, '2024-11-26'], [1, 'Bananas', 100, '2024-11-27'], [3, 'Grapes', 200, '2024-11-27'], [2, 'Grapes', 200, '2024-11-28'], [1, 'Grapes', 100, '2024-11-28']])}, 'expected': [['Bananas', 1, 200], ['Grapes', 2, 200], ['Grapes', 3, 200]]}]


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
