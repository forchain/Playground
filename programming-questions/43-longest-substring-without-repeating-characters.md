# 43. Longest substring without repeating characters

> 难度与建议用时：Medium-2 30 mins

string

sliding window

## Problem Statement

Given a string `s`, find the length of the longest substring without repeating characters

## Input & Output

### Input Format

The first and only line contains the string `s`

### Input Constraints

`s` has at least one character

### Output Format

An integer representing the length of the longest substring

## Examples

### Example 1

#### Input

```
abcabcbb
```

#### Output

```
3
```

#### Explanation

The longest substring without repeating characters is abc. So, the value returned is 3.

### Example 2

#### Input

```
abcda
```

#### Output

```
4
```

#### Explanation

The longest substring without repeating characters is abcd. So, the value returned is 4.

### Example 3

#### Input

```
aaacbb
```

#### Output

```
3
```

#### Explanation

The longest substring without repeating characters is acb. So, the value returned is 3.

## User Task

Your task is to complete the function `solution()` which takes in the string `s` as a parameter and returns an integer. You don't need to read the input as a string, just write code within the function block directly.
