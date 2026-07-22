# 14. String Rotation Check

> 难度与建议用时：Medium-2 30 mins

string

rotation

## Problem Statement

Given two strings `s1` and `s2`, determine if `s2` is a **left-rotation** of `s1`.
A **left-rotation** here means that you take some number of characters from the **beginning** of the string `s1` and append them to the end of `s1` to form `s2`.

## Input & Output

### Input Format

- The first line contains a string `s1`.
- The second line contains a string `s2`.

### Input Constraints

- 1 ≤ |s1|, |s2| ≤ 100
- Both strings consist of lowercase English letters only.

### Output Format

- Return the length of the rotation if `s2` is a **left-rotation** of `s1`.
- If `s2` is not a rotation of `s1`, return `-1`.

## Examples

### Example 1

#### Input

```
abcde
deabc
```

#### Output

```
3
```

#### Explanation

`s2` is a rotation of `s1` by 3 characters ("abcde" rotated by 3 becomes "deabc").

### Example 2

#### Input

```
hello
lohel
```

#### Output

```
2
```

#### Explanation

`s2` is a rotation of `s1` by 2 characters ("hello" rotated by 2 becomes "lohel").

### Example 3

#### Input

```
abc
cabd
```

#### Output

```
-1
```

#### Explanation

`s2` is not a rotation of `s1`.

## User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.


## Python 解法

### 思路

枚举切割长度 cut，比较 s1[cut:]+s1[:cut]。返回的是左移步数。

### 正确性说明

算法维护的状态始终与上述定义一致，并且按输入顺序处理了所有可能影响答案的元素。每次状态更新都只保留满足题意的候选；处理结束后，返回值因此覆盖全部候选且不会包含非法结果。

### 复杂度

- 时间复杂度：`O(n^2)`
- 空间复杂度：`O(n)`

> 注意：原 Example 2 将 `hello -> lohel` 标成左移 2 位，实际需要左移 3 位；测试采用可复算结果。

### 代码与测试

实现见 `solution.py`，题目中的可执行样例见 `test_solution.py`。
