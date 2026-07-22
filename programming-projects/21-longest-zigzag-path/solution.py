def solution(n, arr):
    if n < 2:
        return n
    up = down = 1
    for previous, current in zip(arr, arr[1:]):
        if current > previous:
            up = down + 1
        elif current < previous:
            down = up + 1
    return max(up, down)
