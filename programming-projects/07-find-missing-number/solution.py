def solution(n, arr):
    # Values should be exactly 1..n+1 except for one missing value.
    expected = (n + 1) * (n + 2) // 2
    return expected - sum(arr)
