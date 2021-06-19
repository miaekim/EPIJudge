import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

def cut_cycle(L:ListNode) -> ListNode:
    head = fast = slow = L

    while fast and fast.next and slow:
        if fast == slow and slow != L:
            while head and slow:
                if head == slow:
                    while slow:
                        if slow.next == head:
                            slow.next = None
                            return L
                        else:
                            slow = slow.next
                else:
                    head = head.next
                    slow = slow.next 
        fast = fast.next.next
        slow = slow.next
    return L


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



def has_cycle(head: ListNode) -> Optional[ListNode]:
    fast = slow = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            it = head
            # Both iterators advance in tandem.
            while it is not slow:
                it = it.next
                slow = slow.next
            return it  # iter is the start of cycle.
    return None  # No cycle.

def overlapping_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
    # print(l0, "and",l1)
    l0_cycle, l1_cycle = has_cycle(l0), has_cycle(l1)
    # print(l0_cycle, "and",l1_cycle) 
    l0_cycle_head, l1_cycle_head = l0_cycle, l1_cycle
    while l0_cycle and l1_cycle:
        if l0_cycle.data == l1_cycle_head.data:
            return l0_cycle
        if l1_cycle.data == l0_cycle_head.data:
            return l1_cycle

        l0_cycle = l0_cycle.next
        l1_cycle = l1_cycle.next
        if l0_cycle.data == l0_cycle_head.data:
            return None
        if l1_cycle.data == l1_cycle_head.data:
            return None

    if l0_cycle is None and l1_cycle is None: 
        return overlapping_no_cycle_lists(l0, l1)
    else:
        return None


@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_lists_overlap.py',
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))
