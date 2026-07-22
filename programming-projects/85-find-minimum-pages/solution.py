def solution(n, m, arr):
    pages = arr[:n]
    if m > n or m <= 0:
        return -1

    def students_needed(limit):
        students, current = 1, 0
        for book in pages:
            if current + book > limit:
                students += 1
                current = book
            else:
                current += book
        return students

    low, high = max(pages), sum(pages)
    while low < high:
        middle = (low + high) // 2
        # 至多 m 组时可继续尝试更小上限；少于 m 组可再切分为空间非问题。
        if students_needed(middle) <= m:
            high = middle
        else:
            low = middle + 1
    return low
