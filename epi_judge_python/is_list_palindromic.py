from list_node import ListNode
from test_framework import generic_test

def reverse(L: ListNode) -> ListNode:
    prev, curr = None, L
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev
    
def is_linked_list_a_palindrome(L: ListNode) -> bool:
    if L is None:
        return True
    head = L
    mid, tail = L, L
    while tail and tail.next:
        tail = tail.next.next
        mid = mid.next

    back = reverse(mid)
    while head and back:
        if head.data != back.data:
            return False
        head = head.next
        back = back.next
    return True
    
        
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
