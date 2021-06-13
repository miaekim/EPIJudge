import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    n = len(s)
    s.reverse()
    start = 0
    for idx in range(n):
        if s[idx] != ' ':
            start = idx
            break
    for idx in range(start, n + 1):
        if idx == n or s[idx] == ' ':
            s[start:(None if idx == n else idx)] = s[idx - 1:(None if start - 1 < 0 else start - 1):-1]
            start = idx + 1
    return


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
