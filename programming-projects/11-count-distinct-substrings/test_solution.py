import unittest
from solution import solution

class SolutionTests(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(solution(*('abc',)), 6)

    def test_example_2(self):
        self.assertEqual(solution(*('aaa',)), 3)

if __name__ == "__main__":
    unittest.main()
