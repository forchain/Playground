# 12. Find Majority Element

> 难度与建议用时：Medium-2 30 mins

array

searching

## Problem Statement

Given an array of integers, find the majority element. A majority element is an element that appears more than ⌊n/2⌋ times in the array, where n is the size of the array. If no such element exists, return -1.

## Input & Output

### Input Format

- The first line contains an integer n, the size of the array.
- The second line contains n integers, the elements of the array.

### Input Constraints

- 1 ≤ n ≤ 100
- -10^9 ≤ array[i] ≤ 10^9

### Output Format

- Return the majority element if it exists, otherwise return -1.

## Examples

### Example 1

#### Input

```
5
3 3 4 2 3
```

#### Output

```
3
```

#### Explanation

The element `3` appears 3 times, which is more than ⌊5/2⌋ = 2.

### Example 2

#### Input

```
4
1 2 3 4
```

#### Output

```
-1
```

#### Explanation

No element appears more than ⌊4/2⌋ = 2 times.

### Example 3

#### Input

```
6
2 2 1 1 1 2
```

#### Output

```
-1
```

#### Explanation

No element appears more than ⌊6/2⌋ = 3 times.

## User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.
