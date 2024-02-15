'''

Problem statement
You are given a number 'N' and its reverse 'R'.

Return the number raised to the power of its own reverse. As answers can be very large, print the result modulo '10^9 + 7'.

For Example:

For 'N' = 20, 'R' = 2
The answer is 400 since 20^2 as the reverse of 20 is 2.

Approach:

A number can be represented as the sum of powers of two i.e. binary representation of a number.

Algorithm:

Initialise variable ‘mod’ = 1e9+7
Initialise variable 'ans' = 1
Initialise variable ‘num’ = ‘N’
While ( ‘R’ != 0)
If ‘R’ % 2 == 1
‘ans’ = ('ans' * ‘num’) % ‘mod’
'num' = ('num' * 'num') % 'mod'
‘R’ = ‘R’ / 2
return ‘ans’


Time Complexity - O(LogR), where 'R' is the number obtained by reversing ‘N’. 
We can write the number ‘X’ in just ‘logX’ bits. We are just iterating over ‘logR’ bits. Hence the total time complexity for the solution is O(logR).

Space Complexity - O(1).
We are not utilising any extra space here, hence the (1) space complexity.

'''

from typing import *

def power(a : int, n : int) -> int:
    # Write your code here.
    res = 1
    mod = int(10 ** 9) + 7

    while n > 0:
        if n&1:
            res *= a % mod
        
        a *= a % mod
        n >>= 1
    
    return res % mod
