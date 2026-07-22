import unittest
from solution import solution

class SolutionTests(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(solution(*('abcabcbb',)), 3)

    def test_example_2(self):
        self.assertEqual(solution(*('bbbbb',)), 1)

    def test_example_3(self):
        self.assertEqual(solution(*('pwwkew',)), 3)

if __name__ == "__main__":
    unittest.main()
