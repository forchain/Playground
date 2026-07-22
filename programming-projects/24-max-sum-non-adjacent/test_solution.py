import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution([3, 2, 7, 10, 12]), 22)
        self.assertEqual(solution([-1, 2, 9, -4]), 9)
        self.assertEqual(solution([5, 5, 10, 100, 10, 5]), 110)

if __name__ == "__main__":
    unittest.main()
