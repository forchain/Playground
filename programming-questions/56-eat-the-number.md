# 56. Eat the number

> 难度与建议用时：Medium-1 30 mins

array

## Problem Statement

A number can eat the number to the right of it if it's smaller than itself. After eating that number, it becomes the sum of itself and that number. Your job is to return the final array after the leftmost element has finished "eating".

## Input & Output

### Input Format

- The first line contains an integer `n`, the number of elements in input array.
- The next line contains space-separated integers which are the elements of the array.

### Input Constraints

- Each array has at least 2 elements
- Each element is an integer

### Output Format

The output is an array of integers

## Examples

### Example 1

#### Input

```
4
5 3 7 30
```

#### Output

```
15 30
```

#### Explanation

For the array a = [5, 3, 7, 30] , size = 4

- `5` eats `3` to get `[8, 7, 30]`.
- `8` eats `7` to get `[15, 30]`
- `15` cannot eat `30` and hence `[15, 30]` is the final output

### Example 2

#### Input

```
3
5 1 4
```

#### Output

```
10
```

#### Explanation

For the array `a = [5, 1, 4]` , size = 3

- `5` eats `1` to get `[6, 4]`.
- `6` eats `4` to get `[10]` which is the final output

## User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.
