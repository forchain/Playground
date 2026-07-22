import unittest
from solution import solution

class SolutionTests(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(solution(*('abcde', 'deabc')), 3)

    def test_example_2(self):
        self.assertEqual(solution(*('hello', 'lohel')), 3)

    def test_example_3(self):
        self.assertEqual(solution(*('abc', 'cabd')), -1)

if __name__ == "__main__":
    unittest.main()
