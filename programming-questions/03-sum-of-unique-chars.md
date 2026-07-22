# 3. Sum of Unique Chars

> 难度与建议用时：Medium-1 30 mins

string

ascii

## Problem Statement

You are given a string `s` consisting of lowercase English letters. Your task is to calculate the sum of the ASCII values of all unique characters in the string. A unique character is one that appears exactly once in the string.

## Input & Output

### Input Format

- A single string `s`, containing only lowercase English letters.

### Input Constraints

- `1 <= len(s) <= 100`

### Output Format

- An integer representing the sum of the ASCII values of all unique characters in the string.

## Examples

### Example 1

#### Input

```
abc
```

#### Output

```
294
```

#### Explanation

The unique characters in `abc` are `a, b, c`. Their ASCII values are 97, 98, and 99, respectively. The sum is `97 + 98 + 99 = 294`.

### Example 2

#### Input

```
abac
```

#### Output

```
197
```

#### Explanation

The unique character in `abac` are `b` and `c`. Its ASCII value is `98` + `99`. Output is 197.

### Example 3

#### Input

```
xyzwx
```

#### Output

```
362
```

#### Explanation

The unique characters in `xyzwx` are `y, z, w`. Their ASCII values are `121` , `122, 119`, respectively. The sum is `121 + 122 + 119 = 362`.

## User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.
