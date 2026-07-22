import unittest
from solution import countReleasedPrisoner
class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(countReleasedPrisoner([1,1,1]), 0)
        self.assertEqual(countReleasedPrisoner([0,0,1,1,1,0,1]), 4)
if __name__ == "__main__": unittest.main()
