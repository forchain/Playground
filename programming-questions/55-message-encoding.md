# 55. Message Encoding

> 难度与建议用时：Medium-1 30 mins

string

## Problem Statement

You are given a string `message` which needs to be encoded based on the following steps:

1. The length of the message to be encoded must be **exactly** 9 characters and all the characters must be lowercase letters. If either of these conditions are not met, the message must be encoded to `invalid`
2. The string must be divided into three parts, of three characters each. The first part `part_1` is the first three characters, `part_2` is the next three characters, `part_3` is the last three characters. These parts will be used in a later step.
3. The first and the third letter must be converted to the corresponding number (a = 1, b = 2, c = 3...z = 26 etc)
4. Reverse the fourth, fifth and sixth characters of the original message ('abc' will be converted to 'cba')
5. Replace the seventh, eighth and ninth letter of the original string with the next letter of the alphabet (a -> b, b -> c, z -> a)
6. Return the string in the following order: `part_3` + `part_1` + `part_2`

## Input & Output

### Input Format

The first line contains a string

### Output Format

A single string

## Examples

### Example 1

#### Input

```
moirarose
```

#### Output

```
ptf13o9rar
```

#### Explanation

We start with Step 1: The message contains exactly nine characters and has only lowercase characters so the message is valid

Step 2: The string is divided into 3 parts: `moi`, `rar`, `ose`

Step 3: The first and the third letter must be converted to the corresponding letter: `m=13`, `i=9`, so the string is `13o9rarose`

Step 4: Reverse the fourth, fifth and sixth characters of the original message: `rar` gets reversed to `rar`, so the string now is, `1309rarrose`

Step 5: Replace the seventh, eighth and ninth letter with the next letter of the alphabet. `ose` gets replaced with `ptf`

Step 6: Return the string in the following order: `part_3` + `part_1` + `part_2`: part3 is `ptf`, part_2 is `13o9`, part_1 is `rar`. The string to be returned is `ptf13o9rar`

### Example 2

#### Input

```
AlexisRose
```

#### Output

```
invalid
```

#### Explanation

The message contains uppercase characters.

## User Task

Your task is to complete the function `solution()` which takes a string `message` and returns the expected answer. You don't need to read the input as a string, just write code within the function block directly.
