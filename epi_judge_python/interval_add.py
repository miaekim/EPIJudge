import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))

def is_overlay(left: Interval, right: Interval) -> bool:
    if not right:
        return False
    if (left.right < right.left) or (right.right < left.left):
        return False
    return True

def union(left: Interval, right: Interval):
    if left.left > right.left:
        left, right = right, left
    if left.right < right.right:
        return Interval(left=left.left, right=right.right)
    else:
        return left

def add_interval(disjoint_intervals: List[Interval],
                 new_interval: Interval) -> List[Interval]:
    merged_intervals = []

    for disjoint_interval in disjoint_intervals:
        if is_overlay(disjoint_interval, new_interval):
            new_interval = union(disjoint_interval, new_interval)
        else:
            if new_interval and new_interval.right < disjoint_interval.left:
                merged_intervals.append(new_interval)
                new_interval = None
            merged_intervals.append(disjoint_interval)
    
    if new_interval:
        merged_intervals.append(new_interval)
    return merged_intervals


@enable_executor_hook
def add_interval_wrapper(executor, disjoint_intervals, new_interval):
    disjoint_intervals = [Interval(*x) for x in disjoint_intervals]
    return executor.run(
        functools.partial(add_interval, disjoint_intervals,
                          Interval(*new_interval)))


def res_printer(prop, value):
    def fmt(x):
        return [[e[0], e[1]] for e in x] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('interval_add.py',
                                       'interval_add.tsv',
                                       add_interval_wrapper,
                                       res_printer=res_printer))
