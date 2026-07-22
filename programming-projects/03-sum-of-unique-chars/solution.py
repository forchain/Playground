from collections import Counter

def solution(s):
    counts = Counter(s)
    # A character contributes only when it occurs exactly once.
    return sum(ord(ch) for ch, count in counts.items() if count == 1)
