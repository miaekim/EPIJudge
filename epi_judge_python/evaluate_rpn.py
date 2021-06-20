from test_framework import generic_test


def evaluate(expression: str) -> int:
    expressions = expression.split(",")
    buffer = []
    for e in expressions:
        if e in "+-*/":
            num2, num1 = buffer.pop(), buffer.pop()
            if e == "+":
                buffer.append(num1+num2)
            elif e == "-":
                buffer.append(num1-num2)
            elif e == "*":
                buffer.append(num1*num2)
            elif e == "/":
                buffer.append(num1//num2)
        else:
            buffer.append(int(e))

    return buffer[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
