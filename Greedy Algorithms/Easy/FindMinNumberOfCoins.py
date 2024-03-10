'''

Given an infinite supply of Indian currency i.e. [1, 2, 5, 10, 20, 50, 100, 500, 1000] valued coins and an amount 'N'.
Find the minimum coins needed to make the sum equal to 'N'. You have to return the list containing the value of coins required in decreasing order.

For Example
For Amount = 70, the minimum number of coins required is 2 i.e an Rs. 50 coin and a Rs. 20 coin.
Note -> It is always possible to find the minimum number of coins for the given amount. So, the answer will always exist.

Sample Input 1
13
Sample Output 1
10 2 1
Explanation of Sample Input 1
The minimum number of coins to change is 3 {1, 2, 10}.

Sample Input 2
50
Sample Output 2
50

Time Complexity - O(N), where ‘N’ represents the amount to be changed.
In the worst case, we will end up removing the highest denomination coin most of the times. 
Note that the coins with a lesser denomination will not get picked by more than two times because there always exists a higher denomination for equivalent value.

Space Complexity - O(1)

'''

from typing import List

def MinimumCoins(n: int) -> List[int]:
    # write your code here
    coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    l = len(coins)
    res = []
    
    # Pick coins in decreasing order of their values.
    for i in range(l-1, -1, -1):
        while n >= coins[i]:
            n -= coins[i]
            res.append(coins[i])
    return res


