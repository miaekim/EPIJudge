import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from collections import deque
def exterior_binary_tree(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    left = []
    leaf = []
    right = []
    def traverse(node: BinaryTreeNode, is_left: bool, is_right: bool):
        if node is None:
            return
        if is_left:
            left.append(node)
        elif is_right:
            right.append(node)
        elif node.left == None and node.right == None:
            leaf.append(node)
            return
        
        traverse(node.left, is_left, 0 if node.right or is_left else is_right)
        traverse(node.right, 0 if node.left or is_right else is_left, is_right)
        

    traverse(tree, 1, 1)
    return left + leaf + right[::-1]


def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_exterior.py', 'tree_exterior.tsv',
                                       create_output_list_wrapper))
