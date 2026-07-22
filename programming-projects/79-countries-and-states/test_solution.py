import unittest
from solution import solution

COUNTRIES = ["India", "USA"]
STATES = {"India": [{"name":"Karnataka","population":200},{"name":"Maharashtra","population":130}],
          "USA": [{"name":"Michigan","population":120},{"name":"Virginia","population":48}]}
async def get_country(index):
    if index >= len(COUNTRIES): raise ValueError("Error")
    return COUNTRIES[index]
async def get_states(country): return STATES[country]

class TestSolution(unittest.IsolatedAsyncioTestCase):
    async def test_examples(self):
        self.assertEqual(await solution(0,get_country,get_states), "Karnataka")
        self.assertEqual(await solution(1,get_country,get_states), "Michigan")
        self.assertEqual(await solution(10000,get_country,get_states), "ind = 10000 invalid")
if __name__ == "__main__": unittest.main()
