import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]
    
    smol_idx = 0
    lrge_idx = len(A) - 1

    idx = 0
    while lrge_idx >= smol_idx:
        if A[idx] < pivot:
            smol_idx = smol_idx + 1
        else:
            A[idx], A[lrge_idx] = A[lrge_idx], A[idx]
            lrge_idx = lrge_idx - 1
            continue
        idx = idx + 1

    idx = smol_idx
    lrge_idx = len(A) - 1

    while idx < lrge_idx:
        if A[idx] == pivot:
            smol_idx = smol_idx + 1
        else: 
            A[idx], A[lrge_idx] = A[lrge_idx], A[idx]
            lrge_idx = lrge_idx - 1
            continue
        idx = idx + 1


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
