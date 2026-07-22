import unittest
from solution import solution

class SolutionTests(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(solution(*(5, [2, 3, -2, 4, -1])), 48)

    def test_example_2(self):
        self.assertEqual(solution(*(4, [-2, 0, -1, 3])), 3)

if __name__ == "__main__":
    unittest.main()
