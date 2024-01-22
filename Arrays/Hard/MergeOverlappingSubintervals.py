'''

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Intuition:

We will start traversing the given array with a single loop. At the first index, as our answer list is empty, we will insert the first element into the answer list. 
While traversing afterward we can find two different cases:

Case 1: If the current interval can be merged with the last inserted interval of the answer list:
In this case, we will update the end of the last inserted interval with the maximum(current interval’s end, last inserted interval’s end) and continue moving afterward. 

Case 2: If the current interval cannot be merged with the last inserted interval of the answer list:
In this case, we will insert the current interval in the answer array as it is. And after this insertion, the last inserted interval of the answer list will obviously be updated to the current interval.

'''

class Solution:
    def merge(self, a: List[List[int]]) -> List[List[int]]:
        a.sort()
        res = []
        for i in range(len(a)):
            
            # if the current interval does not
            # lie in the last interval:
            if not res or a[i][0] > res[-1][1]:
                res.append(a[i])

            # if the current interval
            # lies in the last interval:
            else:
                res[-1][1] = max(res[-1][1], a[i][1])
        return res


'''

Time Complexity: O(N*logN) + O(N), where N = the size of the given array.
Reason: Sorting the given array takes  O(N*logN) time complexity. Now, after that, we are just using a single loop that runs for N times. So, the time complexity will be O(N).

Space Complexity: O(N), as we are using an answer list to store the merged intervals. Except for the answer array, we are not using any extra space.

'''
