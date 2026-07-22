import sqlite3
import unittest
from pathlib import Path


CASES = [{'tables': {'orders': (['order_id', 'customer_id', 'order_date', 'order_amount'], [[1, 101, '2024-01-01', 300], [2, 102, '2024-01-02', 200], [3, 101, '2024-01-03', 150], [4, 103, '2024-01-04', 400], [5, 104, '2024-01-05', 100], [6, 103, '2024-01-06', 300]])}, 'expected': [[103, 700], [101, 450], [102, 200]]}, {'tables': {'orders': (['order_id', 'customer_id', 'order_date', 'order_amount'], [[1, 201, '2024-01-01', 500], [2, 202, '2024-01-02', 300], [3, 203, '2024-01-03', 300], [4, 204, '2024-01-04', 200], [5, 205, '2024-01-05', 300], [6, 202, '2024-01-06', 200]])}, 'expected': [[201, 500], [202, 500], [203, 300], [205, 300]]}]


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
