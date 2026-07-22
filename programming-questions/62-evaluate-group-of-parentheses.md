# 62. Evaluate group of parentheses

> 难度与建议用时：Medium-2 30 mins

string

stack

## Problem Statement

You are given a balanced parentheses string. That is, each open `"("` has corresponding closed `")"`. You have to compute the total score based on the following rules:

- Substring `s = "()"` has score 1,
- Substring `s1s2` has total score as score of `s1` + score of `s2`, for ex `()()` has total score `1 + 1 = 2`
- Substring `"(s)"` has total score as `2` * score of `"s"`.
- Calculate the total score of the given expression and return it as integer.

## Input & Output

### Input Format

The first line and only line contains a string

### Input Constraints

The string is a balanced parentheses string with at least one pair of balanced parentheses

### Output Format

An integer representing the total score of the string

## Examples

### Example 1

#### Input

```
(()(()))
```

#### Output

```
6
```

#### Explanation

The `(` at index `0` closes only at the end of the string. So, whatever comes within this will be multiplied by 2.

The next `(` at index `1` closes at index `2`, so, this adds 1 to the result.

The next `(` at index `3` closes at index `6`. So, whatever comes between index `3` and `6` will be multiplied by 2.

The last `(` at index `4` closes at index `5`, so, 1 is added to the result

Therefore, the result is `2 * ((2 * 1) + 1) = 6`

### Example 2

#### Input

```
()((()))
```

#### Output

```
5
```

#### Explanation

The `(` at index `0` closes at index `1`. So, 1 is added to the result.

The next `(` at index `2` closes at index `7`. So, whatever comes between index `2` and `7` will be multiplied by 2.

The next `(` at index `3` closes at index `6`. So, whatever comes between index `3` and `6` will be multiplied by 2.

The last `(` at index `4` closes at index `5`, so, 1 is added to the result

Therefore, the result is `1 + (2 * 2 * 1) = 5`

## User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.
