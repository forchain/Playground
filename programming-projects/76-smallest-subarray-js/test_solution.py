import unittest
from solution import minSubarrayLength
class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minSubarrayLength(2, [1,3]), 2)
        self.assertEqual(minSubarrayLength(1, [2]), 1)
        self.assertEqual(minSubarrayLength(7, [1,5,10,7,1,9,4]), 3)
if __name__ == "__main__": unittest.main()
