# 14. String Rotation Check

> 难度与建议用时：Medium-2 30 mins

string

rotation

## Problem Statement

Given two strings `s1` and `s2`, determine if `s2` is a **left-rotation** of `s1`.
A **left-rotation** here means that you take some number of characters from the **beginning** of the string `s1` and append them to the end of `s1` to form `s2`.

## Input & Output

### Input Format

- The first line contains a string `s1`.
- The second line contains a string `s2`.

### Input Constraints

- 1 ≤ |s1|, |s2| ≤ 100
- Both strings consist of lowercase English letters only.

### Output Format

- Return the length of the rotation if `s2` is a **left-rotation** of `s1`.
- If `s2` is not a rotation of `s1`, return `-1`.

## Examples

### Example 1

#### Input

```
abcde
deabc
```

#### Output

```
3
```

#### Explanation

`s2` is a rotation of `s1` by 3 characters ("abcde" rotated by 3 becomes "deabc").

### Example 2

#### Input

```
hello
lohel
```

#### Output

```
2
```

#### Explanation

`s2` is a rotation of `s1` by 2 characters ("hello" rotated by 2 becomes "lohel").

### Example 3

#### Input

```
abc
cabd
```

#### Output

```
-1
```

#### Explanation

`s2` is not a rotation of `s1`.

## User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.
