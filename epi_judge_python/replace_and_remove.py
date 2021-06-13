import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

import functools
def replace_and_remove(size: int, s: List[str]) -> int:
    final_size = size
    idx = 0
    while idx < final_size:
        if s[idx] == 'b':
            for i in range(idx + 1, final_size):
                s[i - 1] = s[i]
            final_size -= 1
        if s[idx] == 'a':
            for i in reversed(range(idx + 1, final_size)):
                s[i + 1] = s[i]
            s[idx] = 'd'
            s[idx + 1] = 'd'
            final_size += 1
            idx += 2
        if idx < final_size and s[idx] != 'a' and s[idx] != 'b':
            idx += 1 
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
