from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def stable_sort_list(L: ListNode) -> Optional[ListNode]:
    if L is None:
        return None
    indexes = []
    index = 0
    while L:
        indexes.append(L)

        j = index - 1
        while j >= 0 and L.data < indexes[j].data:
            indexes[j + 1] = indexes[j]
            j -= 1
        indexes[j + 1] = L

        index += 1
        L = L.next

    for idx in range(index - 1):
        indexes[idx].next = indexes[idx + 1]
    indexes[-1].next = None

    return indexes[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_list.py', 'sort_list.tsv',
                                       stable_sort_list))
