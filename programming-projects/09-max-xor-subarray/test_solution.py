import unittest
from solution import solution

class SolutionTests(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(solution(*(4, [1, 2, 3, 4])), 7)

    def test_example_2(self):
        self.assertEqual(solution(*(5, [8, 1, 2, 12, 7])), 15)

if __name__ == "__main__":
    unittest.main()
