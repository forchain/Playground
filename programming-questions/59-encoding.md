# 59. Encoding

> 难度与建议用时：Medium-1 30 mins

string

## Problem Statement

You are given a string `message` of lowercase characters and an integer `key`. The string needs to be encoded using the integer based on the following rules:

1. Assign a number to each letter in the alphabet. 'a' corresponds to 1, 'b' corresponds to 2, 'c' corresponds to 3 and so on.
2. Starting from the leftmost character of `message`, sum up the integer value of the first character with the first digit of `key`. Then, sum the integer value of the next character with the next digit of `key`. If the digits of `key` are exhausted, start from the first digit of `key` and continue till the characters of `message` are exhausted.
3. Concatenate all the sums you have calculated into a single string, separated by commas, and return it.

## Inputs & Outputs

### Input Format

- The first line contains the `message` string
- The second line contains the integer `key`

### Input Constraint

- `message` has at least 2 characters
- `message` contains only lowercase alphabets
- `key` has at least 2 digits

### Output Format

- A string containing the different sums which have been calculated, separated by commas
- No spaces after the commas

## Examples

### Example 1

#### Input

```
start
1357
```

#### Output

```
20,23,6,25,21
```

#### Explanation

Start with the first character of `message`, which is 's'. Its integer value is 19. Add the first digit of `key`, which is 1, to 19. The integer value of 't' is 20. Adding this to the next digit of `key`, which is 3, gives you a sum of 23. This process continues until the end of the `message` string. The example is explained in the table below.

| message            | s    | t    | a    | r    | t    |
| ------------------ | ---- | ---- | ---- | ---- | ---- |
| message int values | 19   | 20   | 1    | 18   | 20   |
| key                | 1    | 3    | 5    | 7    | 1    |
| sum                | 20   | 23   | 6    | 25   | 21   |

So, the output for this example is: `20,23,6,25,21`

### Example 2

#### Input

```
masterpiece
1939
```

#### Output

```
14,10,22,29,6,27,19,18,6,12,8
```

#### Explanation

| message            | m    | a    | s    | t    | e    | r    | p    | i    | e    | c    | e    |
| ------------------ | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| message int values | 13   | 1    | 19   | 20   | 5    | 18   | 16   | 9    | 5    | 3    | 5    |
| key                | 1    | 9    | 3    | 9    | 1    | 9    | 3    | 9    | 1    | 9    | 3    |
| sum                | 14   | 10   | 22   | 29   | 6    | 27   | 19   | 18   | 6    | 12   | 8    |

## User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.
