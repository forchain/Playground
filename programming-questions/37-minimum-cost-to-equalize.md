# 37. Minimum Cost to Equalize

> 难度与建议用时：Hard-2 40 mins

array

greedy

## Problem Statement

You are given an array `A` of size `N` consisting of positive integers. You can perform the following operation any number of times:

- Choose any element of the array and either increment or decrement it by 1. Each operation costs 1 unit.

Your task is to determine the minimum cost required to make all elements of the array equal.

## Input & Output

### Input Format

- The first line contains a single integer `N`, the size of the array.
- The second line contains `N` space-separated integers, the elements of the array `A`.

### Input Constraints

- 1 ≤ N ≤ 100,000
- 1 ≤ A[i] ≤ 10,000

### Output Format

- Return a single integer, the minimum cost required to make all elements of the array equal.

## Examples

### Example 1

#### Input

```
5
1 2 3 4 5
```

#### Output

```
6
```

#### Explanation

The optimal strategy is to make all elements equal to 3. The cost is:

- |1 - 3| + |2 - 3| + |3 - 3| + |4 - 3| + |5 - 3| = 2 + 1 + 0 + 1 + 2 = 6.

### Example 2

#### Input

```
4
10 20 30 40
```

#### Output

```
40
```

#### Explanation

The optimal strategy is to make all elements equal to 25. The cost is:

- |10 - 25| + |20 - 25| + |30 - 25| + |40 - 25| = 15 + 5 + 5 + 15 = 40.

### Example 3

#### Input

```
3
7 7 7
```

#### Output

```
0
```

#### Explanation

All elements are already equal, so the cost is 0.

## User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.
