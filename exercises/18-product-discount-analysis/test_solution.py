import sqlite3
import unittest
from pathlib import Path


CASES = [{'tables': {'products': (['product_id', 'product_name', 'price'], [[1, 'Laptop', 2000], [2, 'Smartphone', 1000]]), 'sales': (['sale_id', 'product_id', 'quantity', 'sale_date'], [[1, 1, 30, '2024-01-15'], [2, 2, 60, '2024-01-20']]), 'discounts': (['discount_id', 'product_id', 'discount_percentage', 'start_date', 'end_date'], [[1, 1, 25, '2024-01-10', '2024-01-30'], [2, 2, 20, '2024-01-15', '2024-01-25']])}, 'expected': []}, {'tables': {'products': (['product_id', 'product_name', 'price'], [[1, 'TV', 3000], [2, 'Refrigerator', 2000]]), 'sales': (['sale_id', 'product_id', 'quantity', 'sale_date'], [[1, 1, 25, '2024-03-01'], [2, 2, 40, '2024-03-10']]), 'discounts': (['discount_id', 'product_id', 'discount_percentage', 'start_date', 'end_date'], [[1, 1, 30, '2024-02-28', '2024-03-10'], [2, 2, 20, '2024-03-05', '2024-03-15']])}, 'expected': [['Refrigerator', 64000], ['TV', 52500]]}]


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
