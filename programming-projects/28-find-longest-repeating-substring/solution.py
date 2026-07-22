def solution(s: str) -> int:
    """返回出现至少两次且两次出现不重叠的最长子串长度。"""
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    answer = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if s[i - 1] == s[j - 1]:
                # j-i 是两个结尾之间的距离，用它限制匹配长度即可避免重叠。
                dp[i][j] = min(dp[i - 1][j - 1] + 1, j - i)
                answer = max(answer, dp[i][j])
    return answer
