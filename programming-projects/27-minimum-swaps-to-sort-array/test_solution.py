import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution([3, 1, 2, 5, 4]), 3)
        self.assertEqual(solution([4, 3, 2, 1]), 2)

if __name__ == "__main__":
    unittest.main()
