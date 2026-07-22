class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def deleteNode(head, k):
    if k == 1:
        return head.next
    previous = head
    for _ in range(k - 2):
        previous = previous.next
    previous.next = previous.next.next
    return head
