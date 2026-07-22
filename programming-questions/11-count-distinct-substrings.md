# 11. Count Distinct Substrings

> 难度与建议用时：Medium-2 30 mins

string

substring

## Problem Statement

Given a string `s`, your task is to count the number of distinct substrings of `s`. A substring is defined as a contiguous sequence of characters within a string. The empty substring is not considered.

## Input & Output

### Input Format

- A single string `s`.

### Input Constraints

- 1 ≤ |s| ≤ 100
- `s` consists of lowercase English letters only.

### Output Format

- An integer representing the number of distinct substrings of `s`.

## Examples

### Example 1

#### Input

```
abc
```

#### Output

```
6
```

#### Explanation

The distinct substrings of "abc" are: "a", "b", "c", "ab", "bc", "abc". Total = 6.

### Example 2

#### Input

```
aaa
```

#### Output

```
3
```

#### Explanation

The distinct substrings of "aaa" are: "a", "aa", "aaa". Total = 3.

## User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.
