import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))

# is endpoint1 less than endpoint2?
def _lt(endpoint1, endpoint2):
    if endpoint1.val < endpoint2.val:
        return True
    elif endpoint1.val > endpoint2.val:
        return False

    if not endpoint1.is_closed and endpoint2.is_closed:
        return True
    return False

def union_of_intervals(intervals: List[Interval]) -> List[Interval]:
    if not intervals:
        return []

    intervals.sort(key=lambda x: x.left.val - int(x.left.is_closed) * 0.1)
    unions = []
    curr = intervals[0]
    for interval in intervals[1:]:
        if (curr.right.val > interval.left.val) or (curr.right.val == interval.left.val and (curr.right.is_closed or interval.left.is_closed)):
            left_ = curr.left
            right_ =  interval.right if(_lt(curr.right, interval.right)) else curr.right
            curr = Interval(left_, right_)
        else:
            unions.append(curr)
            curr = interval
    unions.append(curr)
    return unions


@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [(i.left.val, i.left.is_closed, i.right.val, i.right.is_closed)
            for i in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intervals_union.py',
                                       'intervals_union.tsv',
                                       union_of_intervals_wrapper))
