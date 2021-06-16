from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:

    l1 = L1
    l2 = L2
    head = ListNode()
    head_ptr = head
    while l1 and l2:
        if l2.data < l1.data:
            head_ptr.next = l2
            l2 = l2.next
        else:
            head_ptr.next = l1
            l1 = l1.next
        head_ptr = head_ptr.next
    head_ptr.next = l1 or l2
        
    return head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
