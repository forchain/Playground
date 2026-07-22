import unittest

from solution import min_subarray_length


class SolutionTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(min_subarray_length([1,3]), 2)
        self.assertEqual(min_subarray_length([2]), 1)
        self.assertEqual(min_subarray_length([1,5,10,7,1,9,4]), 3)


if __name__ == '__main__':
    unittest.main()
