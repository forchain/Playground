def solution(n, arr):
    left, right, result = 0, n - 1, []
    while left <= right:
        result.append(arr[right]); right -= 1
        if left <= right:
            result.append(arr[left]); left += 1
    return ' '.join(map(str, result))
