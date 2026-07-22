import unittest
from solution import Node, detectLoop
def make_list(values, target):
    nodes=[Node(value) for value in values]
    for left,right in zip(nodes,nodes[1:]): left.next=right
    if nodes and target >= 0: nodes[-1].next=nodes[target]
    return nodes[0] if nodes else None
class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(detectLoop(make_list([2,5,-4,3],1)))
        self.assertTrue(detectLoop(make_list([1,2],0)))
        # 原题第三例声明 N=2 却只给一个节点；按实际节点数据构造单节点无环链表。
        self.assertFalse(detectLoop(make_list([5],-1)))
if __name__ == "__main__": unittest.main()
