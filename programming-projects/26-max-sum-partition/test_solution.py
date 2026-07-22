import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution([1, 3, -1, 2, 5]), 11)
        self.assertEqual(solution([-2, -1, -3, -4]), -1)
        self.assertEqual(solution([4, 2, 1, 6, 3, 8]), 24)

if __name__ == "__main__":
    unittest.main()
