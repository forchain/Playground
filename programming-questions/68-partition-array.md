# 68. Partition Array

> 难度与建议用时：Medium-2 30 mins

array

greedy

## Problem Statement

You are given an array `arr` of integers of length `n`. Your task is to check whether it is possible to divide the array into 2 parts such that the first part contains one of the elements of the array and the second part contains all the other elements, and the product of all the elements in the second part equal the value of the element in the first part. If it is possible to achieve this, return the index (0-indexed) of the element you have chosen as your first part. If there are multiple answers, return the answer with the smallest index. If it is not possible to divide the array in this way, return -1.

## Input & Output

### Input Format

- The first line contains the number of elements in the input array
- The second line contains the elements of the input array separated by spaces.

### Input Constraint

```
2 <= n <= 100
```

### Output Format

An integer which is the index of the element in the first part, or -1

## Examples

### Example 1

#### Input

```
4
2 8 4 1
```

#### Output

```
1
```

#### Explanation

We see that 8 = 2 * 4 * 1, and 1 is the index of 8

### Example 2

#### Input

```
3
2 2 8
```

#### Output

```
-1
```

#### Explanation

It is not possible to divide the array in any way to get the required partitions

## User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.
