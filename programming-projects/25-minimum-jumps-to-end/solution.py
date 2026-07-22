def solution(arr: list[int]) -> int:
    """返回到达最后一个下标的最少跳跃次数，不可达时返回 -1。"""
    n = len(arr)
    if n <= 1:
        return 0
    jumps = 0
    current_end = farthest = 0
    for i in range(n - 1):
        farthest = max(farthest, i + arr[i])
        # 扫完当前一跳能覆盖的区间后，必须使用下一跳。
        if i == current_end:
            if farthest == current_end:
                return -1
            jumps += 1
            current_end = farthest
            if current_end >= n - 1:
                return jumps
    return -1
