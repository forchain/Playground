# 31. Longest Palindromic Subsequence

> 难度与建议用时：Hard-2 45 mins

string

dynamic programming

palindrome

## Problem Statement

Given a string `s`, find the length of the longest palindromic subsequence in the string. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

## Input & Output

### Input Format

- A single string `s`.

### Input Constraints

- 1 ≤ |s| ≤ 1000 (where |s| is the length of the string `s`)
- The string `s` consists of lowercase English letters only.

### Output Format

- Return an integer representing the length of the longest palindromic subsequence.

## Examples

### Example 1

#### Input

```
abdbca
```

#### Output

```
5
```

#### Explanation

The longest palindromic subsequence is "abdba", which has a length of 5.

### Example 2

#### Input

```
cbbd
```

#### Output

```
2
```

#### Explanation

The longest palindromic subsequence is "bb", which has a length of 2.

### Example 3

#### Input

```
a
```

#### Output

```
1
```

#### Explanation

The longest palindromic subsequence is "a", which has a length of 1.

## User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.
