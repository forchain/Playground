# 33. Longest Common Subsequence

> 难度与建议用时：Hard-2 45 mins

string

dynamic programming

subsequence

## Problem Statement

Given two strings `s1` and `s2`, find the length of their longest common subsequence (LCS). A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example, "abc", "abg", "bdf" are subsequences of "abcdefg".

## Input & Output

### Input Format

- The first line contains a string `s1`.
- The second line contains a string `s2`.

### Input Constraints

- 1 ≤ |s1|, |s2| ≤ 1000
- Both strings consist of lowercase English letters only.

### Output Format

- Return a single integer, the length of the longest common subsequence.

## Examples

### Example 1

#### Input

```
abcde
ace
```

#### Output

```
3
```

#### Explanation

The longest common subsequence is "ace" with length 3.

### Example 2

#### Input

```
abc
def
```

#### Output

```
0
```

#### Explanation

There is no common subsequence between "abc" and "def".

### Example 3

#### Input

```
abcde
abcde
```

#### Output

```
5
```

#### Explanation

The longest common subsequence is the entire string "abcde" with length 5.

## User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.
