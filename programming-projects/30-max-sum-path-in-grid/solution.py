def solution(grid: list[list[int]]) -> int:
    """返回从左上到右下、每步向右或向下的路径最大和。"""
    if not grid or not grid[0]:
        return 0
    dp = [float("-inf")] * len(grid[0])
    dp[0] = 0
    for row in grid:
        for col, value in enumerate(row):
            # dp[col] 尚为来自上方的值，dp[col-1] 已更新为来自左方的值。
            from_left = dp[col - 1] if col else float("-inf")
            dp[col] = max(dp[col], from_left) + value
    return int(dp[-1])
