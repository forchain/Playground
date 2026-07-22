import unittest
from solution import solution

class SolutionTests(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(solution(*(6, [1, 2, 3, 4, 5, 6])), '6 1 5 2 4 3')

    def test_example_2(self):
        self.assertEqual(solution(*(5, [10, 20, 30, 40, 50])), '50 10 40 20 30')

if __name__ == "__main__":
    unittest.main()
