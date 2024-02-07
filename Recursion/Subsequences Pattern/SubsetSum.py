'''

Problem statement
You are given an array 'A' of 'N' integers. You have to return true if there exists a subset of elements of 'A' that sums up to 'K'. Otherwise, return false.


For Example
'N' = 3, 'K' = 5, 'A' = [1, 2, 3].
Subset [2, 3] has sum equal to 'K'.
So our answer is True.

'''

from typing import *

def helper(a,i,s,k):
    if s == k:
        return True
    
    if s > k or i >= len(a):
        return False
    
    # Take
    if helper(a, i+1, s + a[i], k):
        return True

    # Not Take
    if helper(a, i+1, s, k):
        return True

    return False

def isSubsetPresent(n:int, k: int, a: List[int]) -> bool:
    # Write your code here.

    return helper(a, 0, 0, k)
    
