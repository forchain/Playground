def compare_and_merge(first: str, second: str) -> str:
    i = j = 0
    result = []
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:  # 相等时按规则选择 first
            result.append(first[i]); i += 1
        else:
            result.append(second[j]); j += 1
    result.append(first[i:])
    result.append(second[j:])
    return ''.join(result)
