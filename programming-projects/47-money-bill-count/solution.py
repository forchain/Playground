def minimum_bill_count(amount: int, coins: list[int]) -> int:
    # dp[value] 表示凑出 value 所需的最少硬币数；动态规划适用于非标准币制。
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value:
                dp[value] = min(dp[value], dp[value - coin] + 1)
    return dp[amount]
