'''

Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
A subarray is a contiguous part of the array.

Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

Example 2:

Input: nums = [0,0,0,0,0], goal = 0
Output: 15

'''

class Solution:
    def numSubarraysWithSum(self, a: List[int], goal: int) -> int:
        preSum = {0:1}
        s = 0
        res = 0
        for i in a:
            s += i
            # Get if there exists a sum s - goal in hashmap 
            res += preSum.get(s - goal, 0)
            # Set the count of current sum
            preSum[s] = preSum.get(s, 0) + 1
        return res
