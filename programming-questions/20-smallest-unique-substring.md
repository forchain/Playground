# 20. Smallest Unique Substring

> 难度与建议用时：Hard-1 30 mins

string

sliding window

two pointer

## Problem Statement

You are given a string `s`. Your task is to find the length of the smallest substring of `s` that contains all the unique characters in `s`.

## Input & Output

### Input Format

A single string `s` containing lowercase alphabets `a-z`.

### Input Constraints

- 1 ≤ |s| ≤ 10^3 (where |s| is the length of the string)
- The string consists of only lowercase English letters.

### Output Format

Return the length of the smallest substring of `s` that contains all unique characters.

## Examples

### Example 1

#### Input

```
abcaacbb
```

#### Output

```
3
```

#### Explanation

The unique characters in the string are `a, b, c`. The smallest substring that contains all these is `abc`, which has a length of `3`.

### Example 2

#### Input

```
aaa
```

#### Output

```
1
```

#### Explanation

The only unique character in the string is `a`. The smallest substring containing `a` is `a` itself, with a length of `1`.

### Example 3

#### Input

```
abcdef
```

#### Output

```
6
```

#### Explanation

All characters in the string are unique and already present in the same substring. Hence the length is `6`.

## User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.
