import unittest
from solution import solution
class TestSolution(unittest.TestCase):
    def test_example_dataset(self):
        dataset = [{"id":1,"salary":3000,"manager":False,"num_days_off":8},
                   {"id":2,"salary":5000,"manager":True,"num_days_off":10},
                   {"id":3,"salary":6000,"manager":True,"num_days_off":14}]
        self.assertEqual(solution(dataset), (6000,24))
if __name__ == "__main__": unittest.main()
