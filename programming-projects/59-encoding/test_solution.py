import unittest

from solution import encode


class SolutionTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(encode('start',1357), '20,23,6,25,21')
        self.assertEqual(encode('masterpiece',1939), '14,10,22,29,6,27,19,18,6,12,8')


if __name__ == '__main__':
    unittest.main()
