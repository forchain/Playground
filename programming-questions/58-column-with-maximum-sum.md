# 58. Column With Maximum Sum

> 难度与建议用时：Medium-1 30 mins

array

## Problem Statement

You are given an array of numbers and a value for `n`. The number `n` splits the array into `n-sized` groups. After splitting, these groups are stacked on top of each other (see below). You have to find the **column-wise sum** and return the column number that has the **largest sum**. In case two or more columns have the same sum, return the **smallest** column number of these. Please note that the column number which should be returned is **1-indexed**.

## Input & Output

### Input Format

- The first line is the number of elements in the input array
- The second line contains input array elements separated by spaces
- The third line is the value of `n`, i.e., the number of elements to be grouped in each subgroup

### Input Constraints

- `2 <= n <= 100`
- `n` will always divide input array into equal-length groups

### Output Format

- A valid column number which has the largest sum

## Examples

### Example 1

#### Input

```
12
4 14 12 7 14 16 5 13 7 16 11 19
4
```

#### Output

```
2
```

#### Explanation

The array elements `4 14 12 7 14 16 5 13 7 16 11 19` are divided into subgroups of size `4` so we get

```
[[4, 14, 12,  7],
[14, 16, 5, 13],
[7, 16, 11, 19]]
```

When we compute the column wise sum we have

```
25, 46, 28, 39
```

the maximum value of `46` is in column 2 therefore it is returned as output

### Example 2

#### Input

```
9
14 9 19 6 13 13 3 2 12
3
```

#### Output

```
1
```

#### Explanation

The array elements `14 9 19 6 13 13 3 2 12` are divided into subgroups of size `3` so we get

```
[
  [14, 9, 19],
  [6, 13, 13],
  [24, 2, 12]
]
```

When we compute the column-wise sum we get

```
44, 24, 44
```

Both column `1` and `3` have the same sum of `44`. But, as `1` is smaller, that is returned as the output.

## User Task

Your task is to complete the function solution() which returns the expected answer. You don't need to read the input, just write code within the function block directly.
