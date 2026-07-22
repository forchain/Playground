# 23. Max Sum Increasing Subsequence

> 难度与建议用时：Hard-1 45 mins

array

dynamic programming

subsequence

## Problem Statement

Given an array of integers, find the maximum sum of an increasing subsequence in the array. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. An increasing subsequence is a sequence of numbers such that every number in the sequence is greater than the previous one. You need to return the maximum sum of such a subsequence.

## Input & Output

### Input Format

- The first line contains an integer `n`, the size of the array.
- The second line contains `n` space-separated integers, the elements of the array.

### Input Constraints

- 1 ≤ n ≤ 100
- -10^4 ≤ array[i] ≤ 10^4

### Output Format

- Return a single integer, the maximum sum of an increasing subsequence.

## Examples

### Example 1

#### Input

```
6
1 101 2 3 100 4
```

#### Output

```
106
```

#### Explanation

The increasing subsequence with the maximum sum is [1, 2, 3, 100].

### Example 2

#### Input

```
5
10 5 4 3 2
```

#### Output

```
10
```

#### Explanation

The increasing subsequence with the maximum sum is [10].

### Example 3

#### Input

```
7
3 4 5 10 1 2 3
```

#### Output

```
22
```

#### Explanation

The increasing subsequence with the maximum sum is [3, 4, 5, 10].

## User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.
