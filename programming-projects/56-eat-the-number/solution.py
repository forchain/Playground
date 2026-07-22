def eat_numbers(values: list[int]) -> list[int]:
    eater = values[0]
    index = 1
    while index < len(values) and values[index] < eater:
        eater += values[index]
        index += 1
    return [eater] + values[index:]
