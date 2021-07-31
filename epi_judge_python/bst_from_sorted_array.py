import functools
from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test
from test_framework.binary_tree_utils import (binary_tree_height,
                                              generate_inorder)
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def build_min_height_bst_from_sorted_array(A: List[int]) -> Optional[BstNode]:
    def build_min_height_bst_from_sorted_array_with_size(arr: List[int], n: int):
        if n == 0:
            return None

        mid = n // 2
        return BstNode(
            arr[mid],
            build_min_height_bst_from_sorted_array_with_size(arr[:mid], mid),
            build_min_height_bst_from_sorted_array_with_size(arr[mid +1:], n - mid - 1)
        )
    return build_min_height_bst_from_sorted_array_with_size(A, len(A))


@enable_executor_hook
def build_min_height_bst_from_sorted_array_wrapper(executor, A):
    result = executor.run(
        functools.partial(build_min_height_bst_from_sorted_array, A))

    if generate_inorder(result) != A:
        raise TestFailure('Result binary tree mismatches input array')
    return binary_tree_height(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'bst_from_sorted_array.py', 'bst_from_sorted_array.tsv',
            build_min_height_bst_from_sorted_array_wrapper))
