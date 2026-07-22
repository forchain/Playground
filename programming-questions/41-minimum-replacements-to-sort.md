# 41. Minimum Replacements to Sort

> 难度与建议用时：Expert-1 60 mins

array

sorting

greedy

## Problem Statement

You are given a 0-indexed integer array `nums`. In one operation, you can replace any element of the array with any two elements that sum to it.

For example, consider `nums = [5,6,7]`. In one operation, you can replace `nums[1]` with `2` and `4` and convert `nums` to `[5,2,4,7]`.

Return the minimum number of operations required to make the array sorted in non-decreasing order.

## Input & Output

### Input Format

- The first line contains an integer `n`, the size of the array.
- The second line contains `n` integers, the elements of the array `nums`.

### Input Constraints

- `1 <= n <= 100`
- `1 <= nums[i] <= 10^9`

### Output Format

- Return a single integer, the minimum number of operations required.

## Examples

### Example 1

#### Input

```
3
5 6 7
```

#### Output

```
0
```

#### Explanation

The array is already sorted in non-decreasing order, so no operations are needed.

### Example 2

#### Input

```
3
3 9 3
```

#### Output

```
2
```

#### Explanation

To sort the array, we need to perform the following operations:

1. Replace `9` with `3` and `6` → `[3, 3, 6, 3]`
2. Replace `6` with `3` and `3` → `[3, 3, 3, 3, 3]`

After these operations, the array becomes sorted.

### Example 3

#### Input

```
5
1 3 2 4 5
```

#### Output

```
1
```

#### Explanation

Replace `3` with `2` and `1` → `[1, 1, 2, 2, 4, 5]`. The array is now sorted.

## User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.
