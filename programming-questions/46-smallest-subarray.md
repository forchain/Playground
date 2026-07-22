# 46. Smallest Subarray

> 难度与建议用时：Hard-1 45 mins

array

sliding window

## Problem Statement

Given an array A, find the size of the smallest subarray such that it contains at least one occurrence of the maximum value of the array and at least one occurrence of the minimum value of the array. A subarray is a contiguous part of the array

## Input & Output

### Input Format

- The first line is the number of elements in the array
- The second line contains space-separated array elements

### Input Constraints

```
1 <= |A| <= 2000
```

### Output Format

The output is an integer which satisfies the required condition

## Examples

### Example 1

#### Input

```
2
1 3
```

#### Output

```
2
```

#### Explanation

The only choice is to take both elements

### Example 2

#### Input

```
1
2
```

#### Output

```
1
```

#### Explanation

The whole array must be taken as it has only one element

### Example 3

#### Input

```
7
1 5 10 7 1 9 4
```

#### Output

```
3
```

#### Explanation

Subarray `{1, 5, 10}` has both maximum and minimum value.

### User Task

Your task is to complete the function `minSubarrayLength()` which takes a number of array elements N and an array as input and returns the expected answer. You don't need to read the input as a string, write code within the function block directly.
