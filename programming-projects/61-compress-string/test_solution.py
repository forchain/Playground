import unittest

from solution import compress_string


class SolutionTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(compress_string('ahaee'), 'a2he2')
        self.assertEqual(compress_string('a'), 'a')


if __name__ == '__main__':
    unittest.main()
