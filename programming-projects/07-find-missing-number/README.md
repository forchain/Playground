# 7. Find Missing Number

> 难度与建议用时：Medium-1 30 mins

array

math

searching

## Problem Statement

You are given an array of size `n` containing integers from `1` to `n+1` inclusive, with exactly one number missing. Your task is to find the missing number.

## Input & Output

### Input Format

- The first line contains an integer `n`, the size of the array.
- The second line contains `n` integers, the elements of the array.

### Input Constraints

- `1 <= n <= 100`
- The array contains distinct integers from `1` to `n+1` with one number missing.

### Output Format

- Return the missing number as an integer.

## Examples

### Example 1

#### Input

```
4
1 2 4 5
```

#### Output

```
3
```

#### Explanation

The array contains numbers from `1` to `5` with `3` missing.

### Example 2

#### Input

```
5
2 3 1 5 6
```

#### Output

```
4
```

#### Explanation

The array contains numbers from `1` to `6` with `4` missing.

## User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.


## Python 解法

### 思路

完整序列 1..n+1 的等差数列和减去实际数组和，就是唯一缺失值。

### 正确性说明

算法维护的状态始终与上述定义一致，并且按输入顺序处理了所有可能影响答案的元素。每次状态更新都只保留满足题意的候选；处理结束后，返回值因此覆盖全部候选且不会包含非法结果。

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`

### 代码与测试

实现见 `solution.py`，题目中的可执行样例见 `test_solution.py`。
