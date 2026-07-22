# 20. Smallest Unique Substring

> 难度与建议用时：Hard-1 30 mins

string

sliding window

two pointer

## Problem Statement

You are given a string `s`. Your task is to find the length of the smallest substring of `s` that contains all the unique characters in `s`.

## Input & Output

### Input Format

A single string `s` containing lowercase alphabets `a-z`.

### Input Constraints

- 1 ≤ |s| ≤ 10^3 (where |s| is the length of the string)
- The string consists of only lowercase English letters.

### Output Format

Return the length of the smallest substring of `s` that contains all unique characters.

## Examples

### Example 1

#### Input

```
abcaacbb
```

#### Output

```
3
```

#### Explanation

The unique characters in the string are `a, b, c`. The smallest substring that contains all these is `abc`, which has a length of `3`.

### Example 2

#### Input

```
aaa
```

#### Output

```
1
```

#### Explanation

The only unique character in the string is `a`. The smallest substring containing `a` is `a` itself, with a length of `1`.

### Example 3

#### Input

```
abcdef
```

#### Output

```
6
```

#### Explanation

All characters in the string are unique and already present in the same substring. Hence the length is `6`.

## User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.


## Python 解法

### 思路

目标字符集合是整串的去重集合。右边界扩张至全部覆盖，再持续收缩左边界以得到最短窗口。

### 正确性说明

算法维护的状态始终与上述定义一致，并且按输入顺序处理了所有可能影响答案的元素。每次状态更新都只保留满足题意的候选；处理结束后，返回值因此覆盖全部候选且不会包含非法结果。

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(k)`

### 代码与测试

实现见 `solution.py`，题目中的可执行样例见 `test_solution.py`。
