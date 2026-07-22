# 77. Pick the Points

> 难度与建议用时：Hard-1 30 mins

math

array

2d array

## Problem Statement

On the integer line, a **segment** is defined by a starting integer and an ending integer. It contains all integers between them, including themselves. For example, a segment `{3, 5}` means integers `3, 4, 5`.

You are given an array of `n` segments `[{a[0],b[0]}, {a[1],b[1]},…,{a[n−1],b[n−1]}]`. You must find the minimum number of points such that each segment contains at least one point. That is, find the size of a minimum set of integers `X` such that for any segment `{a[i], b[i]}` there is a point `x ∈ X` such that `a[i] ≤ x ≤ b[i]`

## Inputs & Outputs

### Input Format

- The first line is an integer `n`, which represents the number of segments.
- The next `n` lines contain a pair of numbers representing the coordinates of a segment. Each pair indicates the start and end of a segment.

### Input Constraints

There are at least 2 segments in the array

### Output Format

The output contains a single integer

## Examples

### Example 1

#### Input

```
3
1 3
2 5
3 6
```

#### Output

```
1
```

#### Explanation

We have segments `[{1,3}, {2,5}, {3,6}]`. All of these segments contain the point with coordinate `3`. Hence, the output for this example is `1`.

### Example 2

#### Input

```
4
4 7
1 3
2 5
5 6
```

#### Output

```
2
```

#### Explanation

We have 4 segments `[{4,7}, {1,3}, {2,5}, {5,6}]`. The second and third segments contain `3`. The first and fourth segments contain `6`. So, the output for this example is `2`.

## User Task

Your task is to complete the function `solution()` which takes in an integer `numOfsets` and a two dimensional array `arr` as parameters and returns an integer. You don't need to read the input as a string, just write code within the function block directly.
