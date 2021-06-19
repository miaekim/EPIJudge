from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    def list_size(L: ListNode):
        size = 0
        temp = L
        while temp:
            size += 1
            temp = temp.next
        return size
    lenL, depth = list_size(L), 0
    head = L
    if lenL == k:
        return L.next
    while depth < lenL - k - 1:
        L = L.next
        depth += 1
    if L.next is None:
        L = None
    else:
        L.next = L.next.next

    return head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
