import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution("aabaab"), 3)
        self.assertEqual(solution("abcdef"), 0)
        self.assertEqual(solution("levellevel"), 5)

if __name__ == "__main__":
    unittest.main()
