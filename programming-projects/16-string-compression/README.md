# 16. String Compression

> 难度与建议用时：Medium-2 30 mins

string

two pointer

## Problem Statement

You are given a string consisting of lowercase English letters. Your task is to compress the string into a new format where consecutive repeated characters are replaced with the character followed by the count of its repetitions. If a character appears only once, it should just appear as it is.

## Input & Output

### Input Format

- A string `s` containing only lowercase English letters.

### Input Constraints

- `1 <= len(s) <= 100`

### Output Format

- A string representing the compressed version of the input.

## Examples

### Example 1

#### Input

```
aaaabbbcca
```

#### Output

```
a4b3c2a1
```

#### Explanation

The character `a` appears 4 times consecutively, followed by `b` three times, then `c` twice, and finally `a` once.

### Example 2

#### Input

```
abcccdeeeeffff
```

#### Output

```
ab1c3d1e4f4
```

#### Explanation

All single characters are followed by `1`, while consecutive characters are followed by their counts.

## User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.


## Python 解法

### 思路

游程编码：找到每个连续相同字符段，段长大于 1 才附加数字。测试以明确书面规则为准。

### 正确性说明

算法维护的状态始终与上述定义一致，并且按输入顺序处理了所有可能影响答案的元素。每次状态更新都只保留满足题意的候选；处理结束后，返回值因此覆盖全部候选且不会包含非法结果。

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(n)`

> 注意：原样例对单字符是否添加 `1` 前后矛盾。本工程按 Problem Statement 的明确规则测试。

### 代码与测试

实现见 `solution.py`，题目中的可执行样例见 `test_solution.py`。
