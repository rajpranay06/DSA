'''

Given a matrix, your task is to rotate the matrix 90 degrees clockwise.

Input: [[1,2,3],[4,5,6],[7,8,9]]

Output: [[7,4,1],[8,5,2],[9,6,3]]

Intuition: By observation, we see that the first column of the original matrix is the reverse of the first row of the rotated matrix, so that’s why we transpose the matrix and then reverse each row, and since we are making changes in the matrix itself space complexity gets reduced to O(1).

Approach:

Step 1: Transpose the matrix. (transposing means changing columns to rows and rows to columns)

Step 2: Reverse each row of the matrix.

'''

class Solution:
    def rotate(self, a: List[List[int]]) -> None:
        # Tranpose the matrix
        for i in range(len(a)):
            for j in range(i):
                a[i][j], a[j][i] = a[j][i], a[i][j]

        # Reverse every row
        for i in a:
            i.reverse()

'''
Time Complexity: O(N*N) + O(N*N).One O(N*N) is for transposing the matrix and the other is for reversing the matrix.

Space Complexity: O(1)

'''
        
