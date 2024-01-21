'''
1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.

2nd variant: Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return {-1, -1}.

Note: You are not allowed to use the same element twice. Example: If the target is equal to 6 and num[1] = 3, then nums[1] + nums[1] = target is not a solution.

'''

# Variant 1

class Solution:
    def twoSum(self, a: List[int], k: int) -> List[int]:
        d = dict()
        s = 0
        for i in range(len(a)):
            
            f = k - a[i]
            if f in d:
                return True

            d[a[i]] = i
        

# Variant 2

class Solution:
    def twoSum(self, a: List[int], k: int) -> List[int]:
        d = dict()
        s = 0
        for i in range(len(a)):
            
            f = k - a[i]
            if f in d:
                # Returning the 2 indices 
                return [i,d[f]]
                
            d[a[i]] = i
        

'''

Time Complexity: O(N), where N = size of the array.
Reason: The loop runs N times in the worst case and searching in a hashmap takes O(1) generally. So the time complexity is O(N).

Space Complexity: O(N) as we use the map data structure.

'''
