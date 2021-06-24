from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def traverse(tree: BinaryTreeNode, _sum: int):
    if tree:
        _sum = (_sum << 1) + tree.data
        if tree.left and tree.right:
            _sum = traverse(tree.left, _sum) + traverse(tree.right, _sum) 
        elif tree.left:
            _sum = traverse(tree.left, _sum)
        elif tree.right:
            _sum = traverse(tree.right, _sum)
    return _sum


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    # TODO - you fill in here.
    return traverse(tree, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
