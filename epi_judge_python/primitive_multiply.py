from test_framework import generic_test

def addition(x, y):
    result = 0
    carry_over = 0

    while True:
        if x == 0:
            return y
        elif y == 0:
            return x
        
        result = x ^ y
        carry_over = (x & y) << 1

        if carry_over == 0:
            break
        else:
            x = result
            y = carry_over

    return result 

def multiply(x: int, y: int) -> int:
    result = 0
    while y:
        if y & 1:
            result = addition(result, x)
        y = y >> 1
        x = x << 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
