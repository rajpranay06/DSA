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

'''

class Solution:
    
    def helper(a, index, store, res):
        if index == len(a):
            res.append(store.copy())
            return
        
        store.append(a[index])
        Solution.helper(a, index + 1, store, res)

        store.pop()
        Solution.helper(a, index + 1, store, res)

        
    def subsets(self, a: List[int]) -> List[List[int]]:
        
        store = []
        res = []

        if a:
            Solution.helper(a, 0, store, res)
        
        return res


'''

Time Complexity: O(2^n)

Space Complexity: O(n), recursion stack.

'''
