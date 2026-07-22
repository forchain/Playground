# 74. Find Common Vowels

> 难度与建议用时：Medium-1 30 mins

string

## Problem Statement

You are given two strings `str_1` and `str_2`. You have to find the vowels in `str_1` that are also present in `str_2`. The output must be a concatenation of the common vowels, in alphabetical order. If there are no common vowels, you must return an empty string.

## Input & Output

### Input Format

The first line is a string which contains `str_1` The second line is a string which contains `str_2`

### Input Constraints

- Both strings have at least 1 character
- All characters in both strings are lower-case

### Output Format

A single string which is satisfies the given condition.

## Examples

### Example 1

#### Input

```
float
arose
```

#### Output

```
ao
```

#### Explanation

The common vowels in `float` and `arose` are `ao` sorted in alphatical order

### Example 2

#### Input

```
equivalent
fraction
```

#### Output

```
ai
```

#### Explanation

The common vowels in `equivalent` and `fraction` are `ai` sorted in alphatical order

## User Task

Your task is to complete the function `solution()` which takes 2 strings `string1` and `string2` as input and returns another string as output. You don't need to read the input as a string, just write code within the function block directly.
