def count_subarrays(values: list[int], target: int) -> int:
    seen = {0: 1}
    prefix = answer = 0
    for value in values:
        prefix += value
        # 若此前前缀为 prefix-target，两前缀之差对应一个目标和子数组。
        answer += seen.get(prefix - target, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    return answer
