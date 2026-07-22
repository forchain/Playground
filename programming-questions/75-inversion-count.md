# 75. Inversion Count

> 难度与建议用时：Medium-1 30 mins

array

## Problem Statement

Given an array `a` of length `n`, two elements `a[i]` and `a[j]` form an inversion if `a[i]` > `a[j]` and `i` < `j`. Find the number of inversions the array contains.

## Inputs & Outputs

### Input Format

- The first line of input contains an integer which is the length of the array.
- The next line of input contains the elements of the array, separated by spaces.

### Input Constraints

For the length of the array `n`

```
2 <= n <= 10000
```

### Output Format

The output will be an integer which contains the number of inversions

## Examples

### Example 1

#### Input

```
5
2 4 1 3 5
```

#### Output

```
3
```

#### Explanation

The inversions of the array `[2, 4, 1, 3, 5]` are: `(2, 1)`, `(4, 2)`, `(4, 3)`

So, the number of inversions are `3`

### Example 2

#### Input

```
3
1 2 5
```

#### Output

```
0
```

#### Explanation

The array `[1, 2, 5]` is already sorted, so the number of inversions is 0.

## User Task

Your task is to complete the function `solution()` which takes an array length and the array as input and returns the inversion count. You don't need to read the input as a string, just write code within the function block directly.
