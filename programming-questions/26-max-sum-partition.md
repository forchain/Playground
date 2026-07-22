# 26. Max Sum Partition

> 难度与建议用时：Hard-1 45 mins

array

dynamic programming

partitioning

## Problem Statement

You are given an array of integers `arr` of size `N`. Your task is to partition the array into contiguous subarrays such that the sum of the maximum element of each subarray is maximized. You can partition the array into as many subarrays as you like, but each subarray must contain at least one element.

Return the maximum sum of the maximum elements of the subarrays.

## Input & Output

### Input Format

- The first line contains an integer `N`, the size of the array.
- The second line contains `N` integers, the elements of the array `arr`.

### Input Constraints

- 1 ≤ N ≤ 100
- -10^4 ≤ arr[i] ≤ 10^4

### Output Format

- Return a single integer, the maximum sum of the maximum elements of the subarrays.

## Examples

### Example 1

#### Input

```
5
1 3 -1 2 5
```

#### Output

```
11
```

#### Explanation

Partition the array as `[1]`, `[3]`, `[-1, 2]`, `[5]`. The maximum elements are `1`, `3`, `2`, and `5`. Their sum is `1 + 3 + 2 + 5 = 11`.

### Example 2

#### Input

```
4
-2 -1 -3 -4
```

#### Output

```
-1
```

#### Explanation

We don't partition the array, and just use the entire array. The maximum of the array is `-1`

### Example 3

#### Input

```
6
4 2 1 6 3 8
```

#### Output

```
24
```

#### Explanation

Partition the array as `[4]`, `[2]`, `[1]`, `[6]`, `[3]`, `[8]`. The maximum elements are `4`, `2`, `1`, `6`, `3` and `8`. Their sum is 4 + 2 + 1 + 6 + 3 + 8 = 24.

## User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.
