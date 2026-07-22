import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution([[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]])
        self.assertEqual(solution([[1,4],[4,5],[6,8]]), [[1,5],[6,8]])

if __name__ == "__main__":
    unittest.main()
