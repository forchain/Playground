import unittest
from solution import solution

class SolutionTests(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(solution(*(5, [1, 2, 3, 4, 5], 2)), [4, 5, 1, 2, 3])

    def test_example_2(self):
        self.assertEqual(solution(*(6, [10, 20, 30, 40, 50, 60], 4)), [30, 40, 50, 60, 10, 20])

if __name__ == "__main__":
    unittest.main()
