from typing import List

from test_framework import generic_test


def find_closest_elements_in_sorted_arrays(sorted_arrays: List[List[int]]
                                           ) -> int:
    sorted_iters = [iter(array) for array in sorted_arrays]
    sub_arr = [(next(array), idx) for idx, array in enumerate(sorted_iters)]
    min_range = range = max(sub_arr)[0] - min(sub_arr)[0]
    while all(sub_arr):
        _, min_idx = min(sub_arr)
        sub_arr[min_idx] = (next(sorted_iters[min_idx], None), min_idx)
        if sub_arr[min_idx][0] == None:
            break
        range = max(sub_arr)[0] - min(sub_arr)[0]

        if range < min_range:
            min_range = range
    return min_range


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('minimum_distance_3_sorted_arrays.py',
                                       'minimum_distance_3_sorted_arrays.tsv',
                                       find_closest_elements_in_sorted_arrays))
