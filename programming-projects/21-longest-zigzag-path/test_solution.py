import unittest
from solution import solution

class SolutionTests(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(solution(*(6, [1, 7, 4, 9, 2, 5])), 6)

    def test_example_2(self):
        self.assertEqual(solution(*(7, [1, 17, 5, 10, 13, 15, 10])), 5)

    def test_example_3(self):
        self.assertEqual(solution(*(5, [10, 10, 10, 10, 10])), 1)

if __name__ == "__main__":
    unittest.main()
