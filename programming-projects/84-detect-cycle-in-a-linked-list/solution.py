class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def detectLoop(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
