# 51. Sum of weights of the mangoes

> 难度与建议用时：Hard-1 45 mins

array

greedy

sliding window

## Problem Statement

You are given an array of integers, `weights` where each integer in the array represents the weight of a mango. You have to find the number of ways in which one mango can be removed from the list, such that the sum of weights of the mangoes at the even positions and the sum of weights of mangoes at the odd positions in the resulting list, are equal

## Input & Output

### Input Format

- The first line of input contains an integer
- The next line contains a single line of space separated integers

### Input Constraints

For each weight `w` in the array, `1 <= w <= 10000`

### Output Format

The output must be an integer which satisfies the required condition

## Examples

### Example 1

#### Input

```
4
3 1 7 4
```

#### Output

```
1
```

#### Explanation

We see that removing the mango at index 1 (0-based indexing) modifies the list to `[3, 7, 4]`, and `weights[0] + weights[2] = weights[1] (3 + 4 = 7)`. This is the only way to satisfy the required condition. So, the output is 1.

### Example 2

#### Input

```
3
3 3 3
```

#### Output

```
3
```

#### Explanation

We see that by removing any of the mangoes from the list, the sum of weights at the even and odd indices become equal. For example, removing element at index 0, modifies the list to `[3, 3]`, and `weights[0] = weights[1]`. This holds true if we remove elements at index 1 and index 2 as well. Therefore, the number of ways to satisfy the required condition is 3.

## User Task

Your task is to complete `solution()` which accepts a list as a parameter and returns an integer. You don't need to read the input, just use the parameter(s) of the function and write code within the function block and return the required answer.
