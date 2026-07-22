import sqlite3
import unittest
from pathlib import Path


CASES = [{'tables': {'users': (['user_id', 'username'], [[1, 'Harry'], [2, 'George'], [3, 'Charles'], [4, 'Meghan'], [5, 'Kate']]), 'posts': (['post_id', 'user_id', 'post_content'], [[1, 1, 'Post A'], [2, 1, 'Post B'], [3, 2, 'Post C'], [4, 3, 'Post D'], [5, 3, 'Post E']]), 'likes': (['like_id', 'user_id', 'post_id'], [[1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 2, 2], [5, 3, 2], [6, 4, 2], [7, 1, 3], [8, 3, 3], [9, 4, 3]])}, 'expected': [['George'], ['Charles'], ['Meghan']]}, {'tables': {'users': (['user_id', 'username'], [[1, 'Harry'], [2, 'George'], [3, 'Charles'], [4, 'Meghan'], [5, 'Kate']]), 'posts': (['post_id', 'user_id', 'post_content'], [[1, 1, 'Post A'], [2, 1, 'Post B'], [3, 2, 'Post C'], [4, 3, 'Post D'], [5, 3, 'Post E']]), 'likes': (['like_id', 'user_id', 'post_id'], [[1, 5, 1], [2, 3, 1], [3, 4, 1], [4, 5, 2], [5, 3, 2], [6, 4, 2], [7, 2, 2], [8, 3, 3], [9, 4, 3]])}, 'expected': [['Charles'], ['Meghan'], ['Kate']]}]


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
