import sqlite3
import unittest
from pathlib import Path


CASES = [{'tables': {'books': (['id', 'title', 'author'], [[1, 'Alice in Wonderland', 'Lewis Carroll'], [2, 'Romeo and Juliet', 'William Shakespeare'], [3, "The Emperor's New Mind", 'Roger Penrose'], [4, 'The Extended Phenotype', 'Richard Dawkins'], [5, 'Flatland: A Romance of Many Dimensions', 'Edwin Abbott Abbott'], [6, 'Elements', 'Euclid'], [7, 'Philosophiæ Naturalis Principia Mathematica', 'Isaac Newton']])}, 'expected': [['Alice in Wonderland'], ['Elements'], ['Flatland: A Romance of Many Dimensions'], ['Philosophiæ Naturalis Principia Mathematica'], ['Romeo and Juliet'], ["The Emperor's New Mind"], ['The Extended Phenotype'], ['Edwin Abbott Abbott'], ['Euclid'], ['Isaac Newton'], ['Lewis Carroll'], ['Richard Dawkins'], ['Roger Penrose'], ['William Shakespeare']]}, {'tables': {'books': (['id', 'title', 'author'], [[1, 1984, 'George Orwell'], [2, 'Brave New World', 'Aldous Huxley'], [3, 'To Kill a Mockingbird', 'Harper Lee'], [4, 'Moby-Dick', 'Herman Melville'], [5, 'Pride and Prejudice', 'Jane Austen'], [6, 'The Great Gatsby', 'F. Scott Fitzgerald'], [7, 'War and Peace', 'Leo Tolstoy']])}, 'expected': [['1984'], ['Brave New World'], ['Moby-Dick'], ['Pride and Prejudice'], ['The Great Gatsby'], ['To Kill a Mockingbird'], ['War and Peace'], ['Aldous Huxley'], ['F. Scott Fitzgerald'], ['George Orwell'], ['Harper Lee'], ['Herman Melville'], ['Jane Austen'], ['Leo Tolstoy']]}]


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
