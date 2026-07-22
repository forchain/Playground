# 22. Count Palindromic Substrings

> 难度与建议用时：Hard-1 45 mins

string

palindrome

substring

## Problem Statement

Given a string `s`, your task is to count the number of distinct palindromic substrings in the string. A substring is a contiguous sequence of characters within a string, and a palindrome is a string that reads the same backward as forward.

## Input & Output

### Input Format

- A single string `s` of length `n`.

### Input Constraints

- 1 ≤ n ≤ 1000
- The string `s` consists of lowercase English letters only.

### Output Format

- Return a single integer, the count of distinct palindromic substrings in the string.

## Examples

### Example 1

#### Input

```
ababa
```

#### Output

```
5
```

#### Explanation

The distinct palindromic substrings are: `a`, `b`, `aba`, `bab`, `ababa`.

### Example 2

#### Input

```
abc
```

#### Output

```
3
```

#### Explanation

The distinct palindromic substrings are: `a`, `b`, `c`.

### Example 3

#### Input

```
aaa
```

#### Output

```
3
```

#### Explanation

The distinct palindromic substrings are: `a`, `aa`, `aaa`.

## User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.
