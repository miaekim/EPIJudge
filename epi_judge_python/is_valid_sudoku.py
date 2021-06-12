from typing import List

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    sudoku_size = 9
    sub_size = 3
    # check if there are dupe numbers in row
    for i in range(sudoku_size):
        visited = [False] * sudoku_size
        for j in range(sudoku_size):
            if partial_assignment[i][j] != 0:
                if visited[partial_assignment[i][j]-1] == False:
                    visited[partial_assignment[i][j]-1] = True
                else:
                    return False
    
    for j in range(sudoku_size):
        visited = [False] * sudoku_size
        for i in range(sudoku_size):
            if partial_assignment[i][j] != 0:
                if visited[partial_assignment[i][j]-1] == False:
                    visited[partial_assignment[i][j]-1] = True
                else:
                    return False

    for i in range(0,sudoku_size,3):
        for j in range(0,sudoku_size,3):
            visited = [False] * sudoku_size
            for _i in range(0,sub_size):
                for _j in range(0,sub_size):
                    if partial_assignment[i+_i][j+_j] != 0:
                        if visited[partial_assignment[i+_i][j+_j] -1] == False:
                            visited[partial_assignment[i+_i][j+_j] - 1] = True
                        else:
                            return False
    
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
