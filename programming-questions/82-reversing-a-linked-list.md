# 82. Reversing a Linked list

> 难度与建议用时：Hard-1 45 mins

linked list

## Problem Statement

You’re given the pointer to the head node of a linked list. Change the `next` pointers of the nodes so that their order is reversed.

## Input & Output

### Input Format

The first line contains an integer `n`, the number of elements in the linked list. Each of the next `n` lines contains an integer, the `data` values of the elements in the linked list.

### Output Format

The function should return the `head` of the updated list. Which, in turn gets consumed by the driver code which will print the linked list element in the updated order.

## Examples

### Example 1

#### Input

```
5
1
2
3
4
5
```

#### Output

```
5 4 3 2 1
```

#### Explanation

`head` references the list 1 -> 2 -> 3 -> 4 -> 5 -> null

Manipulating the `next` pointers of each node in place and return `head` , now referencing the head of the updated list.

5 -> 4 -> 3 -> 2 -> 1 -> null

### Example 2

#### Input

```
2
5
3
```

#### Output

```
3 5
```

#### Explanation

The reversed version of 5 -> 3 is 3 -> 5

## User Task

Your task is to complete the function `reverseList()` and return the expected answer. You don't need to read the input, just write code within the function block directly.
