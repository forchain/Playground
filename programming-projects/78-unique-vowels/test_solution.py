import unittest
from solution import solution
class TestSolution(unittest.TestCase):
    def test_table_cases(self):
        self.assertEqual(solution(["eiqwa","aaabc","aheo","iou"], 3), 3)
        self.assertEqual(solution(["aa","bhg","aeo","lia"], 2), 1)
        self.assertEqual(solution(["anhj","berq","lopa"], 1), 2)
if __name__ == "__main__": unittest.main()
