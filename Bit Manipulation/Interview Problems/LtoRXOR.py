'''

Problem statement
You are given two numbers 'L' and 'R'.

Find the XOR of the elements in the range [L, R].

For Example:
For 'L' = 1 and ‘R’ = 5.
The answer is 1.

'''

from typing import *

def findXORFrom1ToN(n):
    if n%4 == 0:
        return n
    
    if n%4 == 1:
        return 1
    
    if n%4 == 2:
        return n+1
    
    return 0

    '''
        How does this work? 
        When we do XOR of numbers, we get 0 as the XOR value just before a multiple of 4. 
        This keeps repeating before every multiple of 4. 
        

        Number Binary-Repr  XOR-from-1-to-n
        1         1           [0001]
        2        10           [0011]
        3        11           [0000]  <----- We get a 0
        4       100           [0100]  <----- Equals to n
        5       101           [0001]
        6       110           [0111]
        7       111           [0000]  <----- We get 0
        8      1000           [1000]  <----- Equals to n
        9      1001           [0001]
        10     1010           [1011]
        11     1011           [0000] <------ We get 0
        12     1100           [1100] <------ Equals to n

    '''
def findXOR(L : int, R : int) -> int:
    # Write your code here.

    # We can get xor of 1 to L-1 and xor of 1 to R and do xor of both to get xor of L to R
    return findXORFrom1ToN(L-1) ^ findXORFrom1ToN(R)
    

'''

Time Complexity - O(1).
We are just checking a few conditions. Hence the total time complexity for the solution is O(1).

Space Complexity - O(1).
We are not utilising any extra space here, hence the O(1) space complexity.

'''
