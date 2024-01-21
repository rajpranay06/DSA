'''
Example 1:
Input: N = 7, array[] = {1,2,3,4,5,6,7} , k=2 , right
Output: 6 7 1 2 3 4 5
Explanation: array is rotated to right by 2 position .

Example 2:
Input: N = 6, array[] = {3,7,8,9,10,11} , k=3 , left 
Output: 9 10 11 3 7 8
Explanation: Array is rotated to right by 3 position.

Using ” Reversal Algorithm “

Approach:

For Rotating Elements to right
Step 1: Reverse the last k elements of the array

Step 2: Reverse the first n-k elements of the array.

Step 3: Reverse the whole array.

For Rotating Elements to left
Step 1: Reverse the first k elements of the array

Step 2: Reverse the last n-k elements of the array.

Step 3: Reverse the whole array.

'''
#RotateArrayRight code
class Solution:
    def reverse(a,start,end):
        while start <= end:
            a[start], a[end] = a[end], a[start]
            start += 1
            end -= 1
    def rotate(self, a: List[int], k: int) -> None:
        n = len(a)
        k %= n
        Solution.reverse(a,0,n-k-1)
        Solution.reverse(a,n-k,n-1)    
        Solution.reverse(a,0,n-1)
        return a
'''
Time Complexity – O(N) where N is the number of elements in an array

Space Complexity – O(1) since no extra space is required
'''
