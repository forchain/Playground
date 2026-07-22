def solution(s: str) -> int:
    """返回最长回文子序列的长度。"""
    n = len(s)
    if n == 0:
        return 0
    dp = [1] * n
    for left in range(n - 2, -1, -1):
        diagonal = 0
        for right in range(left + 1, n):
            old = dp[right]
            if s[left] == s[right]:
                dp[right] = diagonal + 2
            else:
                dp[right] = max(dp[right], dp[right - 1])
            diagonal = old
    return dp[-1]
