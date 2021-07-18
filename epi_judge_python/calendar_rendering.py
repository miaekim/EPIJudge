import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A: List[Event]) -> int:
    starts = sorted([a.start for a in A])
    finishs = sorted([a.finish for a in A])

    n = len(A)
    start_idx, finish_idx = 0, 0
    simultaneous = 0
    max_simultaneous = 0
    for x in range(0, finishs[-1]+1):
        while start_idx < n and starts[start_idx] <= x:
            start_idx += 1        
            simultaneous += 1
        max_simultaneous = max(max_simultaneous, simultaneous)
        while finish_idx < n and  finishs[finish_idx] <= x:
            finish_idx += 1
            simultaneous -= 1
    return max_simultaneous


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
