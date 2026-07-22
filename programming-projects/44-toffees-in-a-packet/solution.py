def min_difference(packets: list[int], students: int) -> int:
    # 排序后，最优选择一定对应排序数组中长度为 students 的连续窗口。
    ordered = sorted(packets)
    return min(ordered[i + students - 1] - ordered[i]
               for i in range(len(ordered) - students + 1))
