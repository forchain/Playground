# 21. Longest Zigzag Path

> 难度与建议用时：Hard-1 45 mins

array

dynamic programming

subsequence

## Problem Statement

Given an array of integers, find the length of the longest zigzag subsequence. A zigzag subsequence is defined as a sequence where the differences between consecutive elements strictly alternate between positive and negative.

## Input & Output

### Input Format

- The first line contains an integer `n`, the size of the array.
- The second line contains `n` space-separated integers, the elements of the array.

### Input Constraints

- 1 ≤ n ≤ 100
- -10^4 ≤ array[i] ≤ 10^4

### Output Format

- Return a single integer, the length of the longest zigzag subsequence.

## Examples

### Example 1

#### Input

```
6
1 7 4 9 2 5
```

#### Output

```
6
```

#### Explanation

The entire array is a zigzag sequence: [1, 7, 4, 9, 2, 5], as 1 < 7, 7 > 4, 4 < 9, 9 > 2, 2 < 5.

### Example 2

#### Input

```
7
1 17 5 10 13 15 10
```

#### Output

```
5
```

#### Explanation

The longest zigzag subsequence is [1, 17, 10, 13, 10].

### Example 3

#### Input

```
5
10 10 10 10 10
```

#### Output

```
1
```

#### Explanation

All elements are the same, so the longest zigzag subsequence is any single element.

## User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.
