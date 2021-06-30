from typing import List

from test_framework import generic_test

import bisect
def search_first_of_k(A: List[int], k: int) -> int:
    result = bisect.bisect_left(A, k)
    if not A or result == len(A) or A[result] != k:
        return -1
    else:
        return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
