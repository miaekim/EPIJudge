import functools
import random

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    check_sequence_is_uniformly_random, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook

import math

def zero_one_random():
    return random.randrange(2)

def uniform_random(lower_bound: int, upper_bound: int) -> int:
    binary_digit = math.ceil(math.log2(upper_bound)) + 1 # 2 -> 2, 3 -> 2, 4 -> 3, 8 -> 4, 16 -> 5
    range_ = upper_bound - lower_bound
    number = 0
    while binary_digit:
        number = (number << 1) | zero_one_random()
        binary_digit = binary_digit - 1

        if number > range_:
            number = 0
            binary_digit = math.ceil(math.log2(upper_bound))
            
    return number + lower_bound


@enable_executor_hook
def uniform_random_wrapper(executor, lower_bound, upper_bound):
    def uniform_random_runner(executor, lower_bound, upper_bound):
        result = executor.run(
            lambda:
            [uniform_random(lower_bound, upper_bound) for _ in range(100000)])

        return check_sequence_is_uniformly_random(
            [a - lower_bound for a in result], upper_bound - lower_bound + 1,
            0.01)

    run_func_with_retries(
        functools.partial(uniform_random_runner, executor, lower_bound,
                          upper_bound))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('uniform_random_number.py',
                                       'uniform_random_number.tsv',
                                       uniform_random_wrapper))
