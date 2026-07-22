import unittest
from solution import Node, deleteNode
def linked(values):
    head=None
    for value in reversed(values): head=Node(value,head)
    return head
def values(head):
    result=[]
    while head: result.append(head.data); head=head.next
    return result
class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(values(deleteNode(linked([2,4,5,7]),3)), [2,4,7])
        self.assertEqual(values(deleteNode(linked([1,3,4]),3)), [1,3])
if __name__ == "__main__": unittest.main()
