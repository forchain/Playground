import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution("abcde", "ace"), 3)
        self.assertEqual(solution("abc", "def"), 0)
        self.assertEqual(solution("abcde", "abcde"), 5)

if __name__ == "__main__":
    unittest.main()
