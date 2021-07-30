from typing import Optional

from bst_node import BstNode
from test_framework import generic_test

k_found = False

def find_first_greater_than_k(tree: BstNode, k: int) -> Optional[BstNode]:
    if not tree:
        return None

    if tree.data <= k :
        return find_first_greater_than_k(tree.right, k)
    key = find_first_greater_than_k(tree.left, k)
    return key or tree


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'search_first_greater_value_in_bst.py',
            'search_first_greater_value_in_bst.tsv',
            find_first_greater_than_k_wrapper))
