from bisect import bisect_left, bisect_right


def solution(n, m, arr):
    prefix_values = []
    prefix = 0
    for value in arr[:n]:
        prefix = (prefix + value) % m
        prefix_values.append(prefix)

    coordinates = sorted(set([0] + prefix_values))
    tree = [0] * (len(coordinates) + 1)

    def add(index):
        index += 1
        while index < len(tree):
            tree[index] += 1
            index += index & -index

    def count_through(index):
        count = 0
        index += 1
        while index:
            count += tree[index]
            index -= index & -index
        return count

    def index_of_kth(k):
        """返回第 k 个已插入前缀的压缩坐标，k 从 1 开始。"""
        index = 0
        step = 1 << (len(tree).bit_length() - 1)
        while step:
            candidate = index + step
            if candidate < len(tree) and tree[candidate] < k:
                index = candidate
                k -= tree[candidate]
            step >>= 1
        return index

    add(bisect_left(coordinates, 0))
    inserted = 1
    answer = 0
    for prefix in prefix_values:
        answer = max(answer, prefix)
        right = bisect_right(coordinates, prefix) - 1
        not_greater = count_through(right)
        if not_greater < inserted:
            # 下一个已插入值就是严格大于当前值的最小前缀。
            successor = coordinates[index_of_kth(not_greater + 1)]
            answer = max(answer, (prefix - successor) % m)
        add(bisect_left(coordinates, prefix))
        inserted += 1
    return answer
