''' 

Given a number N. Find its unique prime factors in increasing order.

Example 1:

Input: N = 100
Output: 2 5
Explanation: 2 and 5 are the unique prime
factors of 100.
Example 2:

Input: N = 35
Output: 5 7
Explanation: 5 and 7 are the unique prime
factors of 35.

Approach:

Factorization just like basic math. Start with 2 and divide the number till it is not divisible by 2. Go to next number 3 do the same. 
For numbers like 4, 6, 8, 9 they wont be divisors of the number as we divided the number by 2 or 3 until it is not divisible by them. This will reduce the number traversals. 
And check for divisors till sqrt(n) and if the number is not 1 at the end, append the remaining number to the list, cause it would be a prime number.

Complexity Analysis:
Time Complexity - O(sqrt(N) * log(N)) 
Space Compelxity - O(N)

'''

import math
class Solution:
	def AllPrimeFactors(self, n):
		# Code here
		res = []
		for i in range(2, int(math.sqrt(n))+1):
		    if n%i == 0:
		        res.append(i)
		        while n%i == 0:
		            n = n//i
		if n != 1:
		    res.append(n)

        return res
