import unittest

from solution import min_difference


class SolutionTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(min_difference([7,3,2,4,9,12,56], 3), 2)
        self.assertEqual(min_difference([6,8,11,21,90,49], 4), 15)


if __name__ == '__main__':
    unittest.main()
