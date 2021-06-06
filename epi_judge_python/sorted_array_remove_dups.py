import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
# 2 3 5 5 7 11 11 11 13
def delete_duplicates(A: List[int]) -> int:
    if not A:
        return 0

    uniq_cnt = 1
    deleted_cnt = 0
    next_dupe = 1
    for idx in reversed(range(len(A) - 1)):
        if A[idx + next_dupe] == A[idx]:
            deleted_cnt += 1
            for i in range(idx, len(A) - deleted_cnt):
                A[i] = A[i + 1]
        else:
            uniq_cnt += 1

    return uniq_cnt


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
