import unittest
from solution import solution

class SolutionTests(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(solution(*(5, [2, 3, 6, 6, 5])), 5)

    def test_example_2(self):
        self.assertEqual(solution(*(3, [10, 10, 10])), -1)

    def test_example_3(self):
        self.assertEqual(solution(*(6, [1, 2, 3, 4, 5, 4])), 4)

if __name__ == "__main__":
    unittest.main()
