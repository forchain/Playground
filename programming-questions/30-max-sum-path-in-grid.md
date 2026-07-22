# 30. Max Sum Path in Grid

> 难度与建议用时：Hard-2 45 mins

array

2d array

dynamic programming

## Problem Statement

You are given a 2D grid of integers with `N` rows and `M` columns. Starting from the top-left corner of the grid `(0, 0)`, you can move either **right** or **down** at each step. Your task is to find the maximum sum of values you can collect by following a path from the top-left corner to the bottom-right corner of the grid `(N-1, M-1)`.

## Input & Output

### Input Format

- The first line contains two integers `N` and `M`, the number of rows and columns in the grid.
- The next `N` lines each contain `M` integers, representing the grid.

### Input Constraints

- `1 <= N, M <= 100`
- `-1000 <= grid[i][j] <= 1000`

### Output Format

- Return a single integer, the maximum sum of values collected along the path.

## Examples

### Example 1

#### Input

```
3 3
1 2 3
4 5 6
7 8 9
```

#### Output

```
29
```

#### Explanation

The path with the maximum sum is `1 -> 4 -> 7 -> 8 -> 9`, with a total sum of `29`.

### Example 2

#### Input

```
2
2
-1 -2
-3 -4
```

#### Output

```
-7
```

#### Explanation

The path with the maximum sum is `-1 -> -2 -> -4`, with a total sum of `-7`.

### Example 3

#### Input

```
4
4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
```

#### Output

```
73
```

#### Explanation

The path with the maximum sum is `1 -> 5 -> 9 -> 13 -> 14 -> 15 -> 16`, with a total sum of `73`.

## User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.
