from typing import List

from test_framework import generic_test

from math import sqrt

# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    # TODO - you fill in here.
    result = []
    for candidate in range(2, n+1):
        for divider in range(2, int(sqrt(n)) + 1):
            if candidate != divider and candidate % divider == 0:
                break
        else:
            result.append(candidate)
        
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
