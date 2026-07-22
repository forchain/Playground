import sqlite3
import unittest
from pathlib import Path


CASES = [{'tables': {'departments': (['dept_id', 'dept_name', 'annual_budget'], [[1, 'HR', 50000], [2, 'IT', 80000], [3, 'Marketing', 60000]]), 'expenses': (['expense_id', 'dept_id', 'amount', 'expense_date'], [[1, 1, 20000, '2024-01-10'], [2, 1, 40000, '2024-02-15'], [3, 2, 50000, '2024-03-01'], [4, 2, 40000, '2024-03-15'], [5, 3, 25000, '2024-02-20'], [6, 3, 30000, '2024-03-05']])}, 'expected': [['HR', 60000, 10000], ['IT', 90000, 10000]]}, {'tables': {'departments': (['dept_id', 'dept_name', 'annual_budget'], [[1, 'Marketing', 60000], [2, 'Operations', 100000]]), 'expenses': (['expense_id', 'dept_id', 'amount', 'expense_date'], [[1, 1, 25000, '2024-02-10'], [2, 1, 40000, '2024-03-01'], [3, 2, 50000, '2024-01-15'], [4, 2, 60000, '2024-02-20']])}, 'expected': [['Operations', 110000, 10000], ['Marketing', 65000, 5000]]}]


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
