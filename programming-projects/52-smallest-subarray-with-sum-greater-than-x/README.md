# 52. Smallest subarray with sum greater than x

> 难度与建议用时：Medium-2 30 mins

array

subarray

## Problem Statement

Given an array of integers `arr` of length `n` and a number `x`, find the smallest subarray with sum greater than `x`.

## Input & Output

### Input Format

- The first line is an integer `n`, which represents the number of integers in the array
- The next line represents the integer `x`
- The next line contains `n` space-separated integer values of `arr`

### Input Constraints

- `n >= 2`
- `x` <= sum of `arr`

### Output Format

An integer representing the size of the smallest subarray.

## Examples

### Example 1

#### Input

```
6
51
1 4 45 6 0 19
```

#### Output

```
3
```

#### Explanation

We have to find a subarray whose sum is more than 51. `[4, 45, 6]` satisfies this condition and is the smallest such subarray possible. So, the output will be the size of this subarray, 3.

### Example 2

#### Input

```
5
50
1 10 3 40 18
```

#### Output

```
2
```

#### Explanation

A subarray whose sum is greater than 50 is `[40, 18]`. This is the smallest subarray. So, the output is 2.

## User Task

Your task is to complete the function `solution()` which takes in two integers `n` and `x`, and the array `arr` as parameters and returns an integer. You don't need to read the input as a string. Just write code within the function block directly. You don't need to read the input as a string, just write code within the function block directly.

---

## Python 解法

### 解题思路

先计算前缀和。用单调递增队列保存仍可能成为左端点的前缀下标：当前前缀与队首之差大于 `x` 时得到合法区间并弹出队首，以继续寻找更短区间；插入当前前缀前，删除队尾所有不小于它的前缀，因为当前下标更晚且前缀和更小，是严格更优的左端候选。该方法不要求数组元素非负。

### 正确性说明

对任意右端点，队列按下标递增且对应前缀和严格递增。若当前前缀减队首已经大于 `x`，该队首构成合法区间，弹出后只会让左端更靠右，从而可能得到更短答案。若一个旧前缀不小于当前前缀，那么当前前缀下标更晚、数值更小：对任何未来右端，它形成的区间既不会更长，区间和也不会更小，因此旧前缀可安全删除。所有被保留或删除的候选都按上述支配关系处理，所以最短合法区间不会遗漏。

### 复杂度分析

每个前缀下标至多入队、出队一次，时间 O(n)；前缀数组和队列空间 O(n)。

### 样例测试说明

`test_solution.py` 使用 Python 标准库 `unittest` 覆盖原题全部样例。可在本目录运行：

```bash
python3 -m unittest -v
```
