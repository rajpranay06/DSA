'''

The weight of N items and their corresponding values are given. We have to put these items in a knapsack of weight W such that the total value obtained is maximized.
Note: We can either take the item as a whole or break it into smaller units.

Example:

Input: N = 3, W = 50, values[] = {100,60,120}, weight[] = {20,10,30}.
Output: 240.00
Explanation: The first and second items  are taken as a whole  while only 20 units of the third item is taken. Total value = 100 + 60 + 80 = 240.00

Approach: 

The greedy method to maximize our answer will be to pick up the items with higher values. Since it is possible to break the items as well we should focus on picking up items having higher value /weight first. 
To achieve this, items should be sorted in decreasing order with respect to their value /weight. Once the items are sorted we can iterate. 
Pick up items with weight lesser than or equal to the current capacity of the knapsack. In the end, if the weight of an item becomes more than what we can carry, break the item into smaller units. 
Calculate its value according to our current capacity and add this new value to our answer.

Time Complexity: O(n log n + n). O(n log n) to sort the items and O(n) to iterate through all the items for calculating the answer.

Space Complexity: O(1), no additional data structure has been used.

'''

from os import *
from sys import *
from collections import *
from math import *

def maximumValue(items, n, w):

	# Write your code here.
	# ITEMS contains [weight, value] pairs.
	
	# Sorting items acc to their val/weight ratio 
	items.sort(key=lambda x: x[1]/x[0], reverse = True)
	res = 0
	for i in items:
		# If curr weight can be accumulated with knacpsack weight add it to knapsack
		if i[0] <= w:
			w -= i[0]
			res += i[1]
		else:
			# Else add a fraction of it to knapsack
			res += w * (i[1]/i[0])
			break
	return res

