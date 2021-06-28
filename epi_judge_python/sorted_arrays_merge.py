from typing import List

from test_framework import generic_test
import heapq

def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    merged = [x for array in sorted_arrays for x in array]
    heapq.heapify(merged)
    result = []
    while merged:
        result.append(heapq.heappop(merged))
    return result
    
    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
