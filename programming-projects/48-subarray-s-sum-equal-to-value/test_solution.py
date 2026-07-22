import unittest

from solution import count_subarrays


class SolutionTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_subarrays([1,2,3,-3,1], 3), 4)
        self.assertEqual(count_subarrays([1,1,1], 2), 2)


if __name__ == '__main__':
    unittest.main()
