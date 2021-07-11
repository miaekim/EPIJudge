from typing import List

from test_framework import generic_test

from collections import Counter
"""

[1, 2, 1, 3, 1, 2, 1]	3	TODO
"""
def longest_subarray_with_distinct_entries(A: List[int]) -> int:
    subarray = []
    _max = float('-inf')
    for idx, a in enumerate(A):
        if a in subarray:
            n = len(subarray)
            if n > _max:
                _max = n
            dupe_idx = subarray.index(a)
            subarray = subarray[dupe_idx+1:] if dupe_idx < n - 1 else []
        subarray.append(a)

    n = len(subarray)
    if n > _max:
        _max = n
    return _max


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_subarray_with_distinct_values.py',
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
