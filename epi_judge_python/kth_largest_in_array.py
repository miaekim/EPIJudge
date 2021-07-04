from typing import List

from test_framework import generic_test

import heapq

# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:
    # TODO - you fill in here.
    min_heap_size,  min_heap =  0, []
    heapq.heapify(min_heap)

    for a in A:
        if min_heap_size == k:
            if a > min_heap[0]:
                heapq.heappushpop(min_heap, a)
        else:
            heapq.heappush(min_heap, a)
            min_heap_size += 1
    
    return min_heap[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
