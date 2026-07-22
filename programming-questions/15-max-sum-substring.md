# 15. Max Sum Substring

> 难度与建议用时：Medium-2 30 mins

string

greedy

sliding window

## Problem Statement

Given a string of digits, you need to determine the largest sum of a contiguous substring whose digits are strictly decreasing from left to right.

A substring must consist of one or more consecutive characters from the string.

## Input & Output

### Input Format

- A single string `s` consisting of digits (0-9).

### Input Constraints

- `1 <= length(s) <= 1000`

### Output Format

- Return the **maximum possible sum** of digits of any contiguous substring where each digit is **strictly less than the previous digit**.

## Examples

### Example 1

#### Input

```
9875
```

#### Output

```
29
```

#### Explanation

The substring "9875" gives the maximum sum of `9 + 8 + 7 + 5 = 29`.

### Example 2

#### Input

```
1234
```

#### Output

```
4
```

#### Explanation

No two adjacent digits form a strictly decreasing pair.
The maximum sum comes from the single digit substring `4`.

### Example 3

#### Input

```
404
```

#### Output

```
4
```

#### Explanation

Valid strictly decreasing substrings:

- `4`
- `40 → 4 + 0 = 4`

The maximum sum is `4`.

## User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.
