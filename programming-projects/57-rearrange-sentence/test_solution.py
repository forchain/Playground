import unittest

from solution import rearrange_sentence


class SolutionTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(rearrange_sentence('is2 Thi1s T4est 3a'), 'This is a Test')
        self.assertEqual(rearrange_sentence('is3 Cri1stiano 4the Rona2ldo 5best'), 'Cristiano Ronaldo is the best')


if __name__ == '__main__':
    unittest.main()
