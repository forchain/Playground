# 28. Find Longest Repeating Substring

> 难度与建议用时：Hard-2 45 mins

string

searching

## Problem Statement

You are given a string `s`. Your task is to find the length of the longest substring that repeats itself at least twice in the given string. The repeated substrings must not overlap.

## Input & Output

### Input Format

- A single string `s` consisting of only lowercase English letters.

### Input Constraints

- 1 ≤ |s| ≤ 10^3 (where |s| is the length of the string)

### Output Format

- Return an integer representing the length of the longest repeating substring or `0` if no such substring exists.

## Examples

### Example 1

#### Input

```
ababc
```

#### Output

```
2
```

#### Explanation

The longest substring that repeats is `ab`, appearing twice in `ababc`.

### Example 2

#### Input

```
aaaa
```

#### Output

```
2
```

#### Explanation

The substring `aa` is the longest repeated substring in `aaaa`, with no overlaps

### Example 3

#### Input

```
abcdef
```

#### Output

```
0
```

#### Explanation

There are no repeating substrings in `abcdef`.

## User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.
