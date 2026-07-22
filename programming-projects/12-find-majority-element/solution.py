def solution(n, arr):
    candidate, balance = None, 0
    for value in arr:
        if balance == 0:
            candidate = value
        balance += 1 if value == candidate else -1
    # Boyer-Moore only yields a candidate, so a second pass must verify it.
    return candidate if arr.count(candidate) > n // 2 else -1
