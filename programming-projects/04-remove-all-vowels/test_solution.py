import unittest
from solution import solution

class SolutionTests(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(solution(*('hello world',)), 'hll wrld')

    def test_example_2(self):
        self.assertEqual(solution(*('Programming is fun!',)), 'Prgrmmng s fn!')

if __name__ == "__main__":
    unittest.main()
