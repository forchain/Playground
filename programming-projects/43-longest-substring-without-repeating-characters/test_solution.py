import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution("abcabcbb"), 3)
        self.assertEqual(solution("abcda"), 4)
        self.assertEqual(solution("aaacbb"), 3)

if __name__ == "__main__":
    unittest.main()
