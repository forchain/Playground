import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution("ababc"), 2)
        self.assertEqual(solution("aaaa"), 2)
        self.assertEqual(solution("abcdef"), 0)

if __name__ == "__main__":
    unittest.main()
