'''

Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example 1:

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6

Approach:

Convert every row to heights, and use largest area of histogram to find maximal rectangle. How to convert to heights, take an array with size of n(row size of matrix). 
Now traverse each row if row[i] is 1 add 1 to heights, else 0. Because if 0 we cannot use it to increase height.

Time Compelxity - O(N*(N+N)) 
Space Complexity - O(N) + O(N)

'''

class Solution:
    def largestRectangleArea(a: List[int]) -> int:
        n = len(a)
        st = []
        maxRes = 0

        for right in range(n+1):
            while st and (right == n or a[st[-1]] >= a[right]):
                # curr is the index of the current element
                # left is the index of prev min 
                # right is the index of next min
                curr = st.pop()
                left = -1 if not st else st[-1]
                maxRes = max( maxRes, a[curr] * (right - left -1))  # finding the area
            st.append(right)

        return maxRes
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix[0])

        heights = [0]*n
        maxRes = 0

        for row in matrix:
            # Converting every row into heights to find largest area of histogram
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            
            maxRes = max(maxRes, Solution.largestRectangleArea(heights))
        
        return maxRes
