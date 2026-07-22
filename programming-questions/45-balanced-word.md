# 45. Balanced Word

> 难度与建议用时：Medium-1 30 mins

## Problem Statement

We assign a value to each character in a word, based on their position in the alphabet (a = 1, b = 2, ... , z = 26). A balanced word is one where the sum of values of the characters on the left-hand side of the word equals the sum of values of the characters on the right-hand side.

Complete the function `solution` that returns integer `1` if the word is balanced, and `0` if it's not. Return `-1` if the word has an odd number of letters.

## Input & Output

### Input Format

The first line contains a String input

### Input Constraints

All words will be lowercase, and have a minimum of 2 characters

### Output Format

The output must be an integer which satisfies the required condition

## Examples

### Example 1

#### Input

```
zips
```

#### Output

```
1
```

#### Explanation

The input string `zips` is divided to `zi` and `ps`.

- Sum of the position of characters in `zi` is 26 + 9 is 35
- Sum of the position of characters in `ps` is 16 + 19 is 35

As the sum of left-hand side and right-hand side characters is same so return 1

### Example 2

#### Input

```
bray
```

#### Output

```
0
```

#### Explanation

```
The input string bray divided to br and ay
- Sum of the values of characters in br is 20
- Sum of the position of characters in  ay is 26
```

### Example 3

#### Input

```
arise
```

#### Output

```
-1
```

#### Explanation

As `arise` has an odd number of letters, the output is -1

## User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.
