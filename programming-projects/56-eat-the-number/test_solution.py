import unittest

from solution import eat_numbers


class SolutionTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(eat_numbers([5,3,7,30]), [15,30])
        self.assertEqual(eat_numbers([5,1,4]), [10])


if __name__ == '__main__':
    unittest.main()
