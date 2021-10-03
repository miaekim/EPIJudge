import functools
from typing import List, Set
from collections import defaultdict
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
 
# 0  3  6  9  0  2
# bathandbeyond
# bath and bat beyond
# bath and beyond
# bat hand beyond
def decompose_into_dictionary_words(domain: str,
                                    dictionary: Set[str]) -> List[str]:
    n = len(domain)
    @functools.lru_cache(None)
    def recursive(start: int) -> List[str]:
        nonlocal n
        nonlocal domain
        nonlocal dictionary

        if start == n:
            return []
        candidates = []

        for i in range(start+1,n+1):
            if domain[start:i] in dictionary:
                candidates.append([domain[start:i]] + recursive(i))
        
        for candidate in candidates:
            if "-1" not in candidate[-1]:
                return candidate
        return ["-1"]

    result = recursive(0)
    if "-1" not in result:
        return result
    else:
        return []

@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_decomposable_into_words.py',
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
