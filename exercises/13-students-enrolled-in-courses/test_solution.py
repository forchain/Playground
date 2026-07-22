import sqlite3
import unittest
from pathlib import Path


CASES = [{'tables': {'students': (['student_id', 'student_name', 'age'], [[1, 'Alice', 20], [2, 'Bob', 22], [3, 'Carol', 19]]), 'courses': (['course_id', 'student_id', 'course_name', 'grade'], [[1, 1, 'Math', 85], [2, 1, 'Science', 90], [3, 2, 'Math', 75], [4, 2, 'Science', 80], [5, 3, 'History', 88]])}, 'expected': [['Alice']]}, {'tables': {'students': (['student_id', 'student_name', 'age'], [[1, 'Dave', 21], [2, 'Eve', 23], [3, 'Frank', 20]]), 'courses': (['course_id', 'student_id', 'course_name', 'grade'], [[1, 1, 'English', 95], [2, 1, 'History', 88], [3, 2, 'English', 70], [4, 3, 'Math', 85], [5, 3, 'Science', 90]])}, 'expected': [['Dave'], ['Frank']]}]


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
