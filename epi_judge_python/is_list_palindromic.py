from list_node import ListNode
from test_framework import generic_test


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    if L is None:
        return True
    head = L
    mid, tail, size = L, L, 0
    while tail and tail.next:
        size += 1
        nxt = tail.next
        nxt.next = tail
        tail = nxt

    
        
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
