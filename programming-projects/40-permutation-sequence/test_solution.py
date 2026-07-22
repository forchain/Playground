import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution(3, 3), "213")
        self.assertEqual(solution(4, 9), "2314")
        self.assertEqual(solution(2, 2), "21")

if __name__ == "__main__":
    unittest.main()
