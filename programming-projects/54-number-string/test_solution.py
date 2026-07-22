import unittest

from solution import expanded_form


class SolutionTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(expanded_form(35), '30 + 5')
        self.assertEqual(expanded_form(73), '70 + 3')


if __name__ == '__main__':
    unittest.main()
