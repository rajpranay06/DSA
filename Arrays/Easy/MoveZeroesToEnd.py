'''
Problem Statement: You are given an array of integers, your task is to move all the zeros in the array to the end of the array and move non-negative integers to the front by maintaining their order.

Example 1:
Input: 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1
Output: 1 ,2 ,3 ,4 ,1 ,0 ,0 ,0
Explanation: All the zeros are moved to the end and non-negative integers are moved to front by maintaining order

Algorithm:
  Similar to removing duplicates,
  1. First, using a loop, we will place the pointer j. If we don’t find any 0, we will not perform the following steps.
  2. After that, we will point i to index j+1 and start moving the pointer using a loop.
  3. While moving the pointer i, we will do the following:
    If a[i] != 0 i.e. a[i] is a non-zero element: We will swap a[i] and a[j]. Now, the current j is pointing to the non-zero element a[i]. So, we will shift the pointer j by 1 so that it can again point to the first zero.
  4. Finally, our array will be set in the right manner.

'''

class Solution:
    def moveZeroes(self, a: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = -1
        n = len(a)
        for i in range(n):
            if a[i] == 0:
                j = i
                break
        if j != -1:
            for i in range(j+1,n):
                if a[i] != 0:
                    a[i],a[j] = a[j],a[i]
                    j += 1

'''

Time Complexity: O(N), N = size of the array.
Reason: We have used 2 loops and using those loops, we are basically traversing the array once.

Space Complexity: O(1) as we are not using any extra space to solve this problem.

'''

