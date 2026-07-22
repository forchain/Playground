# 4. Remove All Vowels

> 难度与建议用时：Medium-1 30 mins

string

## Problem Statement

Write a function that takes a string as input and removes all vowels (both uppercase and lowercase) from it. The output should be the modified string without vowels.

## Input & Output

### Input Format

- A single string containing uppercase and lowercase letters. The string may also include spaces or special characters (which should be kept intact).

### Input Constraints

- 1 ≤ Length of the string ≤ 100

### Output Format

- Return the string with all vowels removed.

## Examples

### Example 1

#### Input

```
hello world
```

#### Output

```
hll wrld
```

#### Explanation

All vowels (e, o) from "hello world" are removed.

### Example 2

#### Input

```
Programming is fun!
```

#### Output

```
Prgrmmng s fn!
```

#### Explanation

All vowels (o, a, i, i, u) from "Programming is fun!" are removed.

## User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.


## Python 解法

### 思路

用元音集合做常数时间成员判断，只过滤元音，其他字符保持原顺序。

### 正确性说明

算法维护的状态始终与上述定义一致，并且按输入顺序处理了所有可能影响答案的元素。每次状态更新都只保留满足题意的候选；处理结束后，返回值因此覆盖全部候选且不会包含非法结果。

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(n)`

### 代码与测试

实现见 `solution.py`，题目中的可执行样例见 `test_solution.py`。
