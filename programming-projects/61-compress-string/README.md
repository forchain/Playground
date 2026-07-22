# 61. Compress String

> 难度与建议用时：Medium-1 30 mins

string

## Problem Statement

You are given a string of characters `chars`. This string needs to be compressed based on the following rules:

1. If the number of times a character repeats in a string is 1, then the resultant string must contain the character itself.
2. If the number of times a character `x` is repeated is `n`, then the resultant string should contain `xn`

The order of characters in the resultant string must match the order in which they appear in the input string.

## Input & Output

### Input Format

The first and only line of input is a string

### Input Constraints

- The string only has lowercase alphabets.
- The string contains at least 1 character.

### Output Format

- A string is returned as the output

## Examples

### Example 1

#### Input

```
ahaee
```

#### Output

```
a2he2
```

#### Explanation

`a` occurs twice, `h` occurs once and `e` occurs twice.

### Example 2

#### Input

```
a
```

#### Output

```
a
```

#### Explanation

`a` occurs only once.

## User Task

Your task is to complete the function `solution()` which returns the expected answer. You don't need to read the input, just write code within the function block directly.

---

## Python 解法

### 解题思路

先统计全串频次；利用字典的插入顺序按字符首次出现顺序生成字符及可选计数。

### 正确性说明

计数表准确记录每个字符总出现次数，且键顺序等于首次出现顺序。生成阶段对次数 1 和大于 1 分别执行题目两条规则，所以结果完整且顺序正确。

### 复杂度分析

时间 O(n)，空间 O(k)，k 为不同字符数。

### 样例测试说明

`test_solution.py` 使用 Python 标准库 `unittest` 覆盖原题全部样例。可在本目录运行：

```bash
python3 -m unittest -v
```
