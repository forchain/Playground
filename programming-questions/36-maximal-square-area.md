# 36. Maximal Square Area

> 难度与建议用时：Hard-2 45 mins

array

2d array

dynamic programming

## Problem Statement

Given a 2D binary matrix filled with 0s and 1s, find the area of the largest square containing only 1s.

## Input & Output

### Input Format

- The first line contains two integers `n` and `m`, the number of rows and columns in the matrix.
- The next `n` lines each contain `m` integers (0 or 1), representing the binary matrix.

### Input Constraints

- 1 ≤ n, m ≤ 100
- Each element of the matrix is either 0 or 1.

### Output Format

- Return a single integer, the area of the largest square containing only 1s.

## Examples

### Example 1

#### Input

```
4
5
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
```

#### Output

```
4
```

#### Explanation

The largest square containing only 1s has a side length of 2, so the area is 2 * 2 = 4.

### Example 2

#### Input

```
3
3
0 1 0
1 1 1
1 1 1
```

#### Output

```
4
```

#### Explanation

The largest square containing only 1s has a side length of 2, so the area is 2 * 2 = 4.

### Example 3

#### Input

```
2 2
0 0
0 0
```

#### Output

```
0
```

#### Explanation

There are no 1s in the matrix, so the largest square area is 0.

## User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.
