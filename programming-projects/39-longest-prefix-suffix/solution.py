def solution(s: str) -> int:
    """返回不重叠的最长相等前缀与后缀长度。"""
    prefix = [0] * len(s)
    matched = 0
    for i in range(1, len(s)):
        while matched and s[i] != s[matched]:
            matched = prefix[matched - 1]
        if s[i] == s[matched]:
            matched += 1
        prefix[i] = matched
    length = prefix[-1] if s else 0
    # 沿 KMP 失配链寻找第一个不超过字符串一半的边界。
    while length * 2 > len(s):
        length = prefix[length - 1]
    return length
