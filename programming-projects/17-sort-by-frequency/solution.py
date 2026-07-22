from collections import Counter

def solution(n, arr):
    counts = Counter(arr)
    return sorted(arr, key=lambda value: (-counts[value], value))
