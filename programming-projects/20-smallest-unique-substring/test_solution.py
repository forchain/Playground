import unittest
from solution import solution

class SolutionTests(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(solution(*('abcaacbb',)), 3)

    def test_example_2(self):
        self.assertEqual(solution(*('aaa',)), 1)

    def test_example_3(self):
        self.assertEqual(solution(*('abcdef',)), 6)

if __name__ == "__main__":
    unittest.main()
