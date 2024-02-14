'''

Given an integer array nums of unique elements, return all possible 
subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Approach: Prerequisites: To check whether the ith bit is set or not.If n&(1<<i) != 0,then the ith bit is set.
First, write down all the numbers from 0 to 2^(n)-1 and their bit representation.0 means I am not picking the character in my subsequence, and 1 means I am picking the character.

Basically, we traverse from 0 to 2^(n)-1 and check for every number if their bit is set or not. If the bit is set add that character to your subsequence.


Time Complexity: O(2^n * n)
Reason: O(2^n) for the outer for loop and O(n) for the inner for loop.

Space Complexity: O(1)

'''


class Solution:
    
    def subsets(self, a: List[int]) -> List[List[int]]:
        
        res = [[]]
        n = len(a)

        for num in range(1, 1<<n):
            k = []
            for i in range(0, n):
                if num & (1<<i):
                    k.append(a[i])
            if k:
                res.append(k[:])
        
        res.sort()
        return res
            


