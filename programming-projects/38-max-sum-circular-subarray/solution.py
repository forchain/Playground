def solution(array: list[int]) -> int:
    """返回非空环形连续子数组的最大和。"""
    total = array[0]
    max_ending = min_ending = array[0]
    max_sum = min_sum = array[0]
    for value in array[1:]:
        max_ending = max(value, max_ending + value)
        min_ending = min(value, min_ending + value)
        max_sum = max(max_sum, max_ending)
        min_sum = min(min_sum, min_ending)
        total += value
    # 全负时 total-min_sum 会得到空数组，必须返回普通 Kadane 的结果。
    return max_sum if max_sum < 0 else max(max_sum, total - min_sum)
