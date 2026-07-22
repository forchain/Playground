import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution([[1,2,3],[4,5,6],[7,8,9]]), 29)
        self.assertEqual(solution([[-1,-2],[-3,-4]]), -7)
        self.assertEqual(solution([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]), 73)

if __name__ == "__main__":
    unittest.main()
