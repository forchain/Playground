import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution([1, 2, 5, 3, 2, 1]), 6)
        self.assertEqual(solution([1, 11, 2, 10, 4, 5, 2, 1]), 6)
        self.assertEqual(solution([12, 11, 40, 5, 3]), 4)

if __name__ == "__main__":
    unittest.main()
