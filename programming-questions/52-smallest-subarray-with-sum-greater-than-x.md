# 52. Smallest subarray with sum greater than x

> 难度与建议用时：Medium-2 30 mins

array

subarray

## Problem Statement

Given an array of integers `arr` of length `n` and a number `x`, find the smallest subarray with sum greater than `x`.

## Input & Output

### Input Format

- The first line is an integer `n`, which represents the number of integers in the array
- The next line represents the integer `x`
- The next line contains `n` space-separated integer values of `arr`

### Input Constraints

- `n >= 2`
- `x` <= sum of `arr`

### Output Format

An integer representing the size of the smallest subarray.

## Examples

### Example 1

#### Input

```
6
51
1 4 45 6 0 19
```

#### Output

```
3
```

#### Explanation

We have to find a subarray whose sum is more than 51. `[4, 45, 6]` satisfies this condition and is the smallest such subarray possible. So, the output will be the size of this subarray, 3.

### Example 2

#### Input

```
5
50
1 10 3 40 18
```

#### Output

```
2
```

#### Explanation

A subarray whose sum is greater than 50 is `[40, 18]`. This is the smallest subarray. So, the output is 2.

## User Task

Your task is to complete the function `solution()` which takes in two integers `n` and `x`, and the array `arr` as parameters and returns an integer. You don't need to read the input as a string. Just write code within the function block directly. You don't need to read the input as a string, just write code within the function block directly.
