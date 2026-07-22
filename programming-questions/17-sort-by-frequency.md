# 17. Sort by Frequency

> 难度与建议用时：Medium-2 30 mins

array

sorting

frequency

## Problem Statement

Given an array of integers, sort the array in decreasing order of frequency of elements. If two elements have the same frequency, the one with the smaller value should come first.

## Input & Output

### Input Format

- The first line contains an integer `n`, the size of the array.
- The second line contains `n` integers, the elements of the array.

### Input Constraints

- 1 ≤ n ≤ 100
- -10^3 ≤ array[i] ≤ 10^3

### Output Format

- Return the sorted array as a **space-separated string**.

## Examples

### Example 1

#### Input

```
6
4 5 6 5 4 3
```

#### Output

```
4 4 5 5 3 6
```

#### Explanation

The frequency of elements is:

- 4: 2 times
- 5: 2 times
- 6: 1 time
- 3: 1 time

Since 4 and 5 have the highest frequency, they come first. Between 4 and 5, 4 is smaller, so it comes first. The remaining elements are sorted by their values.

### Example 2

#### Input

```
5
1 2 2 3 3
```

#### Output

```
2 2 3 3 1
```

#### Explanation

The frequency of elements is:

- 2: 2 times
- 3: 2 times
- 1: 1 time

Since 2 and 3 have the highest frequency, they come first. Between 2 and 3, 2 is smaller, so it comes first. The remaining element is 1.

## User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.
