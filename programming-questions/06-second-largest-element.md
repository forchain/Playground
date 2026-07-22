# 6. Second Largest Element

> 难度与建议用时：Medium-1 30 mins

array

sorting

## Problem Statement

You are given an array of integers. Your task is to find the second largest element in the array. If the array does not have at least two distinct elements, return `-1`.

## Input & Output

### Input Format

- An integer `n` denoting the size of the array.
- An array of `n` integers.

### Input Constraints

- `2 <= n <= 100`
- `-10^6 <= array[i] <= 10^6`

### Output Format

- An integer representing the second largest element, or `-1` if there isn’t one.

## Examples

### Example 1

#### Input

```
5
2 3 6 6 5
```

#### Output

```
5
```

#### Explanation

The largest element is `6`. The second largest distinct element is `5`.

### Example 2

#### Input

```
3
10 10 10
```

#### Output

```
-1
```

#### Explanation

The array has only one distinct element, so there is no second largest.

### Example 3

#### Input

```
6
1 2 3 4 5 4
```

#### Output

```
4
```

#### Explanation

The largest element is `5`. The second largest distinct element is `4`.

## User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.
