import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution("abdbca"), 5)
        self.assertEqual(solution("cbbd"), 2)
        self.assertEqual(solution("a"), 1)

if __name__ == "__main__":
    unittest.main()
