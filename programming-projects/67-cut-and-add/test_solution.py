import unittest
from solution import solution
class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution("AbcDef", 1, 2), 4)
        self.assertEqual(solution("abcabc", 1, 1), 3)
if __name__ == "__main__": unittest.main()
