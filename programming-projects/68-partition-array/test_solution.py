import unittest
from solution import solution
class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution(4, [2,8,4,1]), 1)
        self.assertEqual(solution(3, [2,2,8]), -1)
if __name__ == "__main__": unittest.main()
