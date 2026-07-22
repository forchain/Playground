import unittest
from solution import solution
class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution("float", "arose"), "ao")
        self.assertEqual(solution("equivalent", "fraction"), "ai")
if __name__ == "__main__": unittest.main()
