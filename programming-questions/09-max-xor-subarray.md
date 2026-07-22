# 9. Max XOR Subarray

> 难度与建议用时：Medium-2 30 mins

array

xor

subarray

## Problem Statement

Given an array of integers, find the maximum XOR value of any subarray of the array.

## Input & Output

### Input Format

- The first line contains an integer `n`, the size of the array.
- The second line contains `n` integers, the elements of the array.

### Input Constraints

- 1 ≤ n ≤ 100,000
- -10^9 ≤ array[i] ≤ 10^9

### Output Format

- Return a single integer, the maximum XOR value of any subarray.

## Examples

### Example 1

#### Input

```
4
1 2 3 4
```

#### Output

```
7
```

#### Explanation

The subarray `[3, 4]` has the maximum XOR value of `7`.

### Example 2

#### Input

```
5
8 1 2 12 7
```

#### Output

```
15
```

#### Explanation

The subarray `[8, 1, 2, 12]` has the maximum XOR value of `15`.

## User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.
