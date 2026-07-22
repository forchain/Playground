# 66. Subarray Sum Modulo

> 难度与建议用时：Medium-2 30 mins

array

subarray

## Problem Statement

A subarray of array "a" of length "n" is a continuous segment from a[i] through a[j] where `0 <= i <= j < n` . The sum of an array is the sum of its elements. Given an array `a` containing `n` integers, and an integer `m`, determine the maximum value of the sum of any of its subarrays modulo `m`.

## Input & Output

### Input Format

The first line contains an integer `n`, the number of elements in the input array.

The second line contains an integer `m`, the modulo divisor.

The third line contains space-separated integers, i.e., array elements

### Input Constraints

- 2 <= n <= 105
- 1 <= m <= 1014
- 1<= a[i] <= 1018

### Output

The output must be an integer which is the maximum value of sum of any of the arrays' subarrays, modulo `m`.

## Examples

### Example 1

#### Input

```
5
7
3 3 9 9 5
```

#### Output

```
6
```

#### Explanation

For the array a = [3,3,9,9,5] , n = 5 and m = 7, the subarrays_sum % m is as follows

- `[3] % 7 => 3`.
- `[9] % 7 => 2`.
- `[5] % 7 => 5`.
- `[9,5] % 7 => 14 % 7 => 0`.
- `[9,9] % 7 => 18 % 7 => 4`.
- `[3,9] % 7 => 11 % 7 => 4`.
- `[3,3] % 7 => 6 % 7 => 6`.
- `[3,9,9] % 7 => 21 % 7 => 0`.
- `[3,3,9] % 7 => 15 % 7 => 1`.
- `[9,9,5] % 7 => 23 % 7 => 2`.
- `[3,3,9,9] % 7 => 24 % 7 => 3`.
- `[3,9,9,5] % 7 => 26 % 7 => 5`.
- `[3,3,9,9,5] % 7 => 29 % 7 => 1`.

### Example 2

#### Input

```
3
6
1 2 3
```

#### Output

```
5
```

#### Explanation

For the array a = [1,2,3] , n = 3 and m = 6, the subarrays_sum % m is as follows

- `[1] % 6 => 1`.
- `[2] % 6 => 2`.
- `[3] % 6 => 3`.
- `[2,3] % 6 => 5 % 6 => 5`.
- `[1,2] % 6 => 3 % 6 => 3`.
- `[1,2,3] % 6 => 6 % 6 => 0`.

## User Task

Your task is to complete the function `solution()` which takes an integer `n`, an integer `m` and an array `arr`, and returns the expected answer which is an integer. You don't need to read the input or print output, just write code within the function block directly.
