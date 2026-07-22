import sqlite3
import unittest
from pathlib import Path


CASES = [{'tables': {'city': (['city_id', 'name'], [[1, 'New York'], [2, 'Los Angeles'], [3, 'Austin']]), 'accounts': (['account_id', 'account_name', 'account_type', 'city_id'], [[1, 'Nathan', 'Savings', 1], [2, 'Maria', 'Current', 2], [3, 'Rachel', 'Savings', 1], [4, 'Rose', 'Savings', 3], [5, 'Roger', 'Current', 1]]), 'transactions': (['transaction_id', 'account_id', 'transaction_type', 'amount', 'date'], [[1, 1, 'Credit', 1000, '2017-05-27'], [2, 1, 'Credit', 200, '2017-05-02'], [3, 3, 'Credit', 1500, '2017-05-27'], [4, 2, 'Savings', 332, '2017-02-23'], [5, 3, 'Credit', 1700, '2017-05-21']])}, 'expected': [['Nathan'], ['Rachel']]}, {'tables': {'city': (['city_id', 'name'], [[1, 'New York'], [2, 'Dallas'], [3, 'Houston']]), 'accounts': (['account_id', 'account_name', 'account_type', 'city_id'], [[1, 'Nathan', 'Savings', 1], [2, 'Mira', 'Current', 2], [3, 'Rose', 'Savings', 1], [4, 'David', 'Savings', 3], [5, 'Roger', 'Current', 1]]), 'transactions': (['transaction_id', 'account_id', 'transaction_type', 'amount', 'date'], [[1, 1, 'Credit', 1000, '2017-05-27'], [2, 1, 'Credit', 200, '2017-05-02'], [3, 1, 'Credit', 1500, '2017-05-27'], [4, 2, 'Savings', 332, '2017-02-23'], [5, 3, 'Credit', 1700, '2017-05-21']])}, 'expected': [['Nathan']]}]


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
