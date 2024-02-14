'''

Problem statement
You are given an array 'arr' of size 'n'.
It contains an even number of occurrences for all numbers except two numbers.
Find those two numbers which have odd occurrences and return in decreasing order.

Example:
For 'arr' = {2, 4, 1, 3, 2, 4} , 'n' = 6.
Answer is {3, 1}.
Here, numbers 1, 3 have occurrence 1 i.e. odd and numbers 2, 4 have occurrence 2 i.e. even.


Approach:

Similar to Array problem finding missing and repeating numbers.
We will xor the whole array to find x^y values. Now find the right most set bit. Now group the array elements which set bits are at the same position of xor set bit adn xor them.
We will get two numbers with setBit and not Set bits. Return the two numbers.

Time Complexity - O(n), where 'n' is the size of array ‘arr’. 
We are iterating via ‘i’ from 0 to ‘n’-1 two times. Hence the overall time complexity of this solution is O(n).

Space Complexity - O(1).
We are not utilising any extra space, hence the O(1) space complexity.

'''

from typing import *

def twoOddNum(a : List[int]) -> List[int]:
    # Write your code here.
    xr = 0
    for i in a:
        xr ^= i
    
    setBit = 0

    while not xr & (1<<setBit):
        setBit += 1
    
    one = 0
    zero = 0

    for i in a:
        if i & (1<<setBit):
            one ^= i
        else:
            zero ^= i
    
    if one > zero:
        return [one, zero]
    
    return [zero, one]
