'''

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. 
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.


Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

'''

class Solution:
    def merge(self, a):

        #Merging overlapping sub-intervals
        res = []
        for i in range(len(a)):
            if not res or a[i][0] > res[-1][1]:
                res.append(a[i])
            else:
                res[-1][1] = max(res[-1][1], a[i][1])
        return res

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        k = newInterval[0]

        low = 0
        high = len(intervals) - 1
        pos = -1

        # Finding the lower bound of the newInterval start using Binary search
        while low <= high:
            mid = (low + high)//2
            if intervals[mid][0] >= k:
                pos = mid
                high = mid - 1
            else:
                low = mid + 1
        
        # Adding newInnterval at its right position
        if pos == -1:
            intervals.append(newInterval)
        else:
            intervals = intervals[:pos] + [newInterval] + intervals[pos:]
        
        return self.merge(intervals)
