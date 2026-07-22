def solution(n, arr, k):
    if not arr:
        return []
    k %= len(arr)  # Avoid doing complete, ineffective rotations.
    return arr[-k:] + arr[:-k] if k else arr[:]
