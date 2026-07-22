import unittest

from solution import parentheses_score


class SolutionTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(parentheses_score('(()(()))'), 6)
        self.assertEqual(parentheses_score('()((()))'), 5)


if __name__ == '__main__':
    unittest.main()
