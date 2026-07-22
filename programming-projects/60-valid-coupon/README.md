# 60. Valid coupon

> 难度与建议用时：Medium-1 30 mins

string

## Problem Statement

A fake coupon website is operating on the internet, and a major e-commerce company must try to identify the fake coupons. Every coupon has a serial number that can be used to determine whether it is valid. The serial number also can be used to determine the discount amount of the coupon. A valid serial number will have the following characteristics:

1. There are 10 to 12 characters.
2. The first 3 characters are distinct uppercase English letters.
3. The next 4 characters represent the year the coupon was printed and will always be between 1900 and 2019 inclusive.
4. The next characters represent the coupon discount amount and may be any one of {10, 20, 50, 100, 200, 500, 1000}.
5. The next character should be the last character of the serial number. The serial number must end with exactly one uppercase English letter only

Given a coupon code, return the **first character** of the coupon code if it is valid i.e., it satisfies all the 5 conditions mentioned above. Otherwise, return the **last character**.

## Input & Output

### Input Format

The first and only line is a string

### Input Constraints

The coupon code has at least 1 character

### Output Format

Return a character in C/C++/Java and string of length 1 in JavaScript/Python

## Examples

### Example 1

#### Input

```
AVG190420T
```

#### Output

```
A
```

#### Explanation

- There are 10 characters, so it passes condition 1.
- The first three characters `AVG` are distinct & uppercase, so it passes condition 2
- The next four characters `1904` is between 1900 and 2019, so it passes condition 3
- For the next two characters `20` is among the list of values, so it passes condition 4
- The next character which is the last character is a `T`, so it passes condition 5

### Example 2

#### Input

```
1234XYZ
```

#### Output

```
Z
```

#### Explanation

The string doesn't have 10 to 12 characters. Therefore, it is invalid and we are returning the last character `Z`.

## User Task

Your task is to complete the function `solution()` which takes a string `string` and returns the expected answer. You don't need to read the input as a string, just write code within the function block directly.

---

## Python 解法

### 解题思路

按长度、前三位、年份、折扣字段和末位五组规则逐项验证。

### 正确性说明

切片边界与字段定义一致；valid 只有在五个条件全部成立时为真，因此真时返回首字符恰表示有效，否则返回末字符恰表示无效。短路求值也避免对非数字年份调用 int。

### 复杂度分析

串长最多 12，按约束为 O(1) 时间和空间。

### 样例测试说明

`test_solution.py` 使用 Python 标准库 `unittest` 覆盖原题全部样例。可在本目录运行：

```bash
python3 -m unittest -v
```
