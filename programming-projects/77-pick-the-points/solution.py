def solution(numOfsets, arr):
    segments = sorted(arr[:numOfsets], key=lambda segment: segment[1])
    selected = None
    count = 0
    for start, end in segments:
        if selected is None or selected < start:
            # 选最早结束区间的右端点，给后续区间留下最大覆盖空间。
            selected = end
            count += 1
    return count
