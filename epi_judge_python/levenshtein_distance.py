from test_framework import generic_test


def levenshtein_distance(A: str, B: str) -> int:
    # distance = 
    # if A[-1] == B[-1]: levenshtein_distance(A[:-1], B[:-1]) + 1
    # else: 
    #     min(levenshtein_distance(A[:-1], B), levenshtein_distance(A[:-1], B))
    #    
    #    
    distance_map = {}
    def distance(a_idx: int, b_idx: int):
        nonlocal A
        nonlocal B
        if (a_idx, b_idx) in distance_map:
            return distance_map[(a_idx, b_idx)]

        if a_idx < 0:
            return b_idx + 1
        if b_idx < 0:
            return a_idx + 1

        if A[a_idx] == B[b_idx]:
            distance_map[(a_idx, b_idx)] = distance(a_idx - 1, b_idx - 1) 
        else:
            distance_map[(a_idx, b_idx)] = min(distance(a_idx - 1, b_idx - 1), distance(a_idx, b_idx - 1), distance(a_idx - 1, b_idx)) + 1

        return distance_map[(a_idx, b_idx)]

    return distance(len(A) - 1, len(B) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
