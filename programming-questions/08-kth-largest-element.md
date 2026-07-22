# 8. Kth Largest Element

> 难度与建议用时：Medium-1 30 mins

array

sorting

searching

## Problem Statement

You are given an array of integers and an integer `k`. Your task is to find the `k`th largest element (1-indexed) in the array.

## Input & Output

### Input Format

- The first line of input contains an integer `n`, the size of the array (1 ≤ n ≤ 100).
- The second line contains `n` integers separated by spaces, representing the array elements. Each array element `a[i]` satisfies `−10^4 ≤ a[i] ≤ 10^4`.
- The third line contains a single integer `k` (1 ≤ k ≤ n), which specifies the position of the largest element to find.

### Input Constraints

- 1 ≤ n ≤ 100
- −10^4 ≤ a[i] ≤ 10^4
- 1 ≤ k ≤ n

### Output Format

- A single integer representing the `k`th largest element in the array.

## Examples

### Example 1

#### Input

```
6
3 2 1 5 6 4
2
```

#### Output

```
5
```

#### Explanation

The sorted array in descending order is [6, 5, 4, 3, 2, 1]. The 2nd largest element is `5`.

### Example 2

#### Input

```
4
7 9 3 2
4
```

#### Output

```
2
```

#### Explanation

The sorted array in descending order is [9, 7, 3, 2]. The 4th largest element is `2`.

## User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.
