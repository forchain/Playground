import unittest
from solution import solution
class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution(1,4,3), "-1 -3")
        self.assertEqual(solution(1,2,1), "-1 -1")
if __name__ == "__main__": unittest.main()
