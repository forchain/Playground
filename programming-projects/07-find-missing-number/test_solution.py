import unittest
from solution import solution

class SolutionTests(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(solution(*(4, [1, 2, 4, 5])), 3)

    def test_example_2(self):
        self.assertEqual(solution(*(5, [2, 3, 1, 5, 6])), 4)

if __name__ == "__main__":
    unittest.main()
