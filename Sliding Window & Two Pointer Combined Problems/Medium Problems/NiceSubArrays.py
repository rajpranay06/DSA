'''

Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
Return the number of nice sub-arrays.

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.

Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16

Intuition
Using Sliding window for getting the subarray that is valid and checking if shrinking the window from the left will make the subarray still valid or not and also for expanding from the right will make another valid subarray

Approach
Have current_count for counting odds in the current iteration
Have count for counting the total valid subarrays
Have Sliding window with the size of one and increment the current_count by 1 when you are at odd number and start your count from zero
If current_count equals k and check if the number at the left pointer is even if so increment count by one and increment shrink the window.
If current_count equals k and check if the number at the left pointer is odd if so increment count by one and increment shrink the window and decrement current_count by one.
Repeat the steps for the whole array.

Complexity
Time complexity: O(n)
Space complexity: O(1)

'''

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        oddCount = 0
        validSubArrays = 0
        left = 0
        n = len(nums)
        for right in nums:
            # Count the odd elements
            if right%2 != 0:
                oddCount += 1
                validSubArrays = 0
            if oddCount == k:
                # Count the valid subarrays 
                while left <= n and nums[left]%2 == 0:
                    validSubArrays += 1
                    left += 1
                # If odd it gives one valid sub array
                validSubArrays += 1
                oddCount -= 1
                left += 1
            res += validSubArrays
        return res


'''

Convert given array into binary array with even as 0 odd as 1. And use Binary SubArrays with given sum k approach

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

    def numberOfSubarrays(self, a: List[int], k: int) -> int:
        # Convert given array with a binary array with even as 0 odd as 1 
        for i in range(len(a)):
            if a[i]%2 == 0:
                a[i] = 0
            else:
                a[i] = 1
        return self.numSubarraysWithSum(a, k)
