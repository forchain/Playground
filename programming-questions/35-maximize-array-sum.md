# 35. Maximize Array Sum

> 难度与建议用时：Hard-2 45 mins

array

greedy

sorting

## Problem Statement

You are given an array `A` of size `N` and an integer `K`. You can perform at most `K` operations on the array. In each operation, you can select any element of the array and negate its value (i.e., change `A[i]` to `-A[i]`). Your task is to maximize the sum of the array after performing at most `K` operations.

## Input & Output

### Input Format

- The first line contains an integer `N`, the size of the array.
- The second line contains `N` integers, the elements of the array `A`.
- The third line contains an integer `K`, the maximum number of operations allowed.

### Input Constraints

- `1 <= N <= 100`
- `-10^4 <= A[i] <= 10^4`
- `1 <= K <= 10^4`

### Output Format

- Return a single integer, the maximum sum of the array after performing at most `K` operations.

## Examples

### Example 1

#### Input

```
5
-2 0 5 -1 -3
4
```

#### Output

```
11
```

#### Explanation

Negate `-2`, `-1`, and `-3` to get `[2, 0, 5, 1, 3]`. The sum is `2 + 0 + 5 + 1 + 3 = 11`.

### Example 2

#### Input

```
3
-5 -2 -3
2
```

#### Output

```
6
```

#### Explanation

Negate `-5` and `-3` to get `[5, -2, 3]`. The sum is `5 + (-2) + 3 = 6`.

## User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.
