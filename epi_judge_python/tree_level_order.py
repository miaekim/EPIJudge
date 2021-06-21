from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from collections import deque

def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    def get_data(depth: List[BinaryTreeNode]) -> List[int]:
        return [d.data for d in depth]

    if not tree:
        return []
    bfs = []
    depth = deque([tree])
    while depth:
        bfs.append(get_data(depth))
        next_ = deque([])
        while depth:
            next_node = depth.popleft()
            left = next_node.left
            right = next_node.right
            if left:
                next_.append(left)
            if right:
                next_.append(right)
        depth = next_
    return bfs


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
