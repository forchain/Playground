# 54. Number String

> 难度与建议用时：Medium-1 30 mins

math

## Problem Statement

You are given an integer `n` which needs to be expanded into a string based on the digits of the number and their place values. The expanded string must be returned.

## Inputs & Outputs

### Input Format

The first and only line contains an integer `n`

### Output Format

A string representing the expanded form of the integer

## Examples

### Example 1

#### Input

```
n = 35
```

#### Output

```
30 + 5
```

### Explanation

5 is in the 1's place, and 3 is in the 10's place.

So, it can be expanded in the following way:

```
(3 x 10) + (5 x 1)
```

This results in the output `30 + 5`

### Example 2

#### Input

```
73
```

#### Output

```
70 + 3
```

#### Explanation

3 is in the 1's place, and 7 is in the 10's place.

So, it can be expanded in the following way:

```
(7 x 10) + (3 x 1)
```

This results in an output of `70 + 3`

## User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.

---

## Python 解法

### 解题思路

逐位把非零数字补上其位数对应的 0，并用加号连接；零位无需出现在展开式。

### 正确性说明

第 i 位数字乘以 10 的相应幂，十进制文本表示正是该数字后补对应数量的 0。所有非零位相加依据十进制位权展开必等于原数。

### 复杂度分析

设数字位数为 d，时间和输出空间均为 O(d²)（计入生成的展开文本）。

### 样例测试说明

`test_solution.py` 使用 Python 标准库 `unittest` 覆盖原题全部样例。可在本目录运行：

```bash
python3 -m unittest -v
```
