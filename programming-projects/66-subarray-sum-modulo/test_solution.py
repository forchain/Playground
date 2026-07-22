import unittest
from solution import solution
class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution(5, 7, [3,3,9,9,5]), 6)
        self.assertEqual(solution(3, 6, [1,2,3]), 5)
if __name__ == "__main__": unittest.main()
