import functools
from typing import Optional, Tuple

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

def sub_lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Tuple[int, Optional[BinaryTreeNode]]:

    if tree == None:
        return 0, tree

    if tree == node0 and tree == node1:
        return 2, tree

    cnt = 0
    if tree == node0:
        cnt = cnt + 1
    if tree == node1:
        cnt = cnt + 1

    right_cnt, right_node = sub_lca(tree.right, node0, node1)
    if right_cnt == 2:
        return 2, right_node
    left_cnt, left_node = sub_lca(tree.left, node0, node1)
    if left_cnt == 2:
        return 2, left_node

    return cnt + right_cnt + left_cnt, tree

def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    cnt, node = sub_lca(tree, node0, node1)
    if cnt == 2:
        return node
    else:
        return None


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
