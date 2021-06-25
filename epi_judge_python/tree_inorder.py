from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from collections import deque
from collections import namedtuple

def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    Node = namedtuple('Node', ('node', 'visited'))
    if not tree:
        return []
    traversal: List[Node] = deque([Node(node=tree, visited=0)])
    to_visit = 1

    while to_visit > 0:
        curr, node_idx = None, None
        for idx, (node, visited) in enumerate(traversal):
            if not visited:
                curr = node
                node_idx = idx
                break
        if curr.right:
            traversal.insert(node_idx+1, Node(node=curr.right, visited = 0))
            to_visit += 1
        # traversal[node_idx].visited = 1
        traversal[node_idx]  = Node(node=curr, visited = 1)
        to_visit -= 1
        if curr.left:
            traversal.insert(node_idx, Node(node=curr.left, visited = 0))
            to_visit += 1
    return list(map(lambda x: x.node.data, traversal))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))
