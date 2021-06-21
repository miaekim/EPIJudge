from test_framework import generic_test
from test_framework.test_failure import TestFailure
from collections import deque

class QueueWithMax:
    _max = float('-inf')
    _queue = deque([])
    def enqueue(self, x: int) -> None:
        if x > self._max:
            self._max = x
        self._queue.append(x)

    def dequeue(self) -> int:
        x = self._queue.popleft()
        if x == self._max:
            self._max = max(self._queue) if self._queue else float('-inf')
        return x

    def max(self) -> int:
        return self._max


def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_with_max.py',
                                       'queue_with_max.tsv', queue_tester))
