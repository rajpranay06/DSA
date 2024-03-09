'''

Given two equally sized 1-D arrays A, B containing N integers each.
A sum combination is made by adding one element from array A and another element of array B.
Return the maximum C valid sum combinations from all the possible sum combinations.

Input Format
First argument is an one-dimensional integer array A of size N.
Second argument is an one-dimensional integer array B of size N.
Third argument is an integer C.

Output Format
Return a one-dimensional integer array of size C denoting the top C maximum sum combinations.

NOTE:
The returned array must be sorted in non-increasing order.

Example Input
Input 1:
 A = [3, 2]
 B = [1, 4]
 C = 2

Input 2:
 A = [1, 4, 2, 3]
 B = [2, 5, 1, 6]
 C = 4


Example Output
Output 1:
 [7, 6]

Output 1:
 [10, 9, 9, 8]


Example Explanation
Explanation 1:
 7     (A : 3) + (B : 4)
 6     (A : 2) + (B : 4)

Explanation 2:
 10   (A : 4) + (B : 6)
 9   (A : 4) + (B : 5)
 9   (A : 3) + (B : 6)
 8   (A : 3) + (B : 5)

 '''

import heapq
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, a, b, c):
        heap = []
        a.sort(reverse = True)
        b.sort(reverse = True)
        n = len(a)
        for i in range(c):
            heapq.heappush(heap, a[i]+b[i])
        
        for i in range(n):
            for j in range(n):
                if i != j:
                    if a[i] + b[j] > heap[0]:
                        heapq.heappop(heap)
                        heapq.heappush(heap, a[i]+b[j])
                    else:
                        break
        
        res = [0]*c                
        for i in range(c-1,-1,-1):
            res[i] = heapq.heappop(heap)
        return res
