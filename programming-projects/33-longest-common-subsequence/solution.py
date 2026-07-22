def solution(s1: str, s2: str) -> int:
    """返回两个字符串的最长公共子序列长度。"""
    if len(s1) < len(s2):
        s1, s2 = s2, s1
    dp = [0] * (len(s2) + 1)
    for char1 in s1:
        diagonal = 0
        for j, char2 in enumerate(s2, 1):
            old = dp[j]
            if char1 == char2:
                dp[j] = diagonal + 1
            else:
                dp[j] = max(dp[j], dp[j - 1])
            diagonal = old
    return dp[-1]
