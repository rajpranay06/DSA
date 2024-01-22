'''

Given an array of integers and an integer k, return the total number of subarrays whose sum equals k.

A subarray is a contiguous non-empty sequence of elements within an array.

Approach:

The steps are as follows:

First, we will declare a map to store the prefix sums and their counts.
Then, we will set the value of 0 as 1 on the map.
Then we will run a loop(say i) from index 0 to n-1(n = size of the array).
For each index i, we will do the following:
We will add the current element i.e. arr[i] to the prefix sum.
We will calculate the prefix sum i.e. x-k, for which we need the occurrence.
We will add the occurrence of the prefix sum x-k i.e. mpp[x-k] to our answer.
Then we will store the current prefix sum in the map increasing its occurrence by 1.

'''

class Solution:
    def subarraySum(self, a: List[int], k: int) -> int:
        n = len(a)
        d = defaultdict(int)
        preSum = 0
        c = 0
        d[0] = 1  # Setting 0 in the map.

        for i in range(n):

            # add current element to prefix Sum:
            preSum += a[i]

            # Calculate x-k:
            x = preSum - k

            # Add the number of subarrays to be removed:
            c += d[x]

            # Update the count of prefix sum in the map.
            d[preSum] += 1
        
        return c


'''

Time Complexity: O(N) or O(N*logN) depending on which map data structure we are using, where N = size of the array.

Space Complexity: O(N) as we are using a map data structure.

'''
