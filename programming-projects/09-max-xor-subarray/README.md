# 9. Max XOR Subarray

> 难度与建议用时：Medium-2 30 mins

array

xor

subarray

## Problem Statement

Given an array of integers, find the maximum XOR value of any subarray of the array.

## Input & Output

### Input Format

- The first line contains an integer `n`, the size of the array.
- The second line contains `n` integers, the elements of the array.

### Input Constraints

- 1 ≤ n ≤ 100,000
- -10^9 ≤ array[i] ≤ 10^9

### Output Format

- Return a single integer, the maximum XOR value of any subarray.

## Examples

### Example 1

#### Input

```
4
1 2 3 4
```

#### Output

```
7
```

#### Explanation

The subarray `[3, 4]` has the maximum XOR value of `7`.

### Example 2

#### Input

```
5
8 1 2 12 7
```

#### Output

```
15
```

#### Explanation

The subarray `[8, 1, 2, 12]` has the maximum XOR value of `15`.

## User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.


## Python 解法

### 思路

子数组异或等于两个前缀异或之异或。二进制 Trie 为当前前缀逐位选择相反比特，得到与旧前缀的最大异或。

### 正确性说明

算法维护的状态始终与上述定义一致，并且按输入顺序处理了所有可能影响答案的元素。每次状态更新都只保留满足题意的候选；处理结束后，返回值因此覆盖全部候选且不会包含非法结果。

### 复杂度

- 时间复杂度：`O(nW)，W=32`
- 空间复杂度：`O(nW)`

### 代码与测试

实现见 `solution.py`，题目中的可执行样例见 `test_solution.py`。
