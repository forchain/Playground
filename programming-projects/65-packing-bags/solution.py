def solution(n, items, bags):
    """判断 items[:n] 能否恰好装进至多 bags 个容量为 10 的袋子。"""
    weights = sorted(items[:n], reverse=True)
    if len(weights) > bags * 10 or sum(weights) > bags * 10:
        return False
    remaining = [10] * bags

    def place(index):
        if index == len(weights):
            return True
        weight = weights[index]
        tried = set()
        for i, capacity in enumerate(remaining):
            # 容量相同的袋子是等价状态，只需尝试其中一个。
            if capacity >= weight and capacity not in tried:
                tried.add(capacity)
                remaining[i] -= weight
                if place(index + 1):
                    return True
                remaining[i] += weight
        return False

    return place(0)
