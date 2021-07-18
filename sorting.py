from typing import List
from typing import Callable
def bubble(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(0, n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def selection(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(0, n - 1):
        min_idx = arr.index(min(arr[i+1:]))
        if arr[i] > arr[min_idx]:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# assumping they keys between a specific range.
def counting(arr: List[int], upper_limit: int = 10) -> List[int]:
    n = len(arr) # upper_limit
    cnt = [0] * upper_limit
    for num in arr:
        cnt[num] += 1

    a_i, c_i = 0, 0
    while a_i < n:
        if cnt[c_i] > 0:
            arr[a_i] = c_i
            cnt[c_i] -= 1
            a_i += 1 
        else:
            c_i += 1
        
    return arr

def merge(arr: List[int]) -> List[int]:
    pass

def test(fs: List[Callable]):
    test_arrs = [
        [1, 4, 1, 2, 7, 5, 2],
        [9,8,7,2,1,3,4,9]
    ]
    for test_arr in test_arrs:
        print("-", test_arr)
        for f in fs:
            print(f.__name__, '\t', f(test_arr))
    
if __name__ == '__main__':
    fs = [sorted, bubble, selection, insertion, counting]
    test(fs)