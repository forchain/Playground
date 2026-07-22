import unittest
from solution import solution

class SolutionTests(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(solution(*('abcd', 'abcxyz')), 'abc')

    def test_example_2(self):
        self.assertEqual(solution(*('hello', 'world')), '')

if __name__ == "__main__":
    unittest.main()
