'''

Given an array of length N. Peak element is defined as the element greater than both of its neighbors. Formally, if ‘arr[i]’ is the peak element, ‘arr[i – 1]’ < ‘arr[i]’ and ‘arr[i + 1]’ < ‘arr[i]’. 
Find the index(0-based) of a peak element in the array. If there are multiple peak numbers, return the index of any peak number.

Input Format: arr[] = {1,2,3,4,5,6,7,8,5,1}
Result: 7
Explanation: In this example, there is only 1 peak that is at index 7.

The left half of the peak element has an increasing order. This means for every index i, arr[i-1] < arr[i].
On the contrary, the right half of the peak element has a decreasing order. This means for every index i, arr[i+1] < arr[i].
Now, using the above observation, we can easily identify the left and right halves, just by checking the property of the current index, i, like the following:

If arr[i] > arr[i-1]: we are in the left half.
If arr[i] > arr[i+1]: we are in the right half.

'''

class Solution:
    def findPeakElement(self, a: List[int]) -> int:
        n = len(a)
        if n == 1 or a[0] > a[1]:
            return 0
        if a[n-1] > a[n-2]:
            return n-1
        low, high = 1, n-2
      
        while low <= high:
            mid = (low+high)//2

            # If arr[mid] is the peak:
            if a[mid] > a[mid-1] and a[mid] > a[mid+1]:
                return mid

            # If we are in the left:
            elif a[mid] > a[mid-1]:
                low = mid+1

            # If we are in the right:
            # Or, arr[mid] is a common point:
            else:
                high = mid-1
              
        return -1

'''

Time Complexity: O(logN), N = size of the given array.
Reason: We are basically using binary search to find the minimum.

Space Complexity: O(1)
Reason: We have not used any extra data structures, this makes space complexity, even in the worst case as O(1).

'''
