class Solution:
    def sortColors(self, a: List[int]) -> None:
        low = 0
        high = len(a) - 1
        mid = 0

        while mid <= high:

            # Swap low and mid if mid == 0
            if a[mid] == 0:
                a[low], a[mid] = a[mid], a[low]
                mid += 1
                low += 1

            # Increase mid if mid == 1
            elif a[mid] == 1:
                mid += 1

            # Swap mid and high if  mid == 2
            else:
                a[mid], a[high] = a[high], a[mid]
                high -= 1

'''

Time Complexity: O(N), where N = size of the given array.
Reason: We are using a single loop that can run at most N times.

Space Complexity: O(1) as we are not using any extra space.

'''
        
        
