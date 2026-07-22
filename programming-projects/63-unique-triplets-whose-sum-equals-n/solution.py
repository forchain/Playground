def count_unique_triplets(values: list[int], target: int) -> int:
    ordered = sorted(values)
    found = set()
    for first in range(len(ordered) - 2):
        left, right = first + 1, len(ordered) - 1
        while left < right:
            total = ordered[first] + ordered[left] + ordered[right]
            if total == target:
                found.add((ordered[first], ordered[left], ordered[right]))
                left += 1
                right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1
    return len(found)
