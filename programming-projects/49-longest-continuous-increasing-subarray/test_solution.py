import unittest

from solution import longest_increasing_subarray


class SolutionTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(longest_increasing_subarray([1,3,5,4,7,8,9]), 4)
        self.assertEqual(longest_increasing_subarray([2,4,6,5,8]), 3)


if __name__ == '__main__':
    unittest.main()
