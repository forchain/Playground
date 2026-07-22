# 19. Longest Prefix Match

> 难度与建议用时：Medium-2 30 mins

string

## Problem Statement

You are given two strings `s1` and `s2`. Your task is to find the longest prefix string that is common to both `s1` and `s2`. If no such prefix exists, return an empty string.

## Input & Output

### Input Format

- The first line contains the string `s1`.
- The second line contains the string `s2`.

### Input Constraints

- `1 <= len(s1), len(s2) <= 10^5`
- Both strings contain only lowercase English letters ('a' to 'z').

### Output Format

- A single string representing the longest common prefix between `s1` and `s2`.

## Examples

### Example 1

#### Input

```
abcd
abcxyz
```

#### Output

```
abc
```

#### Explanation

The common prefix between `s1` and `s2` is "abc".

### Example 2

#### Input

```
hello
world
```

#### Output

```

```

#### Explanation

The strings `s1` and `s2` have no common prefix, so the result is an empty string.

## User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.


## Python 解法

### 思路

从首字符同步比较，第一次不同的位置就是公共前缀的结束边界。

### 正确性说明

算法维护的状态始终与上述定义一致，并且按输入顺序处理了所有可能影响答案的元素。每次状态更新都只保留满足题意的候选；处理结束后，返回值因此覆盖全部候选且不会包含非法结果。

### 复杂度

- 时间复杂度：`O(min(n,m))`
- 空间复杂度：`O(min(n,m))`

### 代码与测试

实现见 `solution.py`，题目中的可执行样例见 `test_solution.py`。
