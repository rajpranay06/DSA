'''

Given an integer array nums that may contain duplicates, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.


Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

'''

class Solution:
    def subsetsWithDup(self, a: List[int]) -> List[List[int]]:
        
        a.sort()
        res = []

        def helper(index, ds):
            
            res.append(ds[:])
            for i in range(index, len(a)):
                # Not considering duplicates
                if i > index and a[i] == a[i-1]:
                    continue
                
                # Take
                ds.append(a[i])
                helper(i+1, ds)

                # Not take
                ds.pop()
            
        helper(0, [])
        return res


'''

Time Complexity: O(2^n) for generating every subset and O(k)  to insert every subset in another data structure if the average length of every subset is k. Overall O(k * 2^n).

Space Complexity: O(2^n * k) to store every subset of average length k. Auxiliary space is O(n)  if n is the depth of the recursion tree.

'''
