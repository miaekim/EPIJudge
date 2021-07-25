from functools import partial
from typing import List

from test_framework import generic_test


def find_salary_cap(target_payroll: int, current_salaries: List[int]) -> float:
    if target_payroll == sum(current_salaries):
        return max(current_salaries)

    n = len(current_salaries)
    current_salaries.sort()

    partial_payroll = target_payroll
    for count_down in range(n):
        fake_cap = partial_payroll * 1.0 / (n - count_down) 
        if current_salaries[count_down] >= fake_cap:
            return fake_cap
        partial_payroll -= current_salaries[count_down]
    return -1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('find_salary_threshold.py',
                                       'find_salary_threshold.tsv',
                                       find_salary_cap))
