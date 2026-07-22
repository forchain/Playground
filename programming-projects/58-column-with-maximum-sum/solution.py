def max_sum_column(values: list[int], width: int) -> int:
    sums = [0] * width
    for index, value in enumerate(values):
        sums[index % width] += value
    # list.index 在并列时自然返回最小列号。
    return sums.index(max(sums)) + 1
