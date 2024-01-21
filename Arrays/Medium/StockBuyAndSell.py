'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


Intuition: We will linearly travel the array. We can maintain a minimum from the start of the array and compare it with every element of the array, 
if it is greater than the minimum then take the difference and maintain it in max, otherwise update the minimum.
'''

class Solution:
    def maxProfit(self, a: List[int]) -> int:
        buy = a[0]
        profit = 0
        for i in range(len(a)):
            buy = min(buy,a[i])
            profit = max(profit,a[i] - buy)
        return profit

'''
Time complexity: O(n)

Space Complexity: O(1)
'''
