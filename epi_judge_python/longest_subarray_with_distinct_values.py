from typing import List

from test_framework import generic_test

from collections import Counter
"""

[1, 2, 1, 3, 1, 2, 1]	3	TODO
"""
def longest_subarray_with_distinct_entries(A: List[int]) -> int:
    recent_idx = {}
    start_idx = 0
    _max = float('-inf')
    for idx, a in enumerate(A):
        if a in recent_idx:
            dupe_idx = recent_idx[a]
            # print(idx, start_idx)
            if dupe_idx >= start_idx:
                _max = max(_max, idx - start_idx)
                start_idx = dupe_idx + 1
        recent_idx[a] = idx

    return max(_max, len(A) - start_idx)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_subarray_with_distinct_values.py',
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
