class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def reverseList(head):
    previous = None
    current = head
    while current is not None:
        # 必须先保存后继；改写 current.next 后将无法再从当前节点向前走。
        following = current.next
        current.next = previous
        previous = current
        current = following
    return previous
