import unittest
from solution import solution
class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution("Rise and shine"), "Riseandshine")
        self.assertEqual(solution("Visual Studio Code"), "VisualStudioCode")
if __name__ == "__main__": unittest.main()
