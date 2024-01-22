'''
Input Format: N = 4, M = 69
Result: -1
Explanation: The 4th root of 69 does not exist. So, the answer is -1.

func(n, m, mid):

  We will first declare a variable ‘ans’ to store the value midn.
  Now, we will run a loop for n times to multiply the ‘mid’ n times with ‘ans’. 
  Inside the loop, if at any point ‘ans’ becomes greater than m, we will return 2.
  Once the loop is completed, if the ‘ans’ is equal to m, we will return 1.
  If the value is smaller, we will return 0.

'''

def func(mid, n, m):
    ans = 1
    for i in range(1, n + 1):
        ans *= mid
        if ans > m:
            return 2
    if ans == m:
        return 1
    return 0

def NthRoot(n: int, m: int) -> int:
    low = 1
    high = m
    while low <= high:
        mid = (low + high) // 2
        midN = func(mid, n, m)
        if midN == 1:
            return mid
        elif midN == 0:
            low = mid + 1
        else:
            high = mid - 1
    return -1


'''

Time Complexity: O(logN), N = size of the given array.
Reason: We are basically using binary search to find the minimum.

Space Complexity: O(1)
Reason: We have not used any extra data structures, this makes space complexity, even in the worst case as O(1).

'''
