import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

import functools
def replace_and_remove(size: int, s: List[str]) -> int:
    final_size = size
    idx = 0

    a_count = 0
    b_count = 0
    while idx < size:
        if s[idx] == 'b':
            b_count += 1
            final_size -= 1
        else:
            if s[idx] == 'a':
                a_count += 1
            s[idx - b_count] = s[idx]
        idx += 1

    idx = final_size - 1
    while a_count > 0:
        if s[idx] == 'a':
            s[idx + a_count] = 'd'
            a_count -= 1
            s[idx + a_count] = 'd'
            final_size += 1
        else:
            s[idx + a_count] = s[idx]
        idx -= 1
    return final_size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
