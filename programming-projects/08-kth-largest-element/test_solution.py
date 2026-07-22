import unittest
from solution import solution

class SolutionTests(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(solution(*(6, [3, 2, 1, 5, 6, 4], 2)), 5)

    def test_example_2(self):
        self.assertEqual(solution(*(4, [7, 9, 3, 2], 4)), 2)

if __name__ == "__main__":
    unittest.main()
