from typing import Iterator, List

from test_framework import generic_test


def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    sunset = []
    for idx, height in enumerate(sequence):
        while sunset and sunset[-1][1] <= height:
            sunset.pop()
        sunset.append((idx, height))

    return [idx for idx, _ in sunset[::-1]]


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
