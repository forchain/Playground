import unittest

from solution import max_sum_column


class SolutionTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_sum_column([4,14,12,7,14,16,5,13,7,16,11,19], 4), 2)
        self.assertEqual(max_sum_column([14,9,19,6,13,13,24,2,12], 3), 1)


if __name__ == '__main__':
    unittest.main()
