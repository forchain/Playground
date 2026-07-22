import sqlite3
import unittest
from pathlib import Path


CASES = [{'tables': {'authors': (['author_id', 'author_name'], [[1, 'Emma'], [2, 'Sophia'], [3, 'Mark']]), 'books': (['book_id', 'author_id', 'title', 'year_published'], [[1, 1, 'Life After Life', 2013], [2, 1, 'Under the Apple Tree', 1995], [3, 2, 'Another Day', 2001], [4, 3, 'Z is for Zebra', 2010]])}, 'expected': [['Life After Life'], ['Another Day']]}, {'tables': {'authors': (['author_id', 'author_name'], [[1, 'Elena'], [2, 'Clara'], [3, 'Anna']]), 'books': (['book_id', 'author_id', 'title', 'year_published'], [[1, 1, "Zorro's Escape", 2002], [2, 1, 'Aqua Blue', 2010], [3, 2, 'Mango Street', 2005], [4, 2, 'Yellow Moon', 1999], [5, 3, 'Alpha Beta', 2021]])}, 'expected': [['Alpha Beta'], ['Mango Street'], ['Aqua Blue'], ["Zorro's Escape"]]}]


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
