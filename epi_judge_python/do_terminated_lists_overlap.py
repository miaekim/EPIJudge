import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    def get_len(head):
        _len = 0
        while head:
            _len += 1
            head = head.next
        return _len

    l0_head, l1_head = l0, l1
    l0_len, l1_len = get_len(l0), get_len(l1)
    l0, l1 = l0_head, l1_head
    if l1_len > l0_len:
        for _ in range(l1_len - l0_len):
            l1 = l1.next
    elif l0_len > l1_len:
        for _ in range(l0_len - l1_len):
            l0 = l0.next
        
    while l0 and l1:
        if l0 == l1:
            return l0
        l0 = l0.next
        l1 = l1.next
    return None


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
