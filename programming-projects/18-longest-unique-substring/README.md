# 18. Longest Unique Substring

> 难度与建议用时：Medium-2 30 mins

string

two pointer

sliding window

## Problem Statement

Given a string `s`, find the length of the longest substring with all unique characters. The substring should not contain any repeating characters.

## Input & Output

### Input Format

- A single string `s` consisting of lowercase English letters.

### Input Constraints

- 1 ≤ |s| ≤ 10^5

### Output Format

- Return an integer, the length of the longest substring with unique characters.

## Examples

### Example 1

#### Input

```
abcabcbb
```

#### Output

```
3
```

#### Explanation

The longest substring with unique characters is "abc", which has a length of 3.

### Example 2

#### Input

```
bbbbb
```

#### Output

```
1
```

#### Explanation

All characters in the string are the same. The longest substring with unique characters is "b", with a length of 1.

### Example 3

#### Input

```
pwwkew
```

#### Output

```
3
```

#### Explanation

The longest substring with unique characters is "wke", which has a length of 3. Note that "pwke" is not valid because "k" is repeated.

## User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.


## Python 解法

### 思路

滑动窗口始终保持无重复；遇到窗口内旧字符时把左边界跳到其上次位置之后。

### 正确性说明

算法维护的状态始终与上述定义一致，并且按输入顺序处理了所有可能影响答案的元素。每次状态更新都只保留满足题意的候选；处理结束后，返回值因此覆盖全部候选且不会包含非法结果。

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(k)`

### 代码与测试

实现见 `solution.py`，题目中的可执行样例见 `test_solution.py`。
