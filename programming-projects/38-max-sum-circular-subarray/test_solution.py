import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution([1,-2,3,-2]), 3)
        self.assertEqual(solution([5,-3,5]), 10)
        self.assertEqual(solution([-3,-2,-1]), -1)

if __name__ == "__main__":
    unittest.main()
