from typing import List
from collections import defaultdict
from test_framework import generic_test


def is_pattern_contained_in_grid(grid: List[List[int]],
                                 pattern: List[int]) -> bool:
    if not grid:
        return False
    
    if not pattern:
        return False

    value_to_idx = defaultdict(list)
    n, m = len(grid), len(grid[0])
    for row in range(n):
        for col in range(m):
            value_to_idx[grid[row][col]].append((row, col))

    prev = pattern[0]
    last_idxes = value_to_idx[prev]
    if not last_idxes:
        return False
        
    for p in pattern[1:]:
        possible_idx = set()
        for row, col in last_idxes:
            if row > 0:
                possible_idx.add((row -1, col))
            if row < n - 1:
                possible_idx.add((row + 1, col))
            if col > 0:
                possible_idx.add((row, col -1))
            if col < m - 1:
                possible_idx.add((row, col + 1))
            
        last_idxes = []
        for idx in value_to_idx[p]:
            if idx in possible_idx:
                last_idxes.append(idx)
        
        if not last_idxes:
            return False
            
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_in_matrix.py',
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
