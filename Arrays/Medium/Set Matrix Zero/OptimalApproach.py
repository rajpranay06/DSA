'''

Intuition:
In the previous approach, the time complexity is minimal as the traversal of a matrix takes at least O(N*M)(where N = row and M = column). In this approach, we can just improve the space complexity. 
So, instead of using two extra matrices row and col, we will use the 1st row and 1st column of the given matrix to keep a track of the cells that need to be marked with 0. 
But here comes a problem. If we try to use the 1st row and 1st column to serve the purpose, the cell matrix[0][0] is taken twice. 
To solve this problem we will take an extra variable col0 initialized with 1. Now the entire 1st row of the matrix will serve the purpose of the row array. 
And the 1st column from (0,1) to (0,m-1) with the col0 variable will serve the purpose of the col array.

'''

class Solution:
    def setZeroes(self, a: List[List[int]]) -> None:
        col0 = 1
        m = len(a)
        n = len(a[0])
        # step 1: Traverse the matrix and
        # mark 1st row & col accordingly:
        for i in range(m):
            for j in range(n):
                if a[i][j] == 0:
                    # mark i-th row
                    a[i][0] = 0
                    # mark j-th column:
                    if j != 0:
                        a[0][j] = 0
                    else:
                        col0 = 0
                      
        # Step 2: Mark with 0 from (1,1) to (n-1, m-1):
        for i in range(1,m):
            for j in range(1,n):
                if a[i][j] != 0:
                    # check for col & row:
                    if a[i][0] == 0 or a[0][j] == 0:
                        a[i][j] = 0
                      
        #step 3: Finally mark the 1st col & then 1st row:
        if a[0][0] == 0:
            for j in range(n):
                a[0][j] = 0
        if col0 == 0:
            for i in range(m):
                a[i][0] = 0
        return a

'''

Time Complexity: O(2*(N*M)), where N = no. of rows in the matrix and M = no. of columns in the matrix.
Reason: In this approach, we are also traversing the entire matrix 2 times and each traversal is taking O(N*M) time complexity.

Space Complexity: O(1) as we are not using any extra space.

'''

