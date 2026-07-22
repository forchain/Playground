def count_fair_removals(weights: list[int]) -> int:
    total_even = sum(weights[::2])
    total_odd = sum(weights[1::2])
    left_even = left_odd = answer = 0
    for index, weight in enumerate(weights):
        # 删除后右侧下标奇偶性翻转，因此右侧偶数和要加到新奇数侧，反之亦然。
        right_even = total_even - left_even - (weight if index % 2 == 0 else 0)
        right_odd = total_odd - left_odd - (weight if index % 2 else 0)
        if left_even + right_odd == left_odd + right_even:
            answer += 1
        if index % 2 == 0:
            left_even += weight
        else:
            left_odd += weight
    return answer
