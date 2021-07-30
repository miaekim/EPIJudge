from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils

def find_k_largest_with_count(tree: BstNode, k:int):
    result, count = [], 0
    if not tree:
        return result, count

    if tree.right:
        result, count = find_k_largest_with_count(tree.right, k)
        if count >= k:
            return result, count
    
    result.append(tree.data)
    count += 1

    if count >= k:
        return result, count

    if tree.left:
        result_left, count_left = find_k_largest_with_count(tree.left, k - count)
        return result + result_left, count + count_left

    return result, count

def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    result, _ = find_k_largest_with_count(tree, k)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
