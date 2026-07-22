# 64. Compare and merge strings

> 难度与建议用时：Medium-2 30 mins

sorting

string

## Problem Statement

You are given two strings `string1` and `string2` made of uppercase letters. You must create a third string `string3` out of them. These are the rules:

- Step 1: Compare the first letter in both strings and pick the smaller of the two. (for eg, if the words are `ABC` and `DEF`, you will pick `A` from the first string)
- Step 2: If both the letters are the same, pick the letter from `string1`
- Step 3: The letter you pick is removed from the original string and gets added to `string3`
- Step 4: You again compare the first two letters in the two strings like in Step 1 above and follow Steps 2 and 3

You follow this process until no letters are left in `string1` and `string2`.

## Input & Output

### Input Format

- The first line contains a string
- The second line contains a string

### Input Constraint

- Both input strings are in upper case
- Each string has at least one alphabet

### Output Format

A single string

## Examples

### Example 1

#### Input

```
ACA
BCF
```

#### Output

```
ABCACF
```

#### Explanation

The table below shows how the process works. We extract characters from both strings step-by-step.

| string1 | string2 | string3 |
| ------- | ------- | ------- |
| ACA     | BCF     |         |
| CA      | BCF     | A       |
| CA      | CF      | AB      |
| A       | CF      | ABC     |
|         | CF      | ABCA    |
|         | F       | ABCAC   |
|         |         | ABCACF  |

### Example 2

#### Input

```
RAJ
RAVI
```

#### Output

```
RAJRAVI
```

#### Explanation

The first letters to choose from are R and R since they are on the top of the stacks. R is chosen from the first string. Then, the options are A and R. A is chosen. Then the two stacks have J and R, so J is chosen. The current string is RAJ. As all the letters from the first stack have been used up, all the characters from the second stack can be appended to the resultant string.

### Example 3

#### Input

```
DAVID
ROSE
```

#### Output

```
DAROSEVID
```

#### Explanation

The first letters to choose from are D and R. D is chosen from the first string. Then, the options are A and R. A is chosen. Then the two stacks have V and R, so R is chosen. The current string is DAR. Next, the letters to choose from are V and O. O is selected. This process continues until all the characters of both stack have been used up.

## User Task

Your task is to complete the function `solution()` which takes 2 strings `string1` and `string2` and returns the expected answer. You don't need to read the input as a string, just write code within the function block directly.
