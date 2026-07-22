def solution(array: list[int]) -> int:
    """返回先严格递增、后严格递减的最长子序列长度。"""
    n = len(array)
    if n == 0:
        return 0
    inc = [1] * n
    dec = [1] * n
    for i in range(n):
        for j in range(i):
            if array[j] < array[i]:
                inc[i] = max(inc[i], inc[j] + 1)
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if array[j] < array[i]:
                dec[i] = max(dec[i], dec[j] + 1)
    # 峰值在两段中被计算两次，因此减一。
    return max(inc[i] + dec[i] - 1 for i in range(n))
