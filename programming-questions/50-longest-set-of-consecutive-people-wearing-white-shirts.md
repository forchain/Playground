# 50. Longest set of consecutive people wearing **white shirts**

> 难度与建议用时：Hard-1 45 mins

bit manipulation

## Problem Statement

You are given a binary string, `bin_str` which represents people standing in a line. A binary string is a string which contains only `0’s` and `1’s`. A `0`, in this case, represents a person wearing a **black** shirt and a `1` represent a person wearing a **white** shirt. You are required to find the length of the longest set of consecutive people wearing **white shirts**, given that you are allowed to perform **at most** one swap between a person wearing a white shirt and a black one.

## Input & Output

### Input Format

The first and only line of input is the string `bin_str`

### Input Constraints

The string has at least 2 characters

### Output Format

The output is an integer

## Examples

### Example 1

#### Input

```
11111000
```

#### Output

```
5
```

#### Explanation

We see that the longest set of consecutive `1's` (people wearing white shirts) starts at index `0` and ends at index `4`. There are no additional `1's` for us to perform any swaps with, so the length of the longest consecutive set of people wearing white shirts is 5.

### Example 2

#### Input

```
111011101
```

#### Output

```
7
```

#### Explanation

By performing a swap between the `0` at index `3` and the `1` at index `8`, we get 7 consecutive `1's` starting at index `0` and ending at index `6`. so the length of the longest consecutive set of people wearing white shirts is 7.

## User Task

Your task is to complete `solution()` which accepts a string as a parameter and returns an integer. You don't need to read the input, just use the parameter(s) of the function and write code within the function block and return the required answer.
