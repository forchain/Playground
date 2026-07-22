import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution("ababa"), 5)
        self.assertEqual(solution("abc"), 3)
        self.assertEqual(solution("aaa"), 3)

if __name__ == "__main__":
    unittest.main()
