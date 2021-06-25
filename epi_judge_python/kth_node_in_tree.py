import functools
from typing import Optional

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, size=None):
        self.data = data
        self.left = left
        self.right = right
        self.size = size


def find_kth_node_binary_tree(tree: BinaryTreeNode,
                              k: int) -> Optional[BinaryTreeNode]:

    to_visit = tree
    while to_visit:
        # print(k, to_visit, to_visit.size, to_visit.left.size if to_visit.left else None)
        if k > to_visit.size or  (not to_visit.left and k <= 0):
            return None

        if not to_visit.left:
            if k == 1:
                return to_visit
            to_visit = to_visit.right
            k -= 1
            continue

        if not to_visit.right:
            if k == to_visit.left.size + 1:
                return to_visit
            to_visit = to_visit.left
            continue

        if k > to_visit.left.size + 1:
            k -= (to_visit.left.size + 1)
            to_visit = to_visit.right
        elif k < to_visit.left.size + 1:
            to_visit = to_visit.left
        else:
            return to_visit
        

    return None


@enable_executor_hook
def find_kth_node_binary_tree_wrapper(executor, tree, k):
    def init_size(node):
        if not node:
            return 0
        node.size = 1 + init_size(node.left) + init_size(node.right)
        return node.size

    init_size(tree)

    result = executor.run(functools.partial(find_kth_node_binary_tree, tree,
                                            k))

    if not result:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_node_in_tree.py',
                                       'kth_node_in_tree.tsv',
                                       find_kth_node_binary_tree_wrapper))
