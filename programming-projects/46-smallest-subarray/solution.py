def min_subarray_length(values: list[int]) -> int:
    low, high = min(values), max(values)
    if low == high:
        return 1
    last_low = last_high = -1
    answer = len(values)
    for index, value in enumerate(values):
        if value == low:
            last_low = index
        if value == high:
            last_high = index
        # 最近的一对极值位置给出以当前位置相关的最短候选区间。
        if last_low >= 0 and last_high >= 0:
            answer = min(answer, abs(last_low - last_high) + 1)
    return answer
