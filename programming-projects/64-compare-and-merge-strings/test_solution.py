import unittest

from solution import compare_and_merge


class SolutionTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(compare_and_merge('ACA','BCF'), 'ABCACF')
        self.assertEqual(compare_and_merge('RAJ','RAVI'), 'RAJRAVI')
        self.assertEqual(compare_and_merge('DAVID','ROSE'), 'DAROSEVID')


if __name__ == '__main__':
    unittest.main()
