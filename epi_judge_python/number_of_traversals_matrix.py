from test_framework import generic_test


def number_of_ways(n: int, m: int) -> int:
    memory = [[1] * m]
    for _ in range(1, n):
        memory.append([1] + ([0] * (m - 1)))

    for row in range(1, n):
        for col in range(1, m):
            memory[row][col] = memory[row - 1][col] + memory[row][col - 1]
    return memory[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
