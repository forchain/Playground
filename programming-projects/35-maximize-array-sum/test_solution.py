import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution([-2,0,5,-1,-3], 4), 11)
        self.assertEqual(solution([-5,-2,-3], 2), 6)

if __name__ == "__main__":
    unittest.main()
