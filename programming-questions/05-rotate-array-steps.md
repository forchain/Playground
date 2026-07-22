# 5. Rotate Array Steps

> 难度与建议用时：Medium-1 30 mins

array

rotation

## Problem Statement

You are given an array `arr` of integers containing `n` elements and an integer `k`. Rotate the array to the right by `k` steps, where `k` can be any positive integer (less than or equal to 1000). Rotation means each element of the array is shifted right by one position, and the last element moves to the beginning. For example, rotating `[1, 2, 3]` by 1 step results in `[3, 1, 2]`.

## Input & Output

### Input Format

- First line contains an integer `n`, the size of the array `arr`.
- Second line contains `n` space-separated integers, representing the elements of the array `arr`.
- Third line contains an integer `k`.

### Input Constraints

- 1 <= n <= 100
- -10^4 <= arr[i] <= 10^4
- 1 <= k <= 10^4

### Output Format

- Output the rotated array as a **space-separated string**.

## Examples

### Example 1

#### Input

```
5
1 2 3 4 5
2
```

#### Output

```
4 5 1 2 3
```

#### Explanation

Rotating `[1, 2, 3, 4, 5]` two steps to the right results in `[4, 5, 1, 2, 3]`.

### Example 2

#### Input

```
6
10 20 30 40 50 60
4
```

#### Output

```
40 50 60 10 20 30
```

#### Explanation

Rotating `[10, 20, 30, 40, 50, 60]` four steps to the right results in `[40, 50, 60, 10, 20, 30]`.

## User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.
