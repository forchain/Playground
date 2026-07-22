def solution(array: list[int]) -> int:
    """返回将互异整数数组升序排列所需的最少任意交换次数。"""
    target_positions = {value: i for i, value in enumerate(sorted(array))}
    visited = [False] * len(array)
    swaps = 0
    for start in range(len(array)):
        if visited[start] or target_positions[array[start]] == start:
            continue
        cycle_size = 0
        i = start
        # 长度为 m 的置换环恰好需要 m-1 次交换。
        while not visited[i]:
            visited[i] = True
            i = target_positions[array[i]]
            cycle_size += 1
        swaps += cycle_size - 1
    return swaps
