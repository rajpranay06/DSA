'''

Given an array of N integers. Every number in the array except one appears twice. Find the single number in the array.

Input Format: arr[] = {1,1,2,2,3,3,4,5,5,6,6}
Result: 4
Explanation: Only the number 4 appears once in the array.

We need to consider 2 different cases while using Binary Search in this problem. Binary Search works by reducing the search space by half. 
So, at first, we need to identify the halves and then eliminate them accordingly. In addition to that, we need to check if the current element i.e. arr[mid] is the ‘single element’.

If arr[mid] != arr[mid-1] and arr[mid] != arr[mid+1]: If this condition is true for arr[mid], we can conclude arr[mid] is the single element.

The above condition will throw errors in the following 3 cases:

  If the array size is 1.
  If ‘mid’ points to 0 i.e. the first index.
  If ‘mid’ points to n-1 i.e. the last index.

The index sequence of the duplicate numbers in the left half is always (even, odd). That means one of the following conditions will be satisfied if we are in the left half:
If the current index is even, the element at the next odd index will be the same as the current element.
Similarly, If the current index is odd, the element at the preceding even index will be the same as the current element.

The index sequence of the duplicate numbers in the right half is always (odd, even). That means one of the following conditions will be satisfied if we are in the right half:
If the current index is even, the element at the preceding odd index will be the same as the current element.
Similarly, If the current index is odd, the element at the next even index will be the same as the current element.

'''

class Solution:
    def singleNonDuplicate(self, a: List[int]) -> int:
        n = len(a)

        # Edge cases:
        if n == 1:
            return a[0]
        if a[0] != a[1]:
            return a[0]
        if a[n-1] != a[n-2]:
            return a[n-1]
        
        low, high = 1, n-2
        while low <= high:
            mid = (low+high)//2

            # If arr[mid] is the single element:
            if a[mid] != a[mid-1] and a[mid] != a[mid+1]:
                return a[mid]

            # We are in the left:
            if (mid%2 == 0 and a[mid] == a[mid+1]) or (mid%2 == 1 and a[mid] == a[mid-1]):
                # Eliminate the left half:
                low = mid + 1
            # We are in the right:
            else:
                # Eliminate the right half:
                high = mid - 1 
              
        return -1

'''

Time Complexity: O(logN), N = size of the given array.
Reason: We are basically using the Binary Search algorithm.

Space Complexity: O(1) as we are not using any extra space.

'''
