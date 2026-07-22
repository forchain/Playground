def minSubarrayLength(n, arr):
    values = arr[:n]
    minimum, maximum = min(values), max(values)
    if minimum == maximum:
        return 1
    answer, last_min, last_max = n, -1, -1
    for i, value in enumerate(values):
        if value == minimum:
            last_min = i
        if value == maximum:
            last_max = i
        if last_min != -1 and last_max != -1:
            answer = min(answer, abs(last_min - last_max) + 1)
    return answer
