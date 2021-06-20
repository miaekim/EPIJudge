from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def add_two_numbers(L1: ListNode, L2: ListNode) -> Optional[ListNode]:
    result_head = ListNode()
    result = result_head
    carry = 0
    while L1 or L2:
        if L1:
            l1 = L1.data
            L1 = L1.next
        else:
            l1 = 0

        if L2:
            l2 = L2.data
            L2 = L2.next
        else:
            l2 = 0

        _sum = l1 + l2 + carry
        carry = _sum // 10
        left = _sum % 10
        result.next = ListNode(left)
        result = result.next
    if carry:
        result.next = ListNode(carry)
    return result_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_list_add.py',
                                       'int_as_list_add.tsv', add_two_numbers))
