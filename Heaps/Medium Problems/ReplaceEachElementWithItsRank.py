'''

Given an array of integers 'ARR’ of size ‘N’. Replace each element of this array with its corresponding rank and return the array.
The rank of an element is an integer between 1 to ‘N’ inclusive that represents how large the element is in comparison to other elements of the array. 
The following rules can also define the rank of an element:

1. It is an integer starting from 1.

2. The larger the element, the larger the rank. If two elements are equal, their rank must be the same.

3. It should be as small as possible.
For Example:
'ARR' = [4, 7, 2, 90]

Here, 2 is the smallest element, followed by 4, 7, and 90. 

Hence rank of element 2 is 1, element 4 is 2, element 7 is 3, and element 90 is 4.

Hence we return [2, 3, 1, 4].

Sample Input 1:
5
1 2 6 9 2 

Sample Output 1:
1 2 3 4 2

Explanation Of Sample Input 1:
Here, 1 is the smallest element, 2 is the second-smallest element and 6 is the third-smallest element and 9 is the largest element.

So, the rank of 1 should be 1.

The rank of 2 should be 2.

The rank of 6 should be 3.

The rank of 9 should be 4.

Thus after replacing elements with their rank we get [1, 2, 3, 4, 2]

'''

from typing import List
import heapq

def replaceWithRank(a: List[int], n: int) -> List[int]:
    # write your code here

    heap = []

    # Creating Min heap
    for i in range(n):
        heapq.heappush(heap, (a[i], i))
    
    rank = 0
    prev = float('-inf')

    while heap:
        curr = heapq.heappop(heap)
        # Checking if popped element is not prev to increase the rank
        if curr[0] != prev:
            rank += 1
        # Setting the rank acc to index
        a[curr[1]] = rank
        prev = curr[0]
    
    return a
    
