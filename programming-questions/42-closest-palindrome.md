# 42. Closest Palindrome

> 难度与建议用时：Expert-2 60 mins

string

palindrome

math

## Problem Statement

Given a string `n` representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.

## Input & Output

### Input Format

- A single string `n` representing a positive integer.

### Input Constraints

- `1 <= len(n) <= 18`
- `n` consists of digits only and does not have leading zeros.

### Output Format

- Return a string representing the closest palindrome.

## Examples

### Example 1

#### Input

```
123
```

#### Output

```
121
```

#### Explanation

The closest palindrome to 123 is 121.

### Example 2

#### Input

```
1
```

#### Output

```
0
```

#### Explanation

The closest palindromes to 1 are 0 and 2. Since there is a tie, the smaller one (0) is returned.

### Example 3

#### Input

```
808
```

#### Output

```
818
```

#### Explanation

The closest palindrome to 808 is 818.

## User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.
