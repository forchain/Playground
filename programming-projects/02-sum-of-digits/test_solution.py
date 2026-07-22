import unittest
from solution import solution

class SolutionTests(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(solution(*(123,)), 6)

    def test_example_2(self):
        self.assertEqual(solution(*(-2059,)), 16)

    def test_example_3(self):
        self.assertEqual(solution(*(0,)), 0)

if __name__ == "__main__":
    unittest.main()
