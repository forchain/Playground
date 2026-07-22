# 11. Count Distinct Substrings

> 难度与建议用时：Medium-2 30 mins

string

substring

## Problem Statement

Given a string `s`, your task is to count the number of distinct substrings of `s`. A substring is defined as a contiguous sequence of characters within a string. The empty substring is not considered.

## Input & Output

### Input Format

- A single string `s`.

### Input Constraints

- 1 ≤ |s| ≤ 100
- `s` consists of lowercase English letters only.

### Output Format

- An integer representing the number of distinct substrings of `s`.

## Examples

### Example 1

#### Input

```
abc
```

#### Output

```
6
```

#### Explanation

The distinct substrings of "abc" are: "a", "b", "c", "ab", "bc", "abc". Total = 6.

### Example 2

#### Input

```
aaa
```

#### Output

```
3
```

#### Explanation

The distinct substrings of "aaa" are: "a", "aa", "aaa". Total = 3.

## User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.


## Python 解法

### 思路

枚举所有非空区间，把对应子串放入集合去重，最后返回集合大小。

### 正确性说明

算法维护的状态始终与上述定义一致，并且按输入顺序处理了所有可能影响答案的元素。每次状态更新都只保留满足题意的候选；处理结束后，返回值因此覆盖全部候选且不会包含非法结果。

### 复杂度

- 时间复杂度：`O(n^3)，包含切片成本`
- 空间复杂度：`O(n^3)`

### 代码与测试

实现见 `solution.py`，题目中的可执行样例见 `test_solution.py`。
