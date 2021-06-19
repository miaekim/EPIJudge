from typing import Optional

from list_node import ListNode
from test_framework import generic_test

def list_len(L: ListNode) -> int:
    size = 0
    tmp = L
    while tmp:
        tmp = tmp.next
        size += 1
    return size

def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    if L is None:
        return L
    n = list_len(L)
    if k > n:
        k = k % n
    if k == 0:
        return L

    head, fast, slow = L, L, L
    for _ in range(k):
        fast = fast.next

    while fast and fast.next:
        fast = fast.next
        slow = slow.next

    new_head = slow.next
    if slow and fast:
        slow.next = None
        fast.next = head
    return new_head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('list_cyclic_right_shift.py',
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
