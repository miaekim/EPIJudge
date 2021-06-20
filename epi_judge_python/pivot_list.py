import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def list_pivoting(l: ListNode, x: int) -> Optional[ListNode]:
    small = ListNode(0)
    big = ListNode(0)
    pivot = ListNode(0)
    small_tail = small
    big_tail = big
    pivot_tail = pivot
    while l:
        if l.data < x:
            small_tail.next = l
            small_tail = small_tail.next
        elif l.data > x:
            big_tail.next = l
            big_tail = big_tail.next
        else:
            pivot_tail.next = l
            pivot_tail = pivot_tail.next
        l = l.next
    big_tail.next = None
    pivot_tail.next = big.next
    small_tail.next = pivot.next
    return small.next

def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
    original = linked_to_list(l)

    l = executor.run(functools.partial(list_pivoting, l, x))

    pivoted = linked_to_list(l)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure('List is not pivoted')
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure('List is not pivoted')

    if sorted(original) != sorted(pivoted):
        raise TestFailure('Result list contains different values')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pivot_list.py', 'pivot_list.tsv',
                                       list_pivoting_wrapper))
