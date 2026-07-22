import unittest
from solution import solution
class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution(5, [2,4,1,3,5]), 3)
        self.assertEqual(solution(3, [1,2,5]), 0)
if __name__ == "__main__": unittest.main()
