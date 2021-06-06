from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    
    num1_sign = 1
    num2_sign = 1
    if num1[0] < 0:
        num1[0] *= -1
        num1_sign = -1
    if num2[0] < 0:
        num2[0] *= -1
        num2_sign = -1

    num3 = [0] * (len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            mul = num3[i+j+1] + num1[i] * num2[j]
            num3[i+j+1] = mul % 10
            num3[i+j] += mul // 10

    while num3[0] == 0 and len(num3) >= 2:
        num3 = num3[1:]
    num3[0] = num3[0] * num1_sign * num2_sign
    return num3


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
