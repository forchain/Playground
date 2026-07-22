# 57. Rearrange Sentence

> 难度与建议用时：Medium-1 30 mins

string

sorting

## Problem Statement

Given a sentence with numbers representing a word's location embedded within each word of given sentence, return the sorted sentence according to the numbers in each word.

## Input & Output

### Input Format

The first and only line of input is a string

### Input Constraints

Only integers between 1 and 9 will be present in the string

### Output Format

The output will be a string

## Examples

### Example 1

#### Input

```
is2 Thi1s T4est 3a
```

#### Output

```
This is a Test
```

#### Explanation

- the word `is2` contains 2 - so the word `is` location is `2`
- the word `Thi1s` contains 1 - so the word `This` location is `1`
- the word `T4est` contains 4 - so the word `Test` location is `4`
- the word `3a` contain 3 - so the word `a` location is `3`

so when we rearrange we get output :

```
This is a Test
```

### Example 2

#### Input

```
is3 Cri1stiano 4the Rona2ldo 5best
```

#### Output

```
Cristiano Ronaldo is the best
```

#### Explanation

- word `is3` contains number `3`, so its location in output string is `3`.
- word `Cri1stiano` contains number `1`, so its location in output string is `1`.
- word `4the` contains number `4`, so its location in output string is `4`.
- word `Rona2ldo` contains number `2`, so its location in output string is `2`.
- word `5best` contains number `5`, so its location in output string is `5`

so the output is, `Cristiano Ronaldo is the best`

## User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.
