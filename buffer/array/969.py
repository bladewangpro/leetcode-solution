"""Pancake Sorting
"""


def pancakeSort(arr):
    '''Dynamic Programming: cut the big problem to small problems
    -------------------------------------------------------------
    Each time, flip the largest value to the end of the array, then
    we can shorten the whole pancake problem of length n to pancake
    problem of length n - 1
    '''

    k = []

    for i in range(len(arr), 0, -1):
        k += [arr[:i+1].index(i) + 1, i]
        arr[:k[-2]] = arr[:k[-2]][::-1]
        arr[:k[-1]] = arr[:k[-1]][::-1]

    return k


if __name__ == '__main__':
    import numpy as np
    arr = np.arange(5)[1:]
    np.random.shuffle(arr)
    arr = arr.tolist()
    print(arr)
    print(pancakeSort(arr))