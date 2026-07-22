def solution(array: list[int], k: int) -> int:
    """返回至多翻转 k 个元素符号后可得到的最大数组和。"""
    # 因为是“至多”而非“恰好”，每个负数最多翻转一次，正数无需翻转。
    values = sorted(array)
    for i, value in enumerate(values):
        if k == 0 or value >= 0:
            break
        values[i] = -value
        k -= 1
    return sum(values)
