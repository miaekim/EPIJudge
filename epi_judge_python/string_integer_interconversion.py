from string import digits
from test_framework import generic_test
from test_framework.test_failure import TestFailure

DIGITS = "0123456789"
def int_to_string(x: int) -> str:
    result = []
    if x < 0:
        sign = "-"
        x = x * -1
    else:
        sign = ""

    if x == 0:
        return "0"

    while x > 0:
        for idx, d in enumerate(DIGITS):
            if x % 10 == idx:
                result.append(d)
                break
        x //= 10
    return sign + "".join(reversed(result))


def string_to_int(s: str) -> int:
    result = 0
    sign = -1 if s[0] == "-" else 1
    for s_idx, _s in enumerate(reversed(s)):
        if _s in DIGITS:
            result += (10 ** s_idx) * DIGITS.index(_s)
    return result * sign


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
