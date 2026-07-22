async def solution(country_index, getCountry, getStates):
    """平台函数以参数注入，便于独立运行和测试。"""
    try:
        country = await getCountry(country_index)
        states = await getStates(country)
    except Exception:
        return f"ind = {country_index} invalid"
    # max 在相同人口时稳定返回列表中最先出现的州。
    return max(states, key=lambda state: state["population"])["name"]
