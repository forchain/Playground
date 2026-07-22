# 10. Max Product Subarray

> 难度与建议用时：Medium-2 30 mins

array

subarray

greedy

## Problem Statement

Given an array of integers, find the contiguous subarray within the array (containing at least one number) which has the largest product.

## Input & Output

### Input Format

- The first line contains an integer `n`, the size of the array.
- The second line contains `n` integers, the elements of the array.

### Input Constraints

- 1 ≤ n ≤ 100
- -10 ≤ array[i] ≤ 10

### Output Format

- Return a single integer, the maximum product of a contiguous subarray.

## Examples

### Example 1

#### Input

```
5
2 3 -2 4 -1
```

#### Output

```
48
```

#### Explanation

The subarray `[2, 3, -2, 4, -1]` has the maximum product of 48.

### Example 2

#### Input

```
4
-2 0 -1 3
```

#### Output

```
3
```

#### Explanation

The subarray `[3]` has the maximum product of 3.

## User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.


## Python 解法

### 思路

同时维护以当前位置结尾的最大和最小乘积；负数可能把最小负积翻转成最大正积。

### 正确性说明

算法维护的状态始终与上述定义一致，并且按输入顺序处理了所有可能影响答案的元素。每次状态更新都只保留满足题意的候选；处理结束后，返回值因此覆盖全部候选且不会包含非法结果。

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`

### 代码与测试

实现见 `solution.py`，题目中的可执行样例见 `test_solution.py`。
