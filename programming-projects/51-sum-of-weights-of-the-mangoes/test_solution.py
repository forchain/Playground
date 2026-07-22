import unittest

from solution import count_fair_removals


class SolutionTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_fair_removals([3,1,7,4]), 1)
        self.assertEqual(count_fair_removals([3,3,3]), 3)


if __name__ == '__main__':
    unittest.main()
