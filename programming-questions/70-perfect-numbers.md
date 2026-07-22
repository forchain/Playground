# 70. Perfect Numbers

> 难度与建议用时：Medium-1 30 mins

math

## Problem Statement

Given an integer `n`, find out all perfect numbers from 1 to n (1 and n are included). A perfect number is a number whose sum of factors is the same number, excluding itself. If there are no numbers to print, an empty string must be returned.

## Inputs & Outputs

### Input Format

The first and only line of input contains the integer `n`

### Input Constraints

For the integer n `2 <= n <= 1000000`

### Output Format

It should be a string of space-separated integers. The output should be a string of space-separated integers which are perfect numbers. If there are no numbers to print, return an empty string

## Examples

### Example 1

#### Input

```
7
```

#### Output

```
6
```

#### Explanation

The only number which has the sum of factors equal to the number itself between 1 and 6 is 6. Factors of 6 excluding 6 are 1, 2, 3

Sum of the factors `1 + 2 + 3 = 6`

### Example 2

#### Input

```
200
```

#### Output

```
6 28
```

#### Explanation

Factors of 6 excluding 6 are 1, 2, 3

Sum of the factors `1 + 2 + 3 = 6`

Factors of 28 excluding 28 are 1, 2, 4, 7, 14

Sum of the factors = `1 + 2 + 4 + 7 + 14 = 28`

## User Task

Your task is to complete `solution()` which accepts an integer and returns a string of space separated perfect numbers between 1 and n. You don't need to read the input, just write code within the function block directly.
