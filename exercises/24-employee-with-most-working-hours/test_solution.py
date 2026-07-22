import sqlite3
import unittest
from pathlib import Path


CASES = [{'tables': {'employees': (['emp_id', 'emp_name', 'department'], [[1, 'Alice', 'HR'], [2, 'Bob', 'IT'], [3, 'Carol', 'Finance'], [4, 'David', 'IT']]), 'projects': (['project_id', 'emp_id', 'project_name', 'hours_worked', 'start_date'], [[1, 1, 'Recruitment', 20, '2023-01-15'], [2, 1, 'Training', 30, '2023-02-10'], [3, 2, 'DevOps', 50, '2023-03-20'], [4, 3, 'Auditing', 25, '2023-01-05'], [5, 3, 'Budgeting', 30, '2023-04-10'], [6, 4, 'Infrastructure', 40, '2022-12-15']])}, 'expected': [['Carol', 55, 2], ['Alice', 50, 2], ['Bob', 50, 1]]}, {'tables': {'employees': (['emp_id', 'emp_name', 'department'], [[1, 'Frank', 'Sales'], [2, 'Grace', 'IT'], [3, 'Heidi', 'Finance'], [4, 'Ivan', 'Marketing'], [5, 'Judy', 'Sales']]), 'projects': (['project_id', 'emp_id', 'project_name', 'hours_worked', 'start_date'], [[1, 1, 'SalesPitch', 60, '2023-11-01'], [2, 2, 'ServerSetup', 45, '2023-10-10'], [3, 3, 'Auditing', 50, '2023-08-20'], [4, 4, 'Campaigns', 30, '2022-11-05'], [5, 5, 'ColdCalling', 40, '2023-09-15'], [6, 5, 'Outreach', 30, '2023-12-01']])}, 'expected': [['Judy', 70, 2], ['Frank', 60, 1], ['Heidi', 50, 1]]}]


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
