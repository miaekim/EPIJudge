from typing import List

from test_framework import generic_test
"""
```
["foo", "bar", "widget", "foo", "widget", "widget", "adnan"]	1	TODO
["foo", "bar", "widget", "foo", "xyz", "widget", "bar", "adnan"]	3	TODO
["foo", "bar", "widget", "adnan"]	-1	TODO
[]	-1	TODO
["foo", "foo", "foo"]	1	TODO
`"""
from collections import defaultdict
def find_nearest_repetition(paragraph: List[str]) -> int:
    _dic = {}

    for idx, word in enumerate(paragraph):
        if word in _dic:
            _dic[word].append(idx)
        else:
            _dic[word] = [idx]

    _nearest = float('inf')
    for word, idxes in _dic.items():
        idxes_len = len(idxes)
        if idxes_len <= 1:
            continue
        for i in range(idxes_len - 1):
            idxes[i] = idxes[i + 1] - idxes[i]
        idxes.pop()
        _nearest_candidate = min(idxes)
        if _nearest_candidate < _nearest:
            _nearest = _nearest_candidate

    if _nearest == float('inf'):
        return -1
    else:
        return _nearest


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
