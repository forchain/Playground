def longest_increasing_subarray(values: list[int]) -> int:
    best = current = 1
    for index in range(1, len(values)):
        current = current + 1 if values[index] > values[index - 1] else 1
        best = max(best, current)
    return best
