'''

Given an array that contains both negative and positive integers, find the maximum product subarray.
 
Input:
 Nums = [1,2,-3,0,-4,-5]
Output:
 20
Explanation:
 In the given array, we can see (-4)×(-5) gives maximum product value.

 We will optimize the solution through some observations.

Observations:

If the given array only contains positive numbers: If this is the case, we can confidently say that the maximum product subarray will be the entire array itself.
If the given also array contains an even number of negative numbers: As we know, an even number of negative numbers always results in a positive number. 
So, also, in this case, the answer will be the entire array itself.
If the given array also contains an odd number of negative numbers: Now, an odd number of negative numbers when multiplied result in a negative number. 
Removal of 1 negative number out of the odd number of negative numbers will leave us with an even number of negatives. Hence the idea is to remove 1 negative number from the result. 
Now we need to decide which 1 negative number to remove such that the remaining subarray yields the maximum product.

'''

class Solution:
    def maxProduct(self, a: List[int]) -> int:
        res = float("-inf")
        n = len(a)
        pref, suff = 1,1
        for i in range(n):
            if pref == 0:
                pref = 1
            if suff == 0:
                suff = 1
            pref *= a[i]
            suff *= a[n - i - 1]
            res = max(res, max(suff, pref))
        return res

'''

Time Complexity: O(N), N = size of the given array.
Reason: We are using a single loop that runs for N times.

Space Complexity: O(1) as No extra data structures are used for computation.

'''

 
