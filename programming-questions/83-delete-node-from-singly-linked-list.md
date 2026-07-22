# 83. Delete Node From Singly Linked List

> 难度与建议用时：Hard-1 45 mins

linked list

## Problem Statement

Given a singly-linked list, delete its `k`th node. You are provided the address of the head of the linked list and the integer `k`. You must return the head of the modified linked list.

## Input & Output

### Input Format

The first line of each test case contains an integer `N` denoting the number of elements of the linked list. Then in the next line are `N` space separated values of the linked list. The third line of each test case contains an integer `k` which denotes the position at which the node needs to be deleted. (We are using 1-based indexing, so `k=1` refers to the first node.)

### Input Constraints

For the number of nodes `N`,

```
1 <= N <= 10000
```

For the integer `k`,

```
1 <= k <= N
```

### Output

The output for each test case will be the space separated value of the returned linked list.

## Examples

### Example 1

#### Input

```
4
2 4 5 7
3
```

#### Output

```
2 4 7
```

#### Explanation

After deleting the node at the 3rd position, the linked list is 2 4 7.

### Example 2

#### Input

```
3
1 3 4
3
```

#### Output

```
1 3
```

#### Explanation

After deleting the node at the 3rd position, the linked list is 1 3.

## User Task

Your task is to complete the method **deleteNode()** which should delete the node at the `k`th position and return the head of the modified linked list. The code has been set up so that you needn't worry about reading the input, converting it to an array, etc.
