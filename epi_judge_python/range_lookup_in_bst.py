import collections
from typing import List

from bst_node import BstNode
from test_framework import generic_test

from collections import deque

Interval = collections.namedtuple('Interval', ('left', 'right'))


def range_lookup_in_bst(tree: BstNode, interval: Interval) -> List[int]:
    left, right = interval.left, interval.right

    to_visit = deque([tree])
    result = []
    while to_visit:
        node = to_visit.popleft()
        if not node:
            continue

        if node.data >= left:
            to_visit.append(node.left)
        if node.data <= right:
            to_visit.append(node.right)
        if left <= node.data <= right:
            result.append(node.data)
    return sorted(result)


def range_lookup_in_bst_wrapper(tree, i):
    return range_lookup_in_bst(tree, Interval(*i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('range_lookup_in_bst.py',
                                       'range_lookup_in_bst.tsv',
                                       range_lookup_in_bst_wrapper))
