# 27. Minimum Swaps To Sort Array

> 难度与建议用时：Hard-2 40 mins

array

sorting

greedy

## Problem Statement

You are given an array `A` of `N` distinct integers. Your task is to determine the minimum number of swaps (not necessarily adjacent) required to sort the array in ascending order.

## Input & Output

### Input Format

- The first line contains an integer `N`, the size of the array.
- The second line contains `N` space-separated integers, the elements of the array `A`.

### Input Constraints

- 1 ≤ N ≤ 100
- -10^4 ≤ A[i] ≤ 10^4
- All elements in the array are distinct.

### Output Format

- Return a single integer, the minimum number of swaps required to sort the array.

## Examples

### Example 1

#### Input

```
5
3 1 2 5 4
```

#### Output

```
3
```

#### Explanation

To sort the array `[3, 1, 2, 5, 4]` in ascending order:

1. Swap `3` and `1`: `[1, 3, 2, 5, 4]`
2. Swap `3` and `2`: `[1, 2, 3, 5, 4]`
3. Swap `5` and `4`: `[1, 2, 3, 4, 5]` Total swaps = 3.

### Example 2

#### Input

```
4
4 3 2 1
```

#### Output

```
2
```

#### Explanation

To sort the array `[4, 3, 2, 1]` in ascending order:

1. Swap `4` and `1`: `[1, 3, 2, 4]`
2. Swap `3` and `2`: `[1, 2, 3, 4]` Total swaps = 2.

## User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.
