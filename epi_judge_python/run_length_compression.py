from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s: str) -> str:
    result = ''
    count = ""
    for idx in range(0, len(s)):
        if s[idx] in "0123456789":
            count += s[idx]
        else:
            cnt, symbol = int(count), s[idx]
            result += symbol * cnt
            count = ""
    return result


def encoding(s: str) -> str:
    result = ''
    if not s:
        return
    count = 1
    for idx in reversed(range(1, len(s))):
        if s[idx] == s[idx - 1]:
            count += 1
        else:
            result = str(count) + s[idx] + result
            count = 1
    result = str(count) + s[0] + result
    return result


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('run_length_compression.py',
                                       'run_length_compression.tsv',
                                       rle_tester))
