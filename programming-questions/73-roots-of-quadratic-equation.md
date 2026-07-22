# 73. Roots of Quadratic Equation

> 难度与建议用时：Medium-2 30 mins

math

## Problem Statement

Write a program to find roots of quadratic equation in the form ax2 + bx + c where a, b & c are integers. The equation will always yield integer roots.

## Input & Output

### Input Format

The first and only line of input contains 3 integers which represent the coefficients (constants a, b and c in the equation in the problem statement) of the quadratic equation.

### Input Constraints

```
-10000 <= a,b,c <= 10000
```

### Output Format

The output must be a string of space-separated integers which are the roots of the equation.

## Examples

### Example 1

#### Input

```
1 4 3
```

#### Output

```
-1 -3
```

#### Explanation

Solving the equation for x2 + 4x + 3, we find the roots of the equation are -1 and -3

### Example 2

#### Input

```
1 2 1
```

#### Output

```
-1 -1
```

#### Explanation

Solving the equation for x2 + 2x + 1, we find the roots of the equation are -1 and -1

## User Task

Your task is to complete `solution()` which accepts three integers a, b & c and returns a string which is contains the roots of the equation, separated by a space. You don't need to read the input, just write code within the function block directly.
