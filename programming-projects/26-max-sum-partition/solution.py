def solution(arr: list[int]) -> int:
    """返回任意连续分段后，各段最大值之和的最大值。"""
    if not arr:
        return 0
    # 正数单独成段才不会损失；非正数合并后只贡献其中最大者。
    positive_sum = sum(value for value in arr if value > 0)
    return positive_sum if positive_sum else max(arr)
