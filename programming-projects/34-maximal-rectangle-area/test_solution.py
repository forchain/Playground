import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution([[1,0,1,0],[1,0,1,1],[1,1,1,1],[1,0,0,1]]), 4)
        self.assertEqual(solution([[0,1,1],[1,1,1],[1,1,0]]), 4)

if __name__ == "__main__":
    unittest.main()
