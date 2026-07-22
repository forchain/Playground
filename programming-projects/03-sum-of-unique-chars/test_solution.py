import unittest
from solution import solution

class SolutionTests(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(solution(*('abc',)), 294)

    def test_example_2(self):
        self.assertEqual(solution(*('abac',)), 197)

    def test_example_3(self):
        self.assertEqual(solution(*('xyzwx',)), 362)

if __name__ == "__main__":
    unittest.main()
