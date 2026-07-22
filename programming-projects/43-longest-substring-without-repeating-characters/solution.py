def solution(s: str) -> int:
    """返回不含重复字符的最长连续子串长度。"""
    last_seen = {}
    left = answer = 0
    for right, char in enumerate(s):
        # 只有位于当前窗口内的旧位置才会推动左边界。
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1
        last_seen[char] = right
        answer = max(answer, right - left + 1)
    return answer
