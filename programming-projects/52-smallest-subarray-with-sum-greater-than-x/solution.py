def smallest_subarray_over(values: list[int], target: int) -> int:
    from collections import deque

    # prefix[i] 是前 i 个元素之和，子数组 [i, j) 的和就是 prefix[j] - prefix[i]。
    prefix = [0]
    for value in values:
        prefix.append(prefix[-1] + value)

    best = len(values) + 1
    candidates = deque()
    for right, current in enumerate(prefix):
        # 队首是最早且前缀和较小的候选；满足条件后继续弹出可得到更短区间。
        while candidates and current - prefix[candidates[0]] > target:
            best = min(best, right - candidates.popleft())

        # 更晚且不大的前缀和永远优于队尾：它能形成更大和、更短的后续区间。
        while candidates and prefix[candidates[-1]] >= current:
            candidates.pop()
        candidates.append(right)
    return best if best <= len(values) else 0
