import unittest
from solution import solution

class SolutionTests(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(solution(*('The quick brown fox',)), 5)

    def test_example_2(self):
        self.assertEqual(solution(*('A journey of a thousand miles begins with a single step',)), 8)

if __name__ == "__main__":
    unittest.main()
