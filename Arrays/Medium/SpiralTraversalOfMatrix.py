'''

Input: Matrix[][] = { { 1, 2, 3, 4 },
		      { 5, 6, 7, 8 },
		      { 9, 10, 11, 12 },
	              { 13, 14, 15, 16 } }

Outhput: 1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10.

In this approach, we will be using four loops to print all four sides of the matrix.

1st loop: This will print the elements from left to right.

2nd loop: This will print the elements from top to bottom.

3rd loop: This will print the elements from right to left.

4th loop: This will print the elements from bottom to top.

Steps:

Create and initialize variables top as starting row index, bottom as ending row index left as starting column index, and right as ending column index. As shown in the image given below.
In each outer loop traversal print the elements of a square in a clockwise manner.
Print the top row, i.e. Print the elements of the top row from column index left to right and increase the count of the top so that it will move to the next row.
Print the right column, i.e. Print the rightmost column from row index top to bottom and decrease the count of right.
Print the bottom row, i.e. if top <= bottom, then print the elements of a bottom row from column right to left and decrease the count of bottom
Print the left column, i.e. if left <= right, then print the elements of the left column from the bottom row to the top row and increase the count of left.
Run a loop until all the squares of loops are printed.

'''

class Solution:
    def spiralOrder(self, a: List[List[int]]) -> List[int]:
        # Define ans array to store the result.
        res = []
        m, n = len(a), len(a[0])
        
        # Initialize the pointers read for traversal.
        top, left = 0, 0
        right, bottom = n-1, m-1

        # Loop until all elements are not traversed.
        while left <= right and top <= bottom:

            # For moving left to right
            for i in range(left,right+1):
                res.append(a[top][i])
            top += 1

            # For moving top to bottom.
            for i in range(top,bottom+1):
                res.append(a[i][right])
            right -= 1

            # For moving right to left.
            if top <= bottom:
                for i in range(right, left-1,-1):
                    res.append(a[bottom][i])
                bottom -= 1

            # For moving bottom to top.
            if left <= right:
                for i in range(bottom, top-1,-1):
                    res.append(a[i][left])
                left += 1
        
        return res

'''

Time Complexity: O(m x n) { Since all the elements are being traversed once and there are total n x m elements ( m elements in each row and total n rows) so the time complexity will be O(n x m)}.

Space Complexity: O(n) { Extra Space used for storing traversal in the ans array }.

'''

