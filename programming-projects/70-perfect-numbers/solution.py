def solution(n):
    divisor_sums = [0] * (n + 1)
    # d 是其所有大于 d 的倍数的真因子。
    for d in range(1, n // 2 + 1):
        for multiple in range(d * 2, n + 1, d):
            divisor_sums[multiple] += d
    return " ".join(str(x) for x in range(2, n + 1) if divisor_sums[x] == x)
