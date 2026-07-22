import unittest

from solution import longest_white_run


class SolutionTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(longest_white_run('11111000'), 5)
        self.assertEqual(longest_white_run('111011101'), 7)


if __name__ == '__main__':
    unittest.main()
