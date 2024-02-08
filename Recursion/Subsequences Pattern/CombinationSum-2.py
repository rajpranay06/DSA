'''

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

'''


class Solution:
    
    def combinationSum2(self, a: List[int], k: int) -> List[List[int]]:
        
        a.sort()
        res = []
        store = []

        def helper(index, k):

            if k == 0:
                res.append(store[:])
                return
            
            for i in range(index, len(a)):
                if i > index and a[i] == a[i-1]:
                    continue
                if a[i] > k:
                    break
                store.append(a[i])
                helper(i + 1, k - a[i])
                store.pop() 
        
        helper(0, k)
        return res


'''

Time Complexity:O(2^n*k)

Reason: Assume if all the elements in the array are unique then the no. of subsequence you will get will be O(2^n). we also add the ds to our ans when we reach the base case that will take “k”//average space for the ds.

Space Complexity:O(k*x)

Reason: if we have x combinations then space will be x*k where k is the average length of the combination.

'''
