def solution(n, arr, k):
    # Sorting descending makes the 1-based kth element direct to index.
    return sorted(arr, reverse=True)[k - 1]
