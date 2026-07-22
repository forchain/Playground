import unittest
from solution import solution

class SolutionTests(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(solution(*(5, [3, 3, 4, 2, 3])), 3)

    def test_example_2(self):
        self.assertEqual(solution(*(4, [1, 2, 3, 4])), -1)

    def test_example_3(self):
        self.assertEqual(solution(*(6, [2, 2, 1, 1, 1, 2])), -1)

if __name__ == "__main__":
    unittest.main()
