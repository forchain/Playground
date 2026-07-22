import sqlite3
import unittest
from pathlib import Path


CASES = [{'tables': {'users': (['user_id', 'user_name', 'region'], [[1, 'Alice', 'North'], [2, 'Bob', 'North'], [3, 'Carol', 'South'], [4, 'Dave', 'West']]), 'transactions': (['transaction_id', 'user_id', 'amount', 'transaction_date'], [[1, 1, 5000, '2024-01-15'], [2, 1, 7000, '2024-02-20'], [3, 2, 8000, '2024-03-05'], [4, 3, 6000, '2024-02-10'], [5, 3, 6000, '2024-03-01'], [6, 4, 4000, '2024-01-25']])}, 'expected': [['North', 'Alice', 12000, '2024-02-20'], ['South', 'Carol', 12000, '2024-03-01']]}, {'tables': {'users': (['user_id', 'user_name', 'region'], [[1, 'Frank', 'East'], [2, 'Grace', 'West'], [3, 'Heidi', 'East'], [4, 'Ivan', 'West']]), 'transactions': (['transaction_id', 'user_id', 'amount', 'transaction_date'], [[1, 1, 7000, '2024-01-10'], [2, 1, 4000, '2024-02-05'], [3, 2, 3000, '2024-03-15'], [4, 2, 4000, '2024-04-10'], [5, 3, 2000, '2024-02-12'], [6, 4, 10000, '2024-01-25']])}, 'expected': [['East', 'Frank', 11000, '2024-02-05']]}]


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
