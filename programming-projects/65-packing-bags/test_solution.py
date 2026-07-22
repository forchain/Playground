import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(solution(12, [2,1,2,5,4,3,6,1,1,9,3,2], 4))
        self.assertFalse(solution(11, [2,7,1,3,3,4,7,4,1,8,2], 4))

if __name__ == "__main__": unittest.main()
