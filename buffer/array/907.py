"""Sum of Subarray Minimums
"""


def sumSubarrayMins1(A):
    '''Brute Force
    --------------------
    works with Golang, won't work with Python
    Golang is more effective than Python
    '''

    res, mod = 0, 10 ** 9 + 7

    for i in range(len(A)):
        _min = A[i]
        for j in range(i, len(A)):
            if _min > A[j]:
                _min = A[j]
            res += _min
    
    return res % mod


class items(object):
    __slots__ = ['val', 'count']
    
    def __init__(self, val, count):
        self.val = val
        self.count = count

def sumSubarrayMins2(A):
    '''Two monotonic stacks
    ----------------------------
    For one item in this array, the left side has lefts possibilities,
    and the right side has rights possibilities. So for one item,
    there will be lefts * rights possibilities.
    ''' 
    res, mod, n = [0, 10 ** 9 + 7, len(A)]
    lefts, rights, leftStack, rightStack = [0] * n, [0] * n, [], []

    #from left to right monotonic stack
    for i in range(n):
        count = 1
        while len(leftStack) != 0 and leftStack[-1].val > A[i]:
            count += leftStack[-1].count
            leftStack.pop()
        leftStack.append(items(A[i], count))
        lefts[i] = count
    print(lefts)

    #from right to left monotonic stack
    for i in range(n - 1, -1, -1):
        count = 1
        while len(rightStack) != 0 and rightStack[-1].val >= A[i]:
            count += rightStack[-1].count
            rightStack.pop()
        rightStack.append(items(A[i], count))
        rights[i] = count
    print(rights)

    for i in range(n):
        res += (A[i] * lefts[i] * rights[i]) % mod
    
    return res % mod


def sumSubarrayMins3(A):
    '''Dynamic Programming and Monotonic Increasing Stack
    -----------------------------------------------------
    Dynamic Programming: cut a big problem into small problems
    dp: dp[i] is the result of a subarray which ends at i
    We need to find relationships within dp[i]s
    '''

    n = len(A)
    mod, stack, dp = (10 ** 9 + 7, [-1], [0] * (n + 1))

    for i in range(n):
        while stack[-1] != -1 and A[stack[-1]] > A[i]:
            stack.pop()
        dp[i + 1] = dp[stack[-1] + 1] + A[i] * (i - stack[-1])
        stack.append(i)
    
    return sum(dp) % mod


if __name__ == '__main__':
    A = [3, 1, 2, 4]
    # A = [11, 81, 94, 43, 3]
    print(sumSubarrayMins3(A))
