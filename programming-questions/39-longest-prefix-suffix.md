# 39. Longest Prefix Suffix

> 难度与建议用时：Expert-1 45 mins

string

searching

## Problem Statement

You are given a string `s`. Your task is to find the length of the longest prefix of the string which is also a suffix. However, this prefix and suffix must not overlap. For example, in the string `abcab`, `ab` is a prefix and also a valid suffix, but they do not overlap.

## Input & Output

### Input Format

- A string `s` consisting of lowercase English letters.

### Input Constraints

- 1 ≤ |s| ≤ 1000 (where |s| is the length of the string)

### Output Format

- An integer representing the length of the longest prefix which is also a suffix and does not overlap.

## Examples

### Example 1

#### Input

```
aabaab
```

#### Output

```
3
```

#### Explanation

The prefix "aab" is also a suffix. It has a length of 3, and it does not overlap.

### Example 2

#### Input

```
abcdef
```

#### Output

```
0
```

#### Explanation

There is no prefix that is also a suffix.

### Example 3

#### Input

```
levellevel
```

#### Output

```
5
```

#### Explanation

The longest prefix "level" is also a suffix and has a length of 5 without overlapping.

## User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.
