import unittest

from solution import expensive_words


class SolutionTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(expensive_words('abc ABC Abc'), 24)
        self.assertEqual(expensive_words('ab-c A-BC'), 18)


if __name__ == '__main__':
    unittest.main()
