from test_framework import generic_test

from typing import List
def look_and_say(n: int) -> str:
    
    def say(prev: List[str]):
        n = len(prev)
        count = 1
        counting = prev[0]
        write_idx = 0
        for num_str in prev[1:]:
            if num_str == counting:
                count += 1
            else:
                if write_idx < n:
                    prev[write_idx] = str(count)
                else:
                    prev.append(str(count))

                if write_idx + 1 < n:
                    prev[write_idx + 1] = counting
                else:
                    prev.append(counting)
                count = 1
                counting = num_str
                write_idx += 2
        
        if write_idx < n:
            prev[write_idx] = str(count)
        else:
            prev.append(str(count))

        if write_idx + 1 < n:
            prev[write_idx + 1] = counting
        else:
            prev.append(counting)

    prev = ['1']
    for x in range(n - 1):
        say(prev)
    return "".join(prev)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
