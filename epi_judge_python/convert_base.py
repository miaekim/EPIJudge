from string import digits
from test_framework import generic_test
import math
import sys

hex_to_dec = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}

dec_to_hex = {
    0 : '0',
    1 : '1',
    2 : '2',
    3 : '3',
    4 : '4',
    5 : '5',
    6 : '6',
    7 : '7',
    8 : '8',
    9 : '9',
    10 : 'A',
    11 : 'B',
    12 : 'C',
    13 : 'D',
    14 : 'E',
    15 : 'F'
}

EPSILON = 0.000000001
def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    sign = ''
    if num_as_string[0] == '-':
        sign = '-'
        num_as_string = num_as_string[1:]
    # Convert b1 to decimal
    decimal = 0
    for idx, s in enumerate(reversed(num_as_string)):
        decimal += hex_to_dec[s] * (b1 ** idx)

    if decimal == 0:
        return "0"
    # Convert decimal to b2
    digit = math.ceil(math.log(decimal, b2) + EPSILON)
    result = [sign]
    for idx in reversed(range(digit)):
        num =  decimal // (b2 ** idx)
        result.append(dec_to_hex[num])
        decimal -= num * (b2 ** idx)
    return "".join(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
