import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution([5,6,7]), 0)
        self.assertEqual(solution([3,9,3]), 2)
        self.assertEqual(solution([1,3,2,4,5]), 1)

if __name__ == "__main__":
    unittest.main()
