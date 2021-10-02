from test_framework import generic_test
import functools 

@functools.lru_cache(None)
def number_of_ways_to_top(top: int, maximum_step: int) -> int:
    if top <= 0:
        return 0

    return (top <= maximum_step) + sum([
        number_of_ways_to_top(top - t, maximum_step) for t in range(1, maximum_step + 1)
    ])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_staircase.py',
                                       'number_of_traversals_staircase.tsv',
                                       number_of_ways_to_top))
