import unittest
from solution import solution
class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution(4,2,[12,34,67,90]), 113)
        self.assertEqual(solution(3,2,[15,17,20]), 32)
if __name__ == "__main__": unittest.main()
