# 65. Packing Bags

> 难度与建议用时：Medium-2 30 mins

array

greedy

## Problem Statement

You arrive at the supermarket checkout and you've only got a limited number of shopping bags with you. Miser that you are, you hate buying extra bags when you've got dozens at home that you forgot to bring with you! Can you fit all your shopping into the bags you've got with you?

Each bag can carry a maximum of 10kg and each item you've purchased weighs between 1 and 10kg.

You have to find out if there are enough bags to carry all the items. Return true if there are enough bags to contain all the items, false otherwise.

## Input & Output

### Input Format

The first line contains an integer `n`, the number of elements in input array.

The next line contains `n` space-separated integers which are the elements of the array.

The next line contains an integer which is the number of bags

### Input Constraints

- All weights will be integers between 1 and 10kg inclusive
- Items can be packed in any order
- There may be more than one way to fit all the items in the available bags

## Examples

### Example 1

#### Input

```
12
2 1 2 5 4 3 6 1 1 9 3 2
4
```

#### Output

```
true
```

#### Explanation

Bag 1 = [2, 1, 2, 5] (10kg)

Bag 2 = [4, 3, 3] (10kg)

Bag 3 = [6, 2, 1, 1] (10kg)

Bag 4 = [9] (9kg)

### Example 2

#### Input

```
11
2 7 1 3 3 4 7 4 1 8 2
4
```

#### Output

```
false
```

#### Explanation

Bag 1 = [2, 8] (10kg)

Bag 2 = [3, 7] (10kg)

Bag 3 = [2, 4, 4] (10kg)

Bag 4 = [7, 3] (10kg)

two 1kg items are left over

## User Task

Your task is to complete `solution()` which accepts 3 parameters, the number of elements, the array of items and the number of bags, and returns an integer. You don't need to read the input, just use the parameter(s) of the function and write code within the function block and return the required answer.
