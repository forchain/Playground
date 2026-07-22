# 13. Rearrange Alternately

> 难度与建议用时：Medium-2 30 mins

array

sorting

two pointer

## Problem Statement

Given a sorted array of integers, rearrange the elements in such a way that the first element is the largest, the second is the smallest, the third is the second largest, the fourth is the second smallest, and so on. Your task is to return the rearranged integers as a space-separated string.

## Input & Output

### Input Format

- The first line contains an integer `n`, the size of the array.
- The second line contains `n` integers, the elements of the array, separated by spaces.

### Input Constraints

- 1 ≤ n ≤ 100
- -10^5 ≤ array[i] ≤ 10^5
- The array is sorted in non-decreasing order.

### Output Format

- Return the rearranged array as a space-separated string.

## Examples

### Example 1

#### Input

```
6
1 2 3 4 5 6
```

#### Output

```
6 1 5 2 4 3
```

#### Explanation

The largest element is 6, the smallest is 1, the second largest is 5, the second smallest is 2, and so on.

### Example 2

#### Input

```
5
10 20 30 40 50
```

#### Output

```
50 10 40 20 30
```

#### Explanation

The largest element is 50, the smallest is 10, the second largest is 40, the second smallest is 20, and so on.

## User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.


## Python 解法

### 思路

数组已排序，用左右双指针交替取当前最大值和最小值。

### 正确性说明

算法维护的状态始终与上述定义一致，并且按输入顺序处理了所有可能影响答案的元素。每次状态更新都只保留满足题意的候选；处理结束后，返回值因此覆盖全部候选且不会包含非法结果。

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(n)`

### 代码与测试

实现见 `solution.py`，题目中的可执行样例见 `test_solution.py`。
