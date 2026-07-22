# 84. Detect Cycle in a Linked List

> 难度与建议用时：Hard-1 45 mins

linked list

## Problem Statement

You are given a linked list of `N` nodes. The task is to check if the linked list has a loop.

## Input & Output

### Input Format

The first line of each test case contains the number of elements in a linked list. The second line shows space-separated nodes of the linked list. The third line shows the index in the linked list to which the last node is connected.

**Note**: Third line will be used only for test cases. It should not be passed as an argument in the function.

### Input Constraints

For the number of nodes `N`

```
1 <= N <= 1000
```

### Output Format

The output for each test case is 1 if it has a loop and 0 otherwise.

### Examples

#### Example 1

#### Input

```
4
2 5 -4 3
1
```

#### Output

```
1
```

#### Explanation

Here, the last node (3) points to a node with index number 1 which creates a loop.

#### Example 2

#### Input

```
2
1 2
0
```

#### Output

```
1
```

#### Explanation

Here, the last node (2) points to a node with index number 0 which creates a loop.

#### Example 3

#### Input

```
2
5
-1
```

#### Output

```
0
```

#### Explanation

Here, the last node (5) points to a node with index number -1 which doesn't exist. So, it doesn't create a loop.

## User Task

The task is to complete the function **detectLoop**(). The function should return whether the linked list is forming any loop. If it is forming a loop, return `true` else return `false`.
