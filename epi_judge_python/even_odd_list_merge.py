from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    if L is None:
        return L 

    even_head, odd_head = L, L.next
    even, odd = even_head, odd_head

    while even and even.next and odd and odd.next:
        even.next = odd.next
        odd.next = even.next.next

        even = even.next
        odd = odd.next

    even.next = odd_head
    return even_head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
