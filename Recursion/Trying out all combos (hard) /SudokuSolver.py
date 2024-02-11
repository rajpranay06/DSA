'''

Problem Statement:

Given a 9×9 incomplete sudoku, solve it such that it becomes valid sudoku. Valid sudoku has the following properties.

         1. All the rows should be filled with numbers(1 – 9) exactly once.

         2. All the columns should be filled with numbers(1 – 9) exactly once.

         3. Each 3×3 submatrix should be filled with numbers(1 – 9) exactly once.

Note: Character ‘.’ indicates empty cell.

Intuition:

Since we have to fill the empty cells with available possible numbers and we can also have multiple solutions, the main intuition is to try every possible way of filling the empty cells. 
And the more correct way to try all possible solutions is to use recursion. 
In each call to the recursive function, we just try all the possible numbers for a particular cell and transfer the updated board to the next recursive call.


Time Complexity: O(9(n ^ 2)), in the worst case, for each cell in the n2 board, we have 9 possible numbers.

Space Complexity: O(1), since we are refilling the given board itself, there is no extra space required, so constant space complexity.

'''

class Solution:
    def solve(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for c in ['1','2','3','4','5','6','7','8','9']:
                        
                        # Checking if the sudoku is valid for the cyrrent char
                        if Solution.isValid(board, i, j, c):
                            
                            board[i][j] = c
                            # If Valid return True
                            if Solution.solve(board):
                                return True
                            # Else remove the char
                            board[i][j] = '.'
                    # If no char is valid
                    return False
        # If the sudoku is filled
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        Solution.solve(board)
        

    def isValid(board, row, col, c):
        for i in range(0,9):
            # Checking for the whole column
            if board[row][i] == c:
                return False
            
            # Checking for the whole row
            if board[i][col] == c:
                return False
            
            # Checking for the 3x3 matrix
            if board[3 * (row//3) + (i//3)][3 * (col//3) + (i%3)] == c:
                return False
                
        return True
                            
        
