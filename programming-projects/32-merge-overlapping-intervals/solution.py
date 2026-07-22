def solution(intervals: list[list[int]]) -> list[list[int]]:
    """合并所有相交或端点相接的闭区间。"""
    if not intervals:
        return []
    ordered = sorted(intervals)
    merged = [ordered[0].copy()]
    for start, end in ordered[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
