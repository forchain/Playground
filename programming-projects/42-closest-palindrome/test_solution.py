import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution("123"), "121")
        self.assertEqual(solution("1"), "0")
        self.assertEqual(solution("808"), "818")

if __name__ == "__main__":
    unittest.main()
