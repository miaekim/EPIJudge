from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from collections import deque
from collections import namedtuple

def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    Node = namedtuple('Node', ('node', 'left_visited'))
    if not tree:
        return []
    traversal = []
    to_visit = [Node(node=tree, left_visited=0)]

    while to_visit:
        node, left_visited = to_visit.pop()
        if not node:
            continue
        if left_visited:
            traversal.append(node.data)
        else:
            to_visit.append(Node(node=node.right, left_visited=0))
            to_visit.append(Node(node=node, left_visited=1))
            to_visit.append(Node(node=node.left, left_visited=0))
    return traversal


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))
