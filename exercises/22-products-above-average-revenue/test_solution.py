import sqlite3
import unittest
from pathlib import Path


CASES = [{'tables': {'orders': (['order_id', 'product_id', 'quantity'], [[1, 1, 10], [2, 1, 5], [3, 2, 2], [4, 3, 20], [5, 4, 3]]), 'products': (['product_id', 'product_name', 'price'], [[1, 'Widget', 100], [2, 'Gadget', 200], [3, 'Thingamajig', 50], [4, 'Doohickey', 500]])}, 'expected': [['Doohickey'], ['Widget']]}, {'tables': {'orders': (['order_id', 'product_id', 'quantity'], [[1, 1, 10], [2, 1, 5], [3, 2, 2], [4, 2, 10], [5, 3, 5], [6, 3, 3], [7, 4, 7]]), 'products': (['product_id', 'product_name', 'price'], [[1, 'Widget', 100], [2, 'Gadget', 200], [3, 'Thingamajig', 150], [4, 'Doohickey', 300]])}, 'expected': [['Doohickey'], ['Gadget']]}]


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
