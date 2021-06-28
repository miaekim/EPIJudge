from typing import List

from test_framework import generic_test
import heapq

def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    merged = []
    heapq.heapify(merged)
    result = []
    columns = [0] * len(sorted_arrays)
    columns_max = [len(arr) for arr in sorted_arrays]

    for idx, arr in enumerate(sorted_arrays):
        if columns_max[idx] > 0:
            heapq.heappush(merged, (arr[columns[idx]], idx))
            columns[idx] += 1

    while merged:
        _data, _idx = heapq.heappop(merged)
        result.append(_data)
        if columns[_idx] < columns_max[_idx]:
            heapq.heappush(merged, (sorted_arrays[_idx][columns[_idx]], _idx))
            columns[_idx] += 1

    return result
    
    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
