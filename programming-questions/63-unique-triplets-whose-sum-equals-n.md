# 63. Unique triplets whose sum equals n

> 难度与建议用时：Medium-2 30 mins

array

## Problem Statement

Given an array of elements `array`, and an integer `k`, find out the number of unique triplets whose sum is equal to `k`. A unique triplet consists of three values from different indices, and triplets with the same values (regardless of order or indices) are considered duplicates and only counted once. Once a triplet is selected, the triplet cannot be reused. So, if you have an array `[1, 2, 3]` and the value of `k` is `6`, `[1, 2, 3]` is your only unique triplets. `[3, 2, 1]`, `[2, 1, 3]` and other triplets using the same triplet in a different order cannot be counted as unique triplets.

## Input & Output

### Input Format

- The first line contains an integer `size`, the number of elements in input array
- The next line contains space-separated integers which are the elements of the array.
- The next line contains the 'k' value i,e., the sum of triplets should equate to

### Input Constraints

The array has at least 3 elements

### Output Format

The output is an integer.

## Examples

### Example 1

#### Input

```
6
1 0 2 6 3 9
11
```

#### Output

```
2
```

#### Explanation

There are two unique triplets whose sum equals `11`, `[0, 2, 9]` and `[2, 6, 3]`

### Example 2

#### Input

```
9
1 2 6 3 4 5 9 10 11
20
```

#### Output

```
5
```

#### Explanation

The unique triplets whose sum equals 20 are

```
[1, 9, 10], [6, 3, 11], [4, 5, 11], [6, 4, 10], [6, 5, 9]
```

### Example 3

#### Input

```
6
1 1 4 5 4 5
10
```

#### Output

```
1
```

#### Explanation

There is only 1 unique triplets whose sum equals 10

```
[1, 4, 5]
```

All other instances are duplicates of the same triplet.

## User Task

Your task is to complete the function `solution()` which takes in an integer `numOfElements`, an array `arr` and another integer `k and returns an integer. You don't need to read the input as a string, just write code within the function block directly.
