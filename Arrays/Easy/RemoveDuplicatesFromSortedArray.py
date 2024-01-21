'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

Example 1: 

Input: arr[1,1,2,2,2,3,3]

Output: arr[1,2,3,_,_,_,_]

Explanation: Total number of unique elements are 3, i.e[1,2,3] and Therefore return 3 after assigning [1,2,3] in the beginning of the array.

Two pointers
Intuition: We can think of using two pointers ‘i’ and ‘j’, we move ‘j’ till we don’t get a number arr[j] which is different from arr[i]. As we got a unique number we will increase the i pointer and update its value by arr[j]. 
'''
class Solution:
    def removeDuplicates(self, a: List[int]) -> int:
        n = len(a)
        i = 0
        for j in range(1,n):
            if a[i] != a[j]:
                i += 1
                a[i] = a[j]
        return i+1

'''
Time Complexity: O(N)

Space Complexity: O(1)
'''
