# 25. Minimum Jumps to End

> 难度与建议用时：Hard-1 45 mins

array

greedy

dynamic programming

## Problem Statement

You are given an array `arr` of size `n` where each element represents the maximum number of steps you can jump forward from that position. Your task is to determine the minimum number of jumps required to reach the end of the array starting from the first element. If it is not possible to reach the end, return `-1`.

## Input & Output

### Input Format

- The first line contains an integer `n`, the size of the array.
- The second line contains `n` integers, the elements of the array `arr`.

### Input Constraints

- `1 <= n <= 100`
- `0 <= arr[i] <= 100`

### Output Format

- Return a single integer, the minimum number of jumps required to reach the end of the array, or `-1` if it is not possible.

## Examples

### Example 1

#### Input

```
5
2 3 1 1 4
```

#### Output

```
2
```

#### Explanation

From index 0, jump 1 step to index 1, then jump 3 steps to the end (index 5). Total jumps = 2.

### Example 2

#### Input

```
5
1 0 0 0 0
```

#### Output

```
-1
```

#### Explanation

It is not possible to move beyond index 0 as all subsequent elements are 0.

### Example 3

#### Input

```
1
0
```

#### Output

```
0
```

#### Explanation

You are already at the end of the array, so no jumps are required.

## User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.
