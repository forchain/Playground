# 53. Expensive Words

> 难度与建议用时：Medium-1 30 mins

string

## Problem Statement

Each letter in a sentence is worth its position in the alphabet (i.e. a = 1, b = 2, c = 3, d = 4, e = 5,..., z = 26). Uppercase alphabets have the same values as lowercase ones. However, if a word is **all** in UPPERCASE, the value of that word is doubled. Complete the function `solution()` that calculates the total value of the words in a sentence. Non-alphabet characters are ignored in this calculation.

## Input & Output

### Input Format

The first and only line of input contains a string.

### Input Constraints

- The sentence has at least one word
- Ignore spaces and punctuation
- Remember that the value of a word isn't doubled unless all the letters in it are uppercased.

### Output Format

The output is an integer

## Examples

### Example 1

#### Input

```
abc ABC Abc
```

#### Output

```
24
```

#### Explanation

- Word 1's value = 1 + 2 + 3 = 6
- Word 2's value = (1 + 2 + 3) x 2 = 12
- Word 3's value = 1 + 2 + 3 = 6

Total value = 6 + 12 + 6 = 24

### Example 2

#### Input

```
ab-c A-BC
```

#### Output

```
18
```

#### Explanation

- Word 1's value = 1 + 2 + 3 = 6
- Word 2's value = (1 + 2 + 3) x 2 = 12

Total value = 6 + 12 = 18

## User Task

Your task is to complete the function `solution()` which returns the expected answer. You don't need to read the input, just write code within the function block directly.
