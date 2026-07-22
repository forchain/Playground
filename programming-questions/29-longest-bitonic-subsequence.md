# 29. Longest Bitonic Subsequence

> 难度与建议用时：Hard-2 45 mins

array

dynamic programming

subsequence

## Problem Statement

Given an array of integers, find the length of the longest bitonic subsequence. A bitonic subsequence is a sequence that first increases and then decreases. The elements of the subsequence need not be contiguous but must maintain their relative order.

## Input & Output

### Input Format

- The first line contains an integer `n`, the size of the array.
- The second line contains `n` space-separated integers, the elements of the array.

### Input Constraints

- 1 ≤ n ≤ 100
- -10^4 ≤ array[i] ≤ 10^4

### Output Format

- Return a single integer, the length of the longest bitonic subsequence.

## Examples

### Example 1

#### Input

```
6
1 2 5 3 2 1
```

#### Output

```
6
```

#### Explanation

The entire array `[1, 2, 5, 3, 2, 1]` is a bitonic subsequence.

### Example 2

#### Input

```
8
1 11 2 10 4 5 2 1
```

#### Output

```
6
```

#### Explanation

The longest bitonic subsequence is `[1, 2, 10, 4, 2, 1]`.

### Example 3

#### Input

```
5
12 11 40 5 3
```

#### Output

```
4
```

#### Explanation

The longest bitonic subsequence is `[12, 40, 5, 3]`.

## User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.
