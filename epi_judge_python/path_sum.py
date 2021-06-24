from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def traverse(tree: BinaryTreeNode, remaining_weight: int):
    if not tree:
        return False
    if not tree.left and not tree.right:
        return remaining_weight == tree.data

    remaining_weight -= tree.data
    return traverse(tree.left, remaining_weight) or traverse(tree.right, remaining_weight)

def has_path_sum(tree: BinaryTreeNode, remaining_weight: int) -> bool:
    return traverse(tree, remaining_weight)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('path_sum.py', 'path_sum.tsv',
                                       has_path_sum))
