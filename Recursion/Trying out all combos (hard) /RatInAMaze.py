'''

Problem statement
You are given a N*N maze with a rat placed at 'mat[0][0]'. Find all paths that rat can follow to reach its destination i.e. mat[N-1][N-1]. 
The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right).

In the given maze, each cell can have a value of either 0 or 1. Cells with a value of 0 are considered blocked, which means the rat cannot enter or traverse through them. 
On the other hand, cells with a value of 1 are open, indicating that the rat is allowed to enter and move through those cells.

Input:
N = 4
m[][] = {{1, 0, 0, 0},
        {1, 1, 0, 1}, 
        {1, 1, 0, 0},
        {0, 1, 1, 1}}

Output: DDRDRR DRDDRR

'''


def ratMaze(a: List[List[int]]) -> List[str]:
    # Write your code here.
    n = len(a)
    res = []
    vis = [[0 for j in range(n)] for i in range(n)]
    
    # Keeping an array for travelling 
    # down => (i+1,j) => (1,0)
    # left => (i,j-1) => (0,-1)
    # right => (i,j+1) => (0,1)
    # up => (i-1,j) => (-1,0)
    di = [1,0,0,-1]
    dj = [0,-1,1,0]

    def solve(row, col, path):

        if row == n-1 and col == n-1:
            res.append(path)
            return
        
        directions = "DLRU"
        for i in range(4):
            # Setting the next position
            nextRow = row + di[i]
            nextCol = col + dj[i]
            if nextRow >= 0 and nextCol >= 0 and nextCol < n and nextRow < n and vis[nextRow][nextCol] == 0 and a[nextRow][nextCol] == 1:
                vis[row][col] = 1
                solve(nextRow, nextCol, path + directions[i])
                vis[row][col] = 0

    if a[0][0] == 1:
        solve(0, 0, "")

    return res


'''

Time Complexity: O(4^(m*n)), because on every cell we need to try 4 different directions.

Space Complexity:  O(m*n), Maximum Depth of the recursion tree(auxiliary space).

'''

