def longestSubarrayWithSumK(a: [int], k: int) -> int:
    # Write your code here
    i = 0
    j = 0
    n = len(a)
    maxLen = 0
    s = a[0]
    while j < n:
      
        # if sum > k, reduce the subarray from left
        # until sum becomes less or equal to k:
        while i <= j and s > k:
            s -= a[i]
            i += 1 
          
        # if sum = k, update the maxLen i.e. answer:
        if s == k:
            maxLen = max(maxLen, j-i+1)
          
        # Move forward the right pointer:
        j += 1
        if j < n:
            s += a[j]
        
    return maxLen

'''

Time Complexity: O(2*N), where N = size of the given array.
Reason: The outer while loop i.e. the right pointer can move up to index n-1(the last index). Now, the inner while loop i.e. the left pointer can move up to the right pointer at most. So, every time the inner loop does not run for n times rather it can run for n times in total. So, the time complexity will be O(2*N) instead of O(N2).

Space Complexity: O(1) as we are not using any extra space.

'''
