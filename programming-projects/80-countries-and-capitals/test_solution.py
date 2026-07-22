import unittest
from solution import solution
COUNTRIES = ["India","USA","countryA"]
CAPITALS = {"India":"New Delhi","USA":"Washington DC","countryA":None}
POPULATIONS = {"New Delhi":120,"Washington DC":80}
def get_country(i): return COUNTRIES[i] if 0 <= i < len(COUNTRIES) else None
async def get_capital(country):
    if CAPITALS[country] is None: raise ValueError("Error")
    return CAPITALS[country]
def get_population(capital): return POPULATIONS[capital]
class TestSolution(unittest.IsolatedAsyncioTestCase):
    async def test_examples(self):
        args = (get_country,get_capital,get_population)
        self.assertEqual(await solution(0,*args), "India, New Delhi, 120")
        self.assertEqual(await solution(1,*args), "USA, Washington DC, 80")
        self.assertEqual(await solution(2,*args), "No capital found for country at ind = 2")
        self.assertEqual(await solution(10000,*args), "No country found at ind = 10000")
if __name__ == "__main__": unittest.main()
