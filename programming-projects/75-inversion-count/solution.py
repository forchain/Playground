def solution(n, arr):
    values = list(arr[:n])

    def sort_count(left, right):
        if right - left <= 1:
            return 0
        middle = (left + right) // 2
        count = sort_count(left, middle) + sort_count(middle, right)
        merged, i, j = [], left, middle
        while i < middle and j < right:
            if values[i] <= values[j]:
                merged.append(values[i]); i += 1
            else:
                merged.append(values[j]); j += 1
                # 左半剩余元素均大于 values[j]，一次计入。
                count += middle - i
        merged.extend(values[i:middle]); merged.extend(values[j:right])
        values[left:right] = merged
        return count

    return sort_count(0, len(values))
