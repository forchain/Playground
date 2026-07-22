import unittest
from solution import solution

class SolutionTests(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(solution(*('aaaabbbcca',)), 'a4b3c2a')

    def test_example_2(self):
        self.assertEqual(solution(*('abcccdeeeeffff',)), 'abc3de4f4')

if __name__ == "__main__":
    unittest.main()
