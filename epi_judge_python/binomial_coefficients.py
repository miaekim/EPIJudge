from test_framework import generic_test


def compute_binomial_coefficient(n: int, k: int) -> int:
    factorials = [1, 1]
    for num in range(2, n + 1):
        factorials.append(factorials[-1] * num)
    return (factorials[n] // factorials[n - k]) // factorials[k]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('binomial_coefficients.py',
                                       'binomial_coefficients.tsv',
                                       compute_binomial_coefficient))
