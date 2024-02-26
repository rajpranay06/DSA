'''

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

'''

class Solution:
    def longestOnes(self, a: List[int], k: int) -> int:
        
        c = 0
        maxL = 0
        j = 0
        n = len(a)

        for i in range(n):

            # Incrementing the count
            if a[i] == 0:
                c += 1
            
            # Removing indices till count == k
            while c > k: 
                if a[j] == 0:
                    c -= 1
                j += 1
            
            maxL = max(maxL, i-j+1)

        return maxL
