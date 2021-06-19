from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    head, fast, slow = L, L, L
    for _ in range(k):
        fast = fast.next

    if fast is None:
        return head.next
    fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
