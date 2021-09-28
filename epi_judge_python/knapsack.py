import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    sorted(items, lambda x: x.weight)
    memory = [[0] * (capacity+1)] * len(items)
    for idx, item in enumerate(items):
        for j in range(1, capacity):
            memory[idx][j] = max(memory[idx][j - 1], memory[idx - item.weight][j] + item.value)
    return 0


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
