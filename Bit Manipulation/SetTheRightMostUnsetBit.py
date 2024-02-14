'''

Problem statement
The problem is to find the rightmost bit of a non-negative number 'N' that is currently unset (i.e., has a value of 0) in its binary representation and set it to 1.

Return the number after setting the rightmost unset bit of 'N'. If there are no unset bits in N's binary representation, then the number should remain unchanged.

Example:
N = 5
Output: 7
Explanation: The binary representation of 5 is 101. After setting the rightmost unset bit it becomes 111 which is 7.


Time Complexity : O(log N) 
Space Complexity : O(1)

where 'N' is the given input
'''

from typing import *

def setBits(N : int) -> int:

    x = N

    # Find the position of the east significant unset bit.
    while (x & 1) != 0:
        x = x >> 1

    # Check if there's any unset bit, if not return 'N'.
    if x == 0:
        return N

    # Set the least significant unset bit of ‘N’ to 1 and return.
    return (N | (N + 1))


'''

Time Complexity : O(1)
Space Complexity : O(1)

'''

from typing import *

def setBits(N : int) -> int:

    # Check if there's any unset bits.
    if (N & (N + 1)) == 0:
        return N

    # Set the least significant unset bit of ‘N’ to 1 and return.
    return (N | (N + 1))
