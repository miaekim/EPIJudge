from test_framework import generic_test

memory = [0, 1]
mem_size = 2
def fibonacci(n: int) -> int:
    global mem_size
    if n >= mem_size:
        for i in range(mem_size, n + 1):
            memory.append(memory[i - 1] + memory[i - 2])
            mem_size += 1
    
    return memory[n]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
