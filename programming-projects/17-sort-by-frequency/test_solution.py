import unittest
from solution import solution

class SolutionTests(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(solution(*(6, [4, 5, 6, 5, 4, 3])), [4, 4, 5, 5, 3, 6])

    def test_example_2(self):
        self.assertEqual(solution(*(5, [1, 2, 2, 3, 3])), [2, 2, 3, 3, 1])

if __name__ == "__main__":
    unittest.main()
