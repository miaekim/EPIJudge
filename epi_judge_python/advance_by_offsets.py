from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    target = len(A) - 1
    furthest = 0
    idx = 0
    while furthest < target and idx <= furthest:
        furthest = max(furthest, idx + A[idx])
        idx += 1

    if furthest >= target:
        return True
    else:
        return False

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
