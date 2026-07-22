import unittest

from solution import encode_message


class SolutionTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(encode_message('moirarose'), 'ptf13o9rar')
        self.assertEqual(encode_message('AlexisRose'), 'invalid')


if __name__ == '__main__':
    unittest.main()
