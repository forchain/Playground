import sqlite3
import unittest
from pathlib import Path


CASES = [{'tables': {'departments': (['dept_id', 'dept_name'], [[1, 'HR'], [2, 'IT']]), 'employees': (['emp_id', 'dept_id', 'emp_name'], [[1, 1, 'Alice'], [2, 1, 'Bob'], [3, 2, 'Carol'], [4, 2, 'David']]), 'expenses': (['expense_id', 'emp_id', 'amount', 'expense_date'], [[1, 1, 20000, '2024-01-10'], [2, 1, 40000, '2024-02-15'], [3, 2, 5000, '2024-01-20'], [4, 3, 25000, '2024-02-25'], [5, 4, 30000, '2024-03-10']])}, 'expected': [['HR', 65000, 40000], ['IT', 55000, 30000]]}, {'tables': {'departments': (['dept_id', 'dept_name'], [[1, 'Marketing'], [2, 'Operations']]), 'employees': (['emp_id', 'dept_id', 'emp_name'], [[1, 1, 'Frank'], [2, 1, 'Grace'], [3, 2, 'Heidi'], [4, 2, 'Ivan']]), 'expenses': (['expense_id', 'emp_id', 'amount', 'expense_date'], [[1, 1, 30000, '2024-02-10'], [2, 1, 30000, '2024-02-15'], [3, 3, 20000, '2024-01-20'], [4, 4, 10000, '2024-03-10']])}, 'expected': [['Marketing', 60000, 30000]]}]


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
