import unittest
from solution import Node, reverseList
def linked(values):
    head = None
    for value in reversed(values): head = Node(value, head)
    return head
def values(head):
    result=[]
    while head: result.append(head.data); head=head.next
    return result
class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(values(reverseList(linked([1,2,3,4,5]))), [5,4,3,2,1])
        self.assertEqual(values(reverseList(linked([5,3]))), [3,5])
if __name__ == "__main__": unittest.main()
