"""Combination Sum III
-----------------------
Constraints:
    * 2 <= k <= 9
    * 1 <= n <= 60
"""


def combinationSum3(k, n):
    '''Recursive Method
    ----------------------------------------------
    c: one combination within all the combinations
    res: one place to hold all the combinations
    stop condition: when target == 0 and len(c) == k
    '''
    if k == 0:
        return []
    c, res = [], []
    findCombinationSum3(k, n, 1, c, res)
    return res


def findCombinationSum3(k, target, index, c, res):
    if target == 0:
        if len(c) == k:
            b = c.copy()
            res.append(b)
        return
    
    for i in range(index, 10):
        if target >= i:
            c.append(i)
            findCombinationSum3(k, target-i, i+1, c, res)
            c.pop()


if __name__ == "__main__":
    k, n = (3, 9)
    print(combinationSum3(k, n))