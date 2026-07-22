def solution(matrix: list[list[int]]) -> int:
    """返回二进制矩阵中全 1 正方形的最大面积。"""
    if not matrix or not matrix[0]:
        return 0
    dp = [0] * (len(matrix[0]) + 1)
    best_side = 0
    for row in matrix:
        diagonal = 0
        for col, value in enumerate(row, 1):
            old = dp[col]
            if value == 1:
                # 当前最大边长由左、上、左上三个正方形中的最短边限制。
                dp[col] = min(dp[col], dp[col - 1], diagonal) + 1
                best_side = max(best_side, dp[col])
            else:
                dp[col] = 0
            diagonal = old
    return best_side * best_side
