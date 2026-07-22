import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution([1, 101, 2, 3, 100, 4]), 106)
        self.assertEqual(solution([10, 5, 4, 3, 2]), 10)
        self.assertEqual(solution([3, 4, 5, 10, 1, 2, 3]), 22)

if __name__ == "__main__":
    unittest.main()
