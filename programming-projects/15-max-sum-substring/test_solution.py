import unittest
from solution import solution

class SolutionTests(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(solution(*('9875',)), 29)

    def test_example_2(self):
        self.assertEqual(solution(*('1234',)), 4)

    def test_example_3(self):
        self.assertEqual(solution(*('404',)), 4)

if __name__ == "__main__":
    unittest.main()
