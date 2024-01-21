'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

'''

class Solution:
    def majorityElement(self, a: List[int]) -> int:
        count = 0
        ele = None

        for i in a:
            if count == 0:
                count += 1
                ele = i
              
            # If curr element == ele than increase the count
            elif i == ele:
                count += 1
            else:
                count -= 1
        
        return ele

'''

Time Complexity: O(N)

Space Complexity: O(1) as we are not using any extra space.

'''
