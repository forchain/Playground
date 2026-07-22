import unittest
from solution import solution
class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution(3, [[1,3],[2,5],[3,6]]), 1)
        self.assertEqual(solution(4, [[4,7],[1,3],[2,5],[5,6]]), 2)
if __name__ == "__main__": unittest.main()
