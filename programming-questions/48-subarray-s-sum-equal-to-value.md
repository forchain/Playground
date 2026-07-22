# 48. Subarray's Sum Equal To Value

> 难度与建议用时：Medium-2 30 mins

array

subarray

two pointer

## Problem Statement

You are given an array of integers `arr[]`. Your task is to find and count all subarrays that have a sum equal to a given target value `x`.

## Input & Output

### Input Format

- The first line is an integer `n`, which represents the number of integers in the array
- The next line represents the integer `x`
- The next line contains `n` space-separated integer values of `arr`

### Input Constraints

For the input n, `n >= 2`

### Output Format

An integer representing the total number of subarrays whose sum is equal to `x`

## Examples

### Example 1

#### Input

```
6
3
1 2 3 -3 1
```

#### Output

```
4
```

#### Explanation

Consider the subarrays `[1, 2]`, `[1, 2, 3, -3]`, `[2, 3, -3, 1]`, `[3]`. All these 4 subarrays sum up to 3.

### Example 2

#### Input

```
3
2
1 1 1
```

#### Output

```
2
```

#### Explanation

The subarrays `[1, 1]`, at indices 0 and 1, `[1, 1]`, at indices 1 and 2

## User Task

Your task is to complete the function `solution()` which takes in the integers `n`, `x` and the array `arr` as parameters and returns an integer. You don't need to read the input as a string. Just write code within the function block directly.
