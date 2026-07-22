import unittest

from solution import minimum_bill_count


class SolutionTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_bill_count(101,[1,10,20]), 6)
        self.assertEqual(minimum_bill_count(1050,[1,10,20,100]), 13)
        self.assertEqual(minimum_bill_count(55,[1,5,10,50]), 2)


if __name__ == '__main__':
    unittest.main()
