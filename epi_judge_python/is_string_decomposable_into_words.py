import functools
from typing import List, Set
from collections import defaultdict
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
 
# 0  3  6  9  0  2
# bedbathandbeyond.com
# bed bath and beyond
# bed bat hand beyond
TRIE_END = "$"
def decompose_into_dictionary_words(domain: str,
                                    dictionary: Set[str]) -> List[str]:
    n = len(domain)
    trie = {}

    for keyword in dictionary:
        trie_ptr = trie
        for key in keyword:
            if key not in trie_ptr:
                trie_ptr[key] = {}
            trie_ptr = trie_ptr[key]
        trie_ptr["$"] = {}

    
    def recursive(start: int, decompose: List[str]):
        nonlocal n
        nonlocal trie

        print(start, decompose)
        if start == n:
            return decompose

        trie_ptr = trie

        for i in range(start, n):
            if domain[start:i]

        # for i in range(start, n):
        #     if TRIE_END in trie_ptr:
        #         r_decompose = recursive(i, decompose + [domain[start:i]])
        #         if r_decompose:
        #             return r_decompose
        #     if domain[i] in trie_ptr:
        #         trie_ptr = trie_ptr[domain[i]]
        #     elif TRIE_END not in trie_ptr:
        #         break
        return []

    return recursive(0, [])


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
