'''

Given an integer array nums and an integer k, return the number of good subarrays of nums.
A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.


Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

Approach

To find subarrays with exactly k distinct integers, we can solve the problem of finding subarrays with less than or equal to k distinct integers first. 
Then, we subtract the result of count of subarrays with less than or equal to (k-1) distinct integers from the count of subarrays with less than or equal to (k) distinct integers to get the final solution.

Time Complexity - O(N), where ‘N’ is the size of array ‘ARR’.
We can insert values into the hash map in ‘O(1)’. For inserting ‘N’ values, the time taken will be ‘O(N)’. In the outer loop, we traverse the array once in ‘O(N)’ time, i.e., from ‘R = [0, N-1]’. The inner loop also runs for ‘O(N)’ iterations effectively, i.e, from ‘L = [0, N-1]’. Thus, the time complexity will be ‘O(N)’.

Space Complexity - O(N), where ‘N’ is the size of array ‘ARR’.
The hash map will store at most ‘N’ values (when all the values in ‘ARR’ are distinct). Thus, the space complexity is ‘O(N)’.

'''

class Solution:
    def subArrayWithAtMostKDistinctElements(self, k, a):
        res = 0
        left = 0
        hashSet = {}
        n = len(a)
        for right in range(n):
            
            # Add the right most element of the array in the  map
            hashSet[a[right]] = hashSet.get(a[right], 0) + 1
            while left < right and len(hashSet) > k:
                # If the set has move than k unique characters then start decreasing the window from left
                hashSet[a[left]] -= 1
                
                # Remove the element from the map if it becomes 0
                if hashSet[a[left]] == 0:
                    del hashSet[a[left]]
                left += 1
            res += right - left + 1
        return res

    def subarraysWithKDistinct(self, a: List[int], k: int) -> int:
        # We can get exact K elements subarray by subtracting atmost k-1 from atmost k subarrays
        if k == 1:
            return self.subArrayWithAtMostKDistinctElements(k, a)
        return self.subArrayWithAtMostKDistinctElements(k, a) - self.subArrayWithAtMostKDistinctElements(k-1, a)
        
