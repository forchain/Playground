# 10. Max Product Subarray

> 难度与建议用时：Medium-2 30 mins

array

subarray

greedy

## Problem Statement

Given an array of integers, find the contiguous subarray within the array (containing at least one number) which has the largest product.

## Input & Output

### Input Format

- The first line contains an integer `n`, the size of the array.
- The second line contains `n` integers, the elements of the array.

### Input Constraints

- 1 ≤ n ≤ 100
- -10 ≤ array[i] ≤ 10

### Output Format

- Return a single integer, the maximum product of a contiguous subarray.

## Examples

### Example 1

#### Input

```
5
2 3 -2 4 -1
```

#### Output

```
48
```

#### Explanation

The subarray `[2, 3, -2, 4, -1]` has the maximum product of 48.

### Example 2

#### Input

```
4
-2 0 -1 3
```

#### Output

```
3
```

#### Explanation

The subarray `[3]` has the maximum product of 3.

## User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.
