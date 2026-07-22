import unittest

from solution import smallest_subarray_over


class SolutionTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(smallest_subarray_over([1,4,45,6,0,19], 51), 3)
        self.assertEqual(smallest_subarray_over([1,10,3,40,18], 50), 2)

    def test_negative_values(self):
        self.assertEqual(smallest_subarray_over([2, -1, 2, 5], 4), 1)


if __name__ == '__main__':
    unittest.main()
