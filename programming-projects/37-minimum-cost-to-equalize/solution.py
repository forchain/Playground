def solution(array: list[int]) -> int:
    """返回通过单位增减使所有元素相等的最小总成本。"""
    if not array:
        return 0
    ordered = sorted(array)
    # 绝对偏差和在任一中位数处取得最小值。
    median = ordered[len(ordered) // 2]
    return sum(abs(value - median) for value in ordered)
