def solution(s):
    result, start = [], 0
    for i in range(1, len(s) + 1):
        if i == len(s) or s[i] != s[start]:
            count = i - start
            # Follow the written rule: omit the count for a single character.
            result.append(s[start] + (str(count) if count > 1 else ''))
            start = i
    return ''.join(result)
