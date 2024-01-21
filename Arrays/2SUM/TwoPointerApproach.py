'''
1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.

2nd variant: Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return {-1, -1}.

Note: You are not allowed to use the same element twice. Example: If the target is equal to 6 and num[1] = 3, then nums[1] + nums[1] = target is not a solution.

'''

# Variant 1
class Solution:
    def twoSum(self, a: List[int], k: int) -> bool:
        a.sort()
        n = len(a)
        i = 0
        j = n-1
        while i <= j:
            if a[i] + a[j] == k:
                return True
            if a[i] + a[j] > k:
                j -= 1
            else:
                i += 1
        return False

# Variant 2
'''
For variant 2, we can store the elements of the array along with its index in a new array. Then the rest of the code will be similar. 
And while returning, we need to return the stored indices instead of returning “YES”. 
But for this variant, the recommended approach is approach 2 i.e. hashing approach.

Time Complexity: O(N) + O(N*logN), where N = size of the array.
Reason: The loop will run at most N times. And sorting the array will take N*logN time complexity.

Space Complexity: O(1) as we are not using any extra space.
'''
