'''

Problem Statement: You have been given a 2-D array ‘mat’ of size ‘N x M’ where ‘N’ and ‘M’ denote the number of rows and columns, respectively. 
The elements of each row and each column are sorted in non-decreasing order.
But, the first element of a row is not necessarily greater than the last element of the previous row (if it exists).
You are given an integer ‘target’, and your task is to find if it exists in the given ‘mat’ or not.

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

We can enhance this method by adjusting how we move through the matrix. 
Let’s take a look at the four corners: (0, 0), (0, m-1), (n-1, 0), and (n-1, m-1). By observing these corners, we can identify variations in how we traverse the matrix.

For cell(0,0) - row and col are sorted in ascending order. So it is not possible tot ake this corner.
For cell(0,m-1) - row is sorted in descending order from back and col is ascending. We can choose this corner.
For cell(n-1,0) - row is sorted in ascending order and col is descending from bottom. We can also choose this.
For cell(n-1,m-1) - row and col are in descending order. Not possible.

Choose any of (0,m-1) and (n-1,0)

Using the above observations, we will start traversal from the cell (0, m-1) and every time we will compare the target with the element at the current cell. 
After comparing we will either eliminate the row or the column accordingly like the following:

If current element > target: We need the smaller elements to reach the target. But the column is in increasing order and so it contains only greater elements. 
So, we will eliminate the column by decreasing the current column value by 1(i.e. col–) and thus we will move row-wise.
If current element < target: In this case, We need the bigger elements to reach the target. But the row is in decreasing order and so it contains only smaller elements. 
So, we will eliminate the row by increasing the current row value by 1(i.e. row++) and thus we will move column-wise.

'''

class Solution:
    def searchMatrix(self, a: List[List[int]], k: int) -> bool:
        m,n = len(a), len(a[0])
        row = 0
        col = n - 1
        while row < m and col >= 0:
            if a[row][col] == k:
                return True
            if a[row][col] > k:
                col -= 1
            else:
                row += 1
        return False


'''

Time Complexity: O(N+M), where N = given row number, M = given column number.
Reason: We are starting traversal from (0, M-1), and at most, we can end up being in the cell (M-1, 0). So, the total distance can be at most (N+M). So, the time complexity is O(N+M).

Space Complexity: O(1) as we are not using any extra space.

'''
