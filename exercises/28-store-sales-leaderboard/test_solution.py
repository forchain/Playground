import sqlite3
import unittest
from pathlib import Path


CASES = [{'tables': {'stores': (['store_id', 'store_name', 'region'], [[1, 'Alpha Mart', 'North'], [2, 'Beta Bazaar', 'North'], [3, 'Gamma Goods', 'North'], [4, 'Delta Deals', 'South'], [5, 'Omega Outlet', 'South']]), 'sales': (['sale_id', 'store_id', 'amount'], [[1, 1, 3000], [2, 1, 4000], [3, 2, 2000], [4, 2, 6000], [5, 3, 8000], [6, 4, 7000], [7, 5, 2000], [8, 5, 5000]])}, 'expected': [['North', 'Beta Bazaar', 1, 8000, 8000], ['North', 'Gamma Goods', 2, 8000, 16000], ['North', 'Alpha Mart', 3, 7000, 23000], ['South', 'Delta Deals', 1, 7000, 7000], ['South', 'Omega Outlet', 2, 7000, 14000]]}, {'tables': {'stores': (['store_id', 'store_name', 'region'], [[1, 'A-Mart', 'East'], [2, 'B-Store', 'East'], [3, 'C-Shop', 'West'], [4, 'D-Depot', 'West'], [5, 'E-Hub', 'West']]), 'sales': (['sale_id', 'store_id', 'amount'], [[1, 1, 6000], [2, 1, 5000], [3, 2, 3000], [4, 2, 4000], [5, 3, 8000], [6, 4, 7000], [7, 5, 9000]])}, 'expected': [['East', 'A-Mart', 1, 11000, 11000], ['East', 'B-Store', 2, 7000, 18000], ['West', 'E-Hub', 1, 9000, 9000], ['West', 'C-Shop', 2, 8000, 17000], ['West', 'D-Depot', 3, 7000, 24000]]}]


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
