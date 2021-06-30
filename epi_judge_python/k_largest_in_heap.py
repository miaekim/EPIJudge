from typing import List

from test_framework import generic_test, test_utils
import heapq

def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    min_heap = []
    heapq.heapify(min_heap)
    min_heap_size = 0
    for a in A:
        heapq.heappush(min_heap, a)
        min_heap_size += 1

        if min_heap_size > k:
            heapq.heappop(min_heap)
    return min_heap


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
