'''

Given an m x n grid of characters board and a string word, return true if the word exists in the grid. 
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: 
[
["A", "B", "C", "E"], 
["S", "F", "C", "S"],
["A", "D", "E", "E"]
] 
word = "ABCCED"
Output: true

Explanation: We can easily find the given word in the matrix.

Approach:

Step 1: Find the first character of the given string.

Step 2: Start Backtracking in all four directions until we find all the letters of sequentially adjacent cells.

Step 3: At the end, If we found our result then return true else return false.

Edge cases: Now think about what will be our stopping condition, 
we can stop or return false if we reach the end of the boundaries of the matrix or the letter at which we are making recursive calls is not the required letter.

We will also return if we found all the letters of the given word i.e. we found the number of letters equal to the length of the given word.

'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])

        # Recursive function
        def check(row, col, index):
            if index  == len(word):
                return True
            
            # Edge cases
            if row < 0 or col < 0 or row == n or col == m or board[row][col] != word[index] or board[row][col] == '!':
                return False
            
            # Marking the visited character
            c = board[row][col] 
            board[row][col] = '!'

            # check top
            top = check(row-1, col, index+1)
            # check bottom
            bottom = check(row+1, col, index+1)
            # check right
            right = check(row, col+1, index+1)
            # check left
            left = check(row, col-1, index+1)

            # Undo the change
            board[row][col] = c

            return top or bottom or right or left 
        
        index = 0
        # Finding the first character position
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[index]:
                    if check(i, j, index):
                        return True
        
        return False


'''

Time Complexity:  O(m*n*4^k), where “K” is the length of the word. And we are searching for the letter m*n times in the worst case. 
Here 4 in 4^k is because at each level of our decision tree we are making 4 recursive calls which equal 4^k in the worst case.

Space Complexity: O(K), Where k is the length of the given words.

'''


