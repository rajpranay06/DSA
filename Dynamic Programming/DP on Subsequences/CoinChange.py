'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0

'''

class Solution:
    # Memoization
    def noOfCoins(coins, index, k, dp):
           
        if dp[index][k] != -1:
            return dp[index][k]
            
        notTake = 0 + Solution.noOfCoins(coins, index-1, k, dp)

        take = int(1e9)

        if coins[index] <= k:
            take = 1 + Solution.noOfCoins(coins, index, k-coins[index], dp)
            
        dp[index][k] = min(take, notTake)
        return dp[index][k]

    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)
        
        # Tabulation
        dp = [[0 for j in range(amount + 1)] for i in range(n)]

        for i in range(amount+1):
            if i%coins[0] == 0:
                dp[0][i] = i//coins[0]
            else:
                dp[0][i] = int(1e9) 
        
        for i in range(1, n):
            for k in range(amount+1):
                notTake = dp[i-1][k]

                take = int(1e9)

                if coins[i] <= k:
                    take = 1 + dp[i][k-coins[i]]
                    
                dp[i][k] = min(take, notTake)

        
        if  dp[n-1][amount] >= int(1e9):
            return -1

        return dp[n-1][amount]

'''
Compelxity Analysis:

Memoization:

Time Complexity: O(N*T)

Reason: There are N*T states therefore at max ‘N*T’ new problems will be solved.

Space Complexity: O(N*T) + O(N)

Reason: We are using a recursion stack space(O(N)) and a 2D array ( O(N*T)).

Tabulation:

Time Complexity: O(N*T)

Reason: There are two nested loops

Space Complexity: O(N*T)

Reason: We are using an external array of size ‘N*T’. Stack Space is eliminated.

Space Optimating the Tabulation Approach:

'''

class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)
        
        # Tabulation
        dp = [[0 for j in range(amount + 1)] for i in range(n)]
        prev = [0]*(amount+1)
        curr = [0]*(amount+1)

        for i in range(amount+1):
            if i%coins[0] == 0:
                prev[i] = i//coins[0]
            else:
                prev[i] = int(1e9) 
        
        for i in range(1, n):
            for k in range(amount+1):
                notTake = prev[k]

                take = int(1e9)

                if coins[i] <= k:
                    take = 1 + curr[k-coins[i]]
                    
                curr[k] = min(take, notTake)
            
            prev= curr

        
        if  prev[amount] >= int(1e9):
            return -1

        return prev[amount]
'''

Compelxity Analysis:

Time Complexity: O(N*T)

Reason: There are two nested loops.

Space Complexity: O(T)

Reason: We are using two external arrays of size ‘T+1’.

'''
