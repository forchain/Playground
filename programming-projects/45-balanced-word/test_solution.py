import unittest

from solution import balanced_word


class SolutionTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(balanced_word('zips'), 1)
        self.assertEqual(balanced_word('bray'), 0)
        self.assertEqual(balanced_word('arise'), -1)


if __name__ == '__main__':
    unittest.main()
