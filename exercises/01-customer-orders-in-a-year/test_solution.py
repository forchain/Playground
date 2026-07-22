import sqlite3
import unittest
from pathlib import Path


CASES = [{'tables': {'customers': (['customer_id', 'customer_name'], [[1, 'Alice Johnson'], [2, 'Eva Parker'], [3, 'Carl Weber']]), 'orders': (['order_id', 'customer_id', 'order_total', 'order_date'], [[1, 1, 200, '2023-03-10'], [2, 1, 400, '2023-04-05'], [3, 2, 500, '2022-12-15'], [4, 2, 300, '2023-01-20'], [5, 3, 100, '2023-07-01'], [6, 3, 100, '2023-07-02']])}, 'expected': [['Alice Johnson', 200], ['Alice Johnson', 400], ['Carl Weber', 100], ['Carl Weber', 100], ['Eva Parker', 300]]}, {'tables': {'customers': (['customer_id', 'customer_name'], [[1, 'Barry Ellis'], [2, 'Chloe Evans'], [3, 'Derek Stone']]), 'orders': (['order_id', 'customer_id', 'order_total', 'order_date'], [[1, 1, 600, '2023-08-10'], [2, 1, 300, '2023-08-11'], [3, 2, 200, '2023-06-05'], [4, 2, 200, '2023-06-06'], [5, 3, 400, '2022-10-20'], [6, 3, 700, '2023-02-15']])}, 'expected': [['Barry Ellis', 300], ['Barry Ellis', 600], ['Chloe Evans', 200], ['Chloe Evans', 200], ['Derek Stone', 700]]}]


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
