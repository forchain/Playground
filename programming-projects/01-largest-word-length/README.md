# 1. Largest Word Length

> 难度与建议用时：Medium-1 30 mins

string

## Problem Statement

Given a string S, your task is to find the length of the largest word (a sequence of non-space characters separated by spaces) in the string.

## Input & Output

### Input Format

A single string S, which may contain both uppercase and lowercase English alphabets, digits, and spaces.

### Input Constraints

1 <= |S| <= 1000 (where |S| represents the length of the string).

Words are separated by one or more spaces, and the string will not contain leading or trailing spaces.

### Output Format

An integer representing the length of the largest word in the string.

## Examples

### Example 1

#### Input

```
The quick brown fox
```

#### Output

```
5
```

#### Explanation

The largest word in the input is "quick," which has a length of 5.

### Example 2

#### Input

```
A journey of a thousand miles begins with a single step
```

#### Output

```
8
```

#### Explanation

The largest word in the input is "thousand," which has a length of 8.

## User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.


## Python 解法

### 思路

按空白切分所有单词，并在一次扫描中保留最大长度。

### 正确性说明

算法维护的状态始终与上述定义一致，并且按输入顺序处理了所有可能影响答案的元素。每次状态更新都只保留满足题意的候选；处理结束后，返回值因此覆盖全部候选且不会包含非法结果。

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(n)`

### 代码与测试

实现见 `solution.py`，题目中的可执行样例见 `test_solution.py`。
