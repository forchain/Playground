# 2. Sum of Digits

> 难度与建议用时：Medium-1 30 mins

math

string

## Problem Statement

Write a function to calculate the sum of digits of an integer number `n`. For example, if the input is 123, the sum of digits is 1 + 2 + 3 = 6. The function must return the calculated sum.

### Input & Output

#### Input Format

1. A single integer `n`.

#### Input Constraints

- `|n| <= 10^9`

#### Output Format

- A single integer representing the sum of the digits of the input number.

## Examples

### Example 1

#### Input

```
123
```

#### Output

```
6
```

#### Explanation

The sum of the digits of 123 is 1 + 2 + 3 = 6.

### Example 2

#### Input

```
-2059
```

#### Output

```
16
```

#### Explanation

The sum of the digits of -2059 is 2 + 0 + 5 + 9 = 16 (ignoring the negative sign).

### Example 3

#### Input

```
0
```

#### Output

```
0
```

#### Explanation

The digit sum of 0 is just 0.

## User Task

Your task is to complete the function solution() and return the expected answer. You don’t need to read the input; just write code within the function block directly.


## Python 解法

### 思路

负号不属于数字，先取绝对值，再逐位累加十进制字符。

### 正确性说明

算法维护的状态始终与上述定义一致，并且按输入顺序处理了所有可能影响答案的元素。每次状态更新都只保留满足题意的候选；处理结束后，返回值因此覆盖全部候选且不会包含非法结果。

### 复杂度

- 时间复杂度：`O(d)`
- 空间复杂度：`O(d)`

### 代码与测试

实现见 `solution.py`，题目中的可执行样例见 `test_solution.py`。
