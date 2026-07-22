import unittest

from solution import count_unique_triplets


class SolutionTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_unique_triplets([1,0,2,6,3,9],11), 2)
        self.assertEqual(count_unique_triplets([1,2,6,3,4,5,9,10,11],20), 5)
        self.assertEqual(count_unique_triplets([1,1,4,5,4,5],10), 1)


if __name__ == '__main__':
    unittest.main()
