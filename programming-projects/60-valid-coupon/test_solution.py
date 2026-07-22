import unittest

from solution import validate_coupon


class SolutionTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(validate_coupon('AVG190420T'), 'A')
        self.assertEqual(validate_coupon('1234XYZ'), 'Z')


if __name__ == '__main__':
    unittest.main()
