import unittest
from solution import solution
class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution(25), 1)
        self.assertEqual(solution(8), 0)
if __name__ == "__main__": unittest.main()
