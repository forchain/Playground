# 47. Money Bill Count

> 难度与建议用时：Medium-2 30 mins

array

math

## Problem Statement

You are given an integer `amount` and an array of distinct integers `arr` which represent different denomination of `coins`. You have to find the minimum number of different `coins` required to match the `amount`.

## Input & Output

### Input Format

- The first line is the amount
- The second line is the number of elements in the input array. That is, the different types of `coins`
- The third line contains the input array elements separated by spaces

### Input Constraints

- There must be atleast 1 combination of `coins` which will match the `amount`

### Output Format

The output is an integer which satisfies the required condition.

## Examples

### Example 1

#### Input

```
101
3
1 10 20
```

#### Output

```
6
```

#### Explanation

To get to `101`, we can have `5` coins that have a denomination of `20` and `1` coin that has a denomination of `1`. . That is, `(20 * 5) + (1 * 1) = 101`. So, with `6` coins, we can get to the amount of `101`.

We can also get to `101` with `10` coins of denomination `10` and `1` coin of denomination `1`. `(10 * 10) + (1 * 1) = 101`. But, this will need `11` coins in total.

So, the answer is `6` because we are looking for the **minimum** number of coins.

### Example 2

#### Input

```
1050
4
1 10 20 100
```

#### Output

```
13
```

#### Explanation

```
1050 = (10 * 100) + (2 * 20) + (1 * 10)
Number of coins = 10 + 2 + 1 = 13
```

### Example 3

#### Input

```
55
4
1 5 10 50
```

#### Output

```
2
```

#### Explanation

```
55 = (1 * 50) + (1 * 5)
Number of coins = 1 + 1 = 2
```

## User Task

Your task is to complete the function `minimumCoins()` and return the expected answer. You don't need to read the input, just write code within the function block directly.

---

## Python 解法

### 解题思路

以金额为状态做完全背包动态规划，而不是假设面额满足贪心性质。

### 正确性说明

凑出 value 的任一方案都有最后一枚 coin，去掉它后是 value-coin 的方案；取所有可用最后硬币对应最优子问题的最小值，依据归纳法得到 dp[value] 最优。

### 复杂度分析

设金额 A、面额数 m，时间 O(A m)，空间 O(A)。

### 样例测试说明

`test_solution.py` 使用 Python 标准库 `unittest` 覆盖原题全部样例。可在本目录运行：

```bash
python3 -m unittest -v
```
