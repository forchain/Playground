from collections import defaultdict

def solution(s):
    required = len(set(s)); counts = defaultdict(int)
    formed = left = 0; best = len(s) + 1
    for right, ch in enumerate(s):
        counts[ch] += 1
        if counts[ch] == 1:
            formed += 1
        while formed == required:
            best = min(best, right - left + 1)
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                formed -= 1
            left += 1
    return best
