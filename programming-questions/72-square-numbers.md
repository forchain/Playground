# 72. Square Numbers

> 难度与建议用时：Medium-1 30 mins

math

## Problem Statement

Write a program to find a number whose square has the same digits in the end as the number itself

## Input & Output

### Input Format

The first and only line contains an integer

### Input Constraints

For the number `n`, `-10000 <= n <= 10000`

### Output Format

Return `1` or `0` based on whether the given condition is satisfied or not.

## Examples

### Example 1

#### Input

```
25
```

#### Output

```
1
```

#### Explanation

The square of 25 is 625, which ends with 25, which is the number itself. So, `1` is returned

### Example 2

#### Input

```
8
```

#### Output

```
0
```

#### Explanation

The square of 8 is 64. As the square does not end with 8, `0` is returned

### User Task

Your task is to complete `solution()` which accepts an integer and returns the expected answer which is also an integer. You don't need to read the input as an integer, just write code within the function block directly.
