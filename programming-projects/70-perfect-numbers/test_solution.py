import unittest
from solution import solution
class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution(7), "6")
        self.assertEqual(solution(200), "6 28")
if __name__ == "__main__": unittest.main()
