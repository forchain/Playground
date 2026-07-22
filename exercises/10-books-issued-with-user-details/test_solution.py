import sqlite3
import unittest
from pathlib import Path


CASES = [{'tables': {'users': (['user_id', 'name', 'email', 'phone_number'], [[1, 'Alfreds Futterkiste', 'alfreds@gmail.com', 987654321], [2, 'Willian Mathew', 'william@gmail.com', 868686888], [3, 'David Smith', 'david@gmail.com', 798575757], [4, 'Alex hales', 'alexhales@gmail.com', 86888688], [5, 'Michael richard', 'michael@gmail.com', 98765443]]), 'books': (['book_id', 'book_name'], [[1, 'The Power of Now'], [2, 'Leo'], [3, 'The Electronic Swagman'], [4, 'Brutal Simplicity of thought'], [5, 'Life Lessons']]), 'books_issued': (['issue_id', 'book_id', 'user_id', 'return_status', 'date_of_return'], [[1, 1, 1, 'Yes', '2017-04-15'], [2, 1, 2, 'No', '2019-07-19'], [3, 2, 2, 'No', '2022-11-23'], [4, 3, 3, 'Yes', '2022-04-15'], [5, 1, 1, 'Yes', '2022-02-18']])}, 'expected': [['The Power of Now', 'Alfreds Futterkiste'], ['The Power of Now', 'Alfreds Futterkiste'], ['The Power of Now', 'Willian Mathew'], ['Leo', 'Willian Mathew'], ['The Electronic Swagman', 'David Smith']]}, {'tables': {'users': (['user_id', 'name', 'email', 'phone_number'], [[1, 'Alfreds Futterkiste', 'alfreds@gmail.com', 987654321], [2, 'Willian Mathew', 'william@gmail.com', 868686888], [3, 'Michael', 'michael@gmail.com', 798575757], [4, 'Alex hales', 'alexhales@gmail.com', 86888688], [5, 'Michael richard', 'michael@gmail.com', 98765443]]), 'books': (['book_id', 'book_name'], [[1, 'The Power of Now'], [2, 'Leo'], [3, 'The Electronic Swagman'], [4, 'Brutal Simplicity of thought'], [5, 'Life Lessons']]), 'books_issued': (['issue_id', 'book_id', 'user_id', 'return_status', 'date_of_return'], [[1, 1, 1, 'Yes', '2017-04-15'], [2, 1, 2, 'No', '2019-07-19'], [3, 2, 2, 'No', '2022-11-23'], [4, 3, 3, 'Yes', '2022-04-15'], [5, 1, 1, 'Yes', '2022-02-18']])}, 'expected': [['The Power of Now', 'Alfreds Futterkiste'], ['The Power of Now', 'Alfreds Futterkiste'], ['The Power of Now', 'Willian Mathew'], ['Leo', 'Willian Mathew'], ['The Electronic Swagman', 'Michael']]}]


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
