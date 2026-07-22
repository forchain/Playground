# 48. Subarray's Sum Equal To Value

> 难度与建议用时：Medium-2 30 mins

array

subarray

two pointer

## Problem Statement

You are given an array of integers `arr[]`. Your task is to find and count all subarrays that have a sum equal to a given target value `x`.

## Input & Output

### Input Format

- The first line is an integer `n`, which represents the number of integers in the array
- The next line represents the integer `x`
- The next line contains `n` space-separated integer values of `arr`

### Input Constraints

For the input n, `n >= 2`

### Output Format

An integer representing the total number of subarrays whose sum is equal to `x`

## Examples

### Example 1

#### Input

```
6
3
1 2 3 -3 1
```

#### Output

```
4
```

#### Explanation

Consider the subarrays `[1, 2]`, `[1, 2, 3, -3]`, `[2, 3, -3, 1]`, `[3]`. All these 4 subarrays sum up to 3.

### Example 2

#### Input

```
3
2
1 1 1
```

#### Output

```
2
```

#### Explanation

The subarrays `[1, 1]`, at indices 0 and 1, `[1, 1]`, at indices 1 and 2

## User Task

Your task is to complete the function `solution()` which takes in the integers `n`, `x` and the array `arr` as parameters and returns an integer. You don't need to read the input as a string. Just write code within the function block directly.

---

## Python 解法

### 解题思路

维护前缀和出现次数；当前前缀减去目标值若曾出现，每次出现都对应一个合法起点。

### 正确性说明

子数组 i..j 的和等于 prefix[j]-prefix[i-1]。因此它等于目标当且仅当旧前缀为当前前缀减目标；哈希表准确计数所有旧前缀，且每个子数组只在其右端点被计一次。

### 复杂度分析

时间 O(n)，空间 O(n)。

### 样例测试说明

`test_solution.py` 使用 Python 标准库 `unittest` 覆盖原题全部样例。可在本目录运行：

```bash
python3 -m unittest -v
```

> 原题样例 1 声明 n=6，但只列出 5 个数组元素；测试按实际列出的数组执行，其结果仍为 4。
