def solution(string, m, n):
    length = len(string)
    offset = 0
    for turns in range(1, 2 * length + 1):
        offset = (offset + (m if turns % 2 else n)) % length
        rotated = string[-offset:] + string[:-offset] if offset else string
        if rotated == string:
            return turns
    raise ValueError("有限旋转必然会回到原字符串")
