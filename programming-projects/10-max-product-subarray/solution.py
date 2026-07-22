def solution(n, arr):
    max_here = min_here = answer = arr[0]
    for value in arr[1:]:
        # A negative value swaps the roles of maximum and minimum products.
        candidates = (value, max_here * value, min_here * value)
        max_here, min_here = max(candidates), min(candidates)
        answer = max(answer, max_here)
    return answer
