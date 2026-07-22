def solution(s: str) -> int:
    """返回 s 中不同回文子串的数量。"""
    palindromes = set()
    n = len(s)

    # 分别以每个字符和每对相邻字符为中心向两侧扩展。
    for center in range(2 * n - 1):
        left = center // 2
        right = left + center % 2
        while left >= 0 and right < n and s[left] == s[right]:
            palindromes.add(s[left:right + 1])
            left -= 1
            right += 1
    return len(palindromes)
