# 32. Merge Overlapping Intervals

> 难度与建议用时：Hard-2 45 mins

array

sorting

## Problem Statement

You are given a list of intervals where each interval is represented as a pair of integers `[start, end]`. Your task is to merge all overlapping intervals and return the resulting list of merged intervals. Two intervals `[a, b]` and `[c, d]` overlap if `b >= c` and `a <= d`.

## Input & Output

### Input Format

- The first line contains an integer `n`, the number of intervals.
- The next `n` lines each contain two integers `start` and `end` representing an interval.

### Input Constraints

- `1 <= n <= 100`
- `-10^4 <= start <= end <= 10^4`

### Output Format

- Return a 2d array of the merged intervals, where each interval is represented as `[start, end]`

## Examples

### Example 1

#### Input

```
4
1 3
2 6
8 10
15 18
```

#### Output

```
[[1, 6], [8, 10], [15, 18]]
```

#### Explanation

The intervals `[1, 3]` and `[2, 6]` overlap, so they are merged into `[1, 6]`. The other intervals do not overlap.

### Example 2

#### Input

```
3
1 4
4 5
6 8
```

#### Output

```
[[1, 5], [6, 8]]
```

#### Explanation

The intervals `[1, 4]` and `[4, 5]` overlap, so they are merged into `[1, 5]`. The interval `[6, 8]` does not overlap with any other interval.

## User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.
