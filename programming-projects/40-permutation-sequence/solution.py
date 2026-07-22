from math import factorial

def solution(n: int, k: int) -> str:
    """返回 1..n 的第 k 个字典序排列（k 从 1 开始）。"""
    numbers = [str(value) for value in range(1, n + 1)]
    k -= 1  # 转为从 0 开始的排名
    result = []
    for remaining in range(n, 0, -1):
        block_size = factorial(remaining - 1)
        index, k = divmod(k, block_size)
        # 每个首元素对应 (remaining-1)! 个连续排列。
        result.append(numbers.pop(index))
    return "".join(result)
