# 24. Max Sum Non-Adjacent

> 难度与建议用时：Hard-1 45 mins

array

dynamic programming

greedy

## Problem Statement

Given an array of integers, find the maximum sum of non-adjacent elements. You cannot pick two consecutive elements from the array. If the array is empty, or you choose to pick no elements, return 0.

## Input & Output

### Input Format

- The first line contains an integer `n`, the size of the array.
- The second line contains `n` integers, the elements of the array.

### Input Constraints

- 1 ≤ n ≤ 100
- -10^4 ≤ array[i] ≤ 10^4

### Output Format

- Return a single integer, the maximum sum of non-adjacent elements.

## Examples

### Example 1

#### Input

```
5
3 2 7 10 12
```

#### Output

```
22
```

#### Explanation

The maximum sum is obtained by picking 3, 7, and 12 (3 + 7 + 12 = 22).

### Example 2

#### Input

```
4
-1 2 9 -4
```

#### Output

```
9
```

#### Explanation

The maximum sum is obtained by picking 9.

### Example 3

#### Input

```
6
5 5 10 100 10 5
```

#### Output

```
110
```

#### Explanation

The maximum sum is obtained by picking 5, 100, and 5 (5 + 100 + 5 = 110).

## User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.
