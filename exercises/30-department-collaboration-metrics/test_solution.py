import sqlite3
import unittest
from pathlib import Path


CASES = [{'tables': {'departments': (['dept_id', 'dept_name'], [[1, 'HR'], [2, 'IT'], [3, 'Finance'], [4, 'Marketing'], [5, 'Operations']]), 'collaborations': (['collab_id', 'dept_id_1', 'dept_id_2', 'hours_worked'], [[1, 1, 2, 40], [2, 1, 3, 60], [3, 1, 4, 20], [4, 2, 3, 50], [5, 2, 5, 30], [6, 3, 4, 40], [7, 4, 5, 70]])}, 'expected': [['Finance', 150, 3], ['Marketing', 130, 3], ['HR', 120, 3], ['IT', 120, 3]]}, {'tables': {'departments': (['dept_id', 'dept_name'], [[1, 'Sales'], [2, 'Support'], [3, 'Logistics'], [4, 'Research and Development'], [5, 'Legal']]), 'collaborations': (['collab_id', 'dept_id_1', 'dept_id_2', 'hours_worked'], [[1, 1, 2, 50], [2, 1, 3, 80], [3, 1, 4, 20], [4, 2, 3, 60], [5, 2, 5, 40], [6, 3, 4, 90], [7, 4, 5, 30]])}, 'expected': [['Logistics', 230, 3], ['Sales', 150, 3], ['Support', 150, 3], ['Research and Development', 140, 3]]}]


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
