from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from collections import deque

def traverse(tree: BinaryTreeNode, depth: int):
    if not tree:
        return depth, True
    else:
        depth_left, is_left_balanced = traverse(tree.left, depth + 1)
        depth_right, is_right_balanced = traverse(tree.right, depth + 1)
        if is_left_balanced and is_right_balanced:
            return (max(depth_left, depth_right), abs(depth_left - depth_right) <= 1)
        else:
            return (max(depth_left, depth_right), False)


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    _, is_balanced = traverse(tree, 0)
    return is_balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
