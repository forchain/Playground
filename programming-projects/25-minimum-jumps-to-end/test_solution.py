import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution([2, 3, 1, 1, 4]), 2)
        self.assertEqual(solution([1, 0, 0, 0, 0]), -1)
        self.assertEqual(solution([0]), 0)

if __name__ == "__main__":
    unittest.main()
