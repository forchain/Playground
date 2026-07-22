# 19. Longest Prefix Match

> 难度与建议用时：Medium-2 30 mins

string

## Problem Statement

You are given two strings `s1` and `s2`. Your task is to find the longest prefix string that is common to both `s1` and `s2`. If no such prefix exists, return an empty string.

## Input & Output

### Input Format

- The first line contains the string `s1`.
- The second line contains the string `s2`.

### Input Constraints

- `1 <= len(s1), len(s2) <= 10^5`
- Both strings contain only lowercase English letters ('a' to 'z').

### Output Format

- A single string representing the longest common prefix between `s1` and `s2`.

## Examples

### Example 1

#### Input

```
abcd
abcxyz
```

#### Output

```
abc
```

#### Explanation

The common prefix between `s1` and `s2` is "abc".

### Example 2

#### Input

```
hello
world
```

#### Output

```

```

#### Explanation

The strings `s1` and `s2` have no common prefix, so the result is an empty string.

## User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.
