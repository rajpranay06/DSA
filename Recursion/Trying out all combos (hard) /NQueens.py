'''

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Intuition: Using the concept of Backtracking, we will place Queen at different positions of the chessboard and find the right arrangement where all the n queens can be placed on the n*n grid.


Time Complexity: Exponential in nature since we are trying out all ways, to be precise it is O(N!).

Space Complexity: O(N^2)

'''


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []
        board = ['.'*n for _ in range(n)]
        
        # Hashing to check if Q can be placed or not
        leftRow = [0]*n
        upperDiagonal = [0]*(2*n - 1)
        lowerDiagonal = [0]*(2*n - 1)

        def helper(col):
            if col == n:
                res.append(board[:])
                return
            
            for row in range(n):
                if leftRow[row] == 0 and upperDiagonal[row+col] == 0 and lowerDiagonal[n-1 + col-row] == 0:
                    # Setting Q to visited 
                    leftRow[row] = 1
                    upperDiagonal[row+col] = 1
                    lowerDiagonal[n-1 + col-row] = 1

                    # Adding Q to the board
                    board[row] = board[row][:col] + 'Q' + board[row][col+1:]

                    helper(col+1)
                    
                    # Removing Q from the board
                    board[row] = board[row][:col] + '.' + board[row][col+1:]

                    # Setting Q to not visited
                    leftRow[row] = 0
                    upperDiagonal[row+col] = 0
                    lowerDiagonal[n-1 + col-row] = 0

        helper(0)
        return res
