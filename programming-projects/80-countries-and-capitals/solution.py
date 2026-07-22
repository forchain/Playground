async def solution(country_index, getCountry, getCapitalFromCountry,
                   getPopulationFromCapital):
    country = getCountry(country_index)
    if country is None:
        return f"No country found at ind = {country_index}"
    try:
        capital = await getCapitalFromCountry(country)
    except Exception:
        return f"No capital found for country at ind = {country_index}"
    population = getPopulationFromCapital(capital)
    return f"{country}, {capital}, {population}"
