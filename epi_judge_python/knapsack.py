import collections
import functools
from typing import List
from collections import defaultdict
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))

def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    n = len(items)
    memory = {}
    def knapsack(item_idx: int, cap: int) -> int:
        nonlocal items
        nonlocal n
        if (item_idx, cap) in memory:
            return memory[(item_idx, cap)]
        if item_idx < 0 or cap == 0:
            return 0

        item = items[item_idx]

        if item.weight > cap:
            memory[(item_idx, cap)] = knapsack(item_idx - 1, cap)
            return memory[(item_idx, cap)]
        memory[(item_idx, cap)] = max(
            item.value + knapsack(item_idx - 1, cap - item.weight),
            knapsack(item_idx - 1, cap)
        )
        return memory[(item_idx, cap)]

    return knapsack(n - 1, capacity)


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
