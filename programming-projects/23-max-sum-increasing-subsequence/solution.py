def solution(array: list[int]) -> int:
    """返回严格递增子序列的最大元素和。"""
    if not array:
        return 0
    # dp[i] 是以 array[i] 结尾的最优和；单独选择当前元素是初值。
    dp = array.copy()
    for i in range(len(array)):
        for j in range(i):
            if array[j] < array[i]:
                dp[i] = max(dp[i], dp[j] + array[i])
    return max(dp)
