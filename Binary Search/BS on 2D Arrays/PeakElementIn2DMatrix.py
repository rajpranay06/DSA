'''

A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.

Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].

You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.

Input: mat = [[10,20,15],[21,30,14],[7,16,32]]
Output: [1,1]
Explanation: Both 30 and 32 are peak elements so [1,1] and [2,2] are both acceptable answers.

	Use similar approach as Peak Element in 1D Array. Traverse row or col wise. Ex – col wise   low = 0 high = m-1, find mid and get max element from mid col. 
Check if max element is peak by comparing to its adjacent elements. 
If peak return the max element. If previous element > max then eliminate right half else eliminate left half. 

'''

class Solution:
    def findPeakGrid(self, a: List[List[int]]) -> List[int]:
            n = len(a)
            m = len(a[0])
            low = 0
            high = m-1
            
            while low <= high:
                mid = (low+high)//2
                maxEl = -1
                maxIndex = -1

                # Finding amx element of col
                for i in range(n):
                    if a[i][mid] > maxEl:
                        maxEl = a[i][mid]
                        maxIndex = i
                left, right = -1, -1

                # Edge cases
                if mid - 1 >= 0:
                    left = a[maxIndex][mid-1]
                if mid + 1 < m:
                    right = a[maxIndex][mid+1]
                # Peak element condition
                if maxEl > left and maxEl > right:
                    return [maxIndex,mid]
                if maxEl < left:
                    high = mid - 1
                else:
                    low = mid + 1
            return [-1,-1]
                

'''

Time Complexity - O(logM * N). BS on col so logM and N for checking max in the col.
Space Complexity - O(1)

'''
        
