import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
                                             ('duplicate', 'missing'))


def find_duplicate_missing(A: List[int]) -> DuplicateAndMissing:
    n = len(A)
    missing_minus_dupe = int((n * (n - 1)) / 2) -sum(A)
    gap = abs(missing_minus_dupe)
    if missing_minus_dupe > 0:
        candidates = zip(range(gap, n), range(0, n - gap))
    else:
        candidates = zip(range(0, n - gap), range(gap, n))

    
    for missing, dupe in candidates:
        if missing not in A:
            return DuplicateAndMissing(dupe, missing)


def res_printer(prop, value):
    def fmt(x):
        return 'duplicate: {}, missing: {}'.format(x[0], x[1]) if x else None

    return fmt(value) if prop in (PropertyName.EXPECTED,
                                  PropertyName.RESULT) else value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_for_missing_element.py',
                                       'find_missing_and_duplicate.tsv',
                                       find_duplicate_missing,
                                       res_printer=res_printer))
