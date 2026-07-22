import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution([1,2,3,4,5]), 6)
        self.assertEqual(solution([10,20,30,40]), 40)
        self.assertEqual(solution([7,7,7]), 0)

if __name__ == "__main__":
    unittest.main()
