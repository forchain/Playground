# 53. Expensive Words

> 难度与建议用时：Medium-1 30 mins

string

## Problem Statement

Each letter in a sentence is worth its position in the alphabet (i.e. a = 1, b = 2, c = 3, d = 4, e = 5,..., z = 26). Uppercase alphabets have the same values as lowercase ones. However, if a word is **all** in UPPERCASE, the value of that word is doubled. Complete the function `solution()` that calculates the total value of the words in a sentence. Non-alphabet characters are ignored in this calculation.

## Input & Output

### Input Format

The first and only line of input contains a string.

### Input Constraints

- The sentence has at least one word
- Ignore spaces and punctuation
- Remember that the value of a word isn't doubled unless all the letters in it are uppercased.

### Output Format

The output is an integer

## Examples

### Example 1

#### Input

```
abc ABC Abc
```

#### Output

```
24
```

#### Explanation

- Word 1's value = 1 + 2 + 3 = 6
- Word 2's value = (1 + 2 + 3) x 2 = 12
- Word 3's value = 1 + 2 + 3 = 6

Total value = 6 + 12 + 6 = 24

### Example 2

#### Input

```
ab-c A-BC
```

#### Output

```
18
```

#### Explanation

- Word 1's value = 1 + 2 + 3 = 6
- Word 2's value = (1 + 2 + 3) x 2 = 12

Total value = 6 + 12 = 18

## User Task

Your task is to complete the function `solution()` which returns the expected answer. You don't need to read the input, just write code within the function block directly.

---

## Python 解法

### 解题思路

按空白划分单词，过滤标点后计算字母序号和，并对全大写单词翻倍。

### 正确性说明

每个字母按定义贡献其序号，非字母被过滤故贡献为零。对每个词仅在全部有效字母均大写时乘二，最后求和与题目逐词计价完全一致。

### 复杂度分析

时间 O(n)，单个词的临时字母列表最坏 O(n)。

### 样例测试说明

`test_solution.py` 使用 Python 标准库 `unittest` 覆盖原题全部样例。可在本目录运行：

```bash
python3 -m unittest -v
```
