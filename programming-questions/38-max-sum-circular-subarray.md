# 38. Max Sum Circular Subarray

> 难度与建议用时：Hard-2 45 mins

array

subarray

greedy

## Problem Statement

Given a circular array of integers, your task is to find the maximum possible sum of a subarray. A circular array means that the end of the array wraps around to the beginning. For example, in the array `[1, -2, 3, -2]`, the subarray `[3, -2, 1]` is valid.

## Input & Output

### Input Format

- The first line contains an integer `n`, the size of the array.
- The second line contains `n` integers, the elements of the array.

### Input Constraints

- 1 ≤ n ≤ 100
- -10^4 ≤ array[i] ≤ 10^4

### Output Format

- Return a single integer, the maximum sum of a subarray in the circular array.

## Examples

### Example 1

#### Input

```
4
1 -2 3 -2
```

#### Output

```
3
```

#### Explanation

The subarray `[3]` has the maximum sum of 3.

### Example 2

#### Input

```
3
5 -3 5
```

#### Output

```
10
```

#### Explanation

The subarray `[5, 5]` (circular) has the maximum sum of 10.

### Example 3

#### Input

```
3
-3 -2 -1
```

#### Output

```
-1
```

#### Explanation

The subarray `[-1]` has the maximum sum of -1.

## User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.
