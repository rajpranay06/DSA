'''

Given an integer array arr of size N, sorted in ascending order (with distinct values) and a target value k. 
Now the array is rotated at some pivot point unknown to you. Find the index at which k is present and if k is not present return -1.

Input Format: arr = [4,5,6,7,0,1,2,3], k = 0
Result: 4
Explanation: Here, the target is 0. We can see that 0 is present in the given rotated sorted array, nums. Thus, we get output as 4, which is the index at which 0 is present in the array.

Though the array is rotated, we can clearly notice that for every index, one of the 2 halves will always be sorted. In the above example, the right half of the index mid is sorted.

So, to efficiently search for a target value using this observation, we will follow a simple two-step process. 

First, we identify the sorted half of the array. 
Once found, we determine if the target is located within this sorted half. 
If not, we eliminate that half from further consideration. 
Conversely, if the target does exist in the sorted half, we eliminate the other half.

'''

class Solution:
    def search(self, a: List[int], k: int) -> int:
        n = len(a)
        low, high = 0, n-1
        while low <= high:

            # if mid points the target
            mid = (low+high)//2
            if a[mid] == k:
                return mid

            # if left part is sorted
            elif a[mid] >= a[low]:
                if a[low] <= k and k <= a[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            # if right part is sorted
            else:
                if a[mid] <= k and k <= a[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1

'''

Time Complexity: O(logN), N = size of the given array.
Reason: We are using binary search to search the target.

Space Complexity: O(1)
Reason: We have not used any extra data structures, this makes space complexity, even in the worst case as O(1).

'''
