'''

Problem statement
You are given an array 'nums' of ‘n’ integers.

Return all subset sums of 'nums' in a non-decreasing order.

Note:
Here subset sum means sum of all elements of a subset of 'nums'. A subset of 'nums' is an array formed by removing some (possibly zero or all) elements of 'nums'.

For example
Input: 'nums' = [1,2]

Output: 0 1 2 3

Explanation:
Following are the subset sums:
0 (by considering empty subset)
1 
2
1+2 = 3
So, subset sum are [0,1,2,3].

'''

from sys import *
from collections import *
from math import *

from typing import List

def helper(a, index, s, res):
    if index == len(a):
        res.append(s)
        return
        
    # Take
    helper(a, index + 1, s + a[index], res)

    # Not Take
    helper(a, index + 1, s, res)

        
def subsetSum(a: List[int]) -> List[int]:
        
    res = []
    if a:
        helper(a, 0, 0, res)
    
    return sorted(res)


'''

Time Complexity: O(2^n)+O(2^n log(2^n)). Each index has two ways. You can either pick it up or not pick it. So for n index time complexity for O(2^n) and for sorting it will take (2^n log(2^n)).

Space Complexity: O(2^n) for storing subset sums, since 2^n subsets can be generated for an array of size n.

'''
