from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:

    m, n = len(individual_play_scores), final_score + 1
    array = [[0] * n for _ in range(m)]
    for row, score in enumerate(individual_play_scores):
        array[row][0] = 1
        for col in range(1, n):
            prev_row = array[row -1][col] if row >= 1 else 0
            prev_col = array[row][col - score] if col >= score else 0
            array[row][col] = prev_col + prev_row
    return array[-1][-1]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
