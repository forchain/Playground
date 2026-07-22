# 49. Longest Continuous Increasing Subarray

> 难度与建议用时：Hard-1 45 mins

array

subarray

sliding window

## Problem Statement

Given an unsorted array of integers `arr[]`, find the length of the longest continuous increasing subarray (subarray with strictly increasing elements)

## Input & Output

### Input Format

- The first line is an integer `n`, which represents the number of integers in the array
- The next line contains `n` space-separated integer values of `arr`

### Input Constraints

For the input n, `n >= 2`

### Output Format

An integer representing the length of the longest continuous increasing subarray. For Example 1, the output will be

## Examples

### Example 1

#### Input

```
7
1 3 5 4 7 8 9
```

#### Output

```
4
```

#### Explanation

Consider the subarray `[4, 7, 8, 9]`. This is the longest increasing subarray possible. You will then return 4 as the output.

### Example 2

#### Input

```
5
2 4 6 5 8
```

#### Output

```
3
```

#### Explanation

Consider the subarray `[2, 4, 6]`. This is the longest increasing subarray possible. You will then return 3 as the output.

## User Task

Your task is to complete the function `solution()` which takes in the integers `n` and the array `arr` as parameters and returns an integer. You don't need to read the input as a string. Just write code within the function block directly. You don't need to read the input as a string, just write code within the function block directly.
