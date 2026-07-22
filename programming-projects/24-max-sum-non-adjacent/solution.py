def solution(array: list[int]) -> int:
    """返回不选择相邻元素时可得到的最大和，允许一个都不选。"""
    skip = take = 0
    for value in array:
        # 新的 take 只能接在此前 skip 后；新的 skip 取此前两种状态较优者。
        skip, take = max(skip, take), skip + value
    return max(skip, take)
