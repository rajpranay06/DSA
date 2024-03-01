'''

You have been given ‘K’ different arrays/lists, which are sorted individually (in ascending order). 
You need to merge all the given arrays/list such that the output array/list should be sorted in ascending order.

Sample Input 1:
1
2
3 
3 5 9 
4 
1 2 3 8   

Sample Output 1:
1 2 3 3 5 8 9 
Explanation of Sample Input 1:
After merging the two given arrays/lists [3, 5, 9] and [ 1, 2, 3, 8], the output sorted array will be [1, 2, 3, 3, 5, 8, 9].

Approach 1:
Add all the elements into min heap. Perform heapifyDown after popping root element and swapping it with last node. 

Time Complexity - O(N*k) + O((N*k)log(N*k))
Space Complexity - O(N*k)

'''

from sys import *
from collections import *
from math import *
import heapq

def moveDown(heap, pos, n):
	largest = pos 
	left = 2*pos + 1
	right = 2*pos + 2
	if left < n and heap[left] < heap[largest]:
		largest = left
	if right < n and heap[right] < heap[largest]:
		largest = right
	if largest != pos:
		heap[largest], heap[pos] = heap[pos], heap[largest]
		moveDown(heap, largest, n)

def mergeKSortedArrays(kArrays, k:int):
	# Write your code here.
	# kArrays is a list of 'k' lists.
	# Return a list.
	heap = []
	# Adding all the elements into heapq
	for arr in kArrays:
		for i in arr:
			heapq.heappush(heap, i)

	n = len(heap)
	res = []
	# Removing the min element and heapifying down
	for _ in range(n):
		res.append(heap[0])
		heap[0] = heap[-1]
		heap.pop()
		moveDown(heap, 0, len(heap))
	
	return res


'''

The idea is to use the concept of min-heap. As we know, the root of the min-heap is always the minimum element in the heap. 
Thus, insert the first elements of all the ‘K’ arrays into the heap along with their indices, 
and then removing the minimum ( root ) element and adding it to the output array will give us the required result. 
We will store indices into the heap because we can get the next greater element from the same array where the current element has been popped.
 
Algorithm: 

Create an output array ‘RESULT’.
Create a min-heap of size K and insert the first element of all the arrays, along with its indices, into the heap.
The heap is ordered by the element of the array/list.
While the min-heap is not empty, we will keep doing the following operations :
Remove the minimum element from the min-heap (the minimum element is always at the root) and store it in the output array.
Insert the next element from the array for which the current element is extracted. 
If the array doesn’t have any more elements i.e. if the index of the above-removed component is equal to ‘LENGTH-1’ of the array from which the element is extracted, then do nothing. 
Because we are done with this array.
After the above process, 'RESULT' will contain all the elements of ‘K’ arrays in ascending order.
Return the output array i.e. ‘RESULT’.

Time Complexity - O((N * K) * log(K)), Where ‘K’ is the number of arrays and ‘N’ is the average number of elements in every array. 
We are using the min-heap of size K. Due to the insertion and the removal of elements in the heap, the final complexity of this approach is O(K * N * log(K)).

Space Complexity - O(N * K), where ‘K’ is the number of arrays and ‘N’ is the average number of elements in every array.
Since we are using a min-heap of size K arrays for the average N elements present in every array, therefore, the space complexity of the approach is O(N * K).

'''


import heapq

def mergeKSortedArrays(kArrays, k):
    
    res = []
    
    # Create a min heap to store atmost k heap nodes at a time.
    minHeap = []
    
    for i in range(len(kArrays)):    
        heapq.heappush( minHeap, (kArrays[i][0], i, 0) )
        
	
    while len(minHeap) > 0:
        # Remove the minimum element from the heap.
        curr = heapq.heappop(minHeap)
        
        # i is the array number and j is the index of the removed element in the ith array.
        i = curr[1]
        j = curr[2]
        
        # Add the removed element to the output array.
        res.append(curr[0])
        
        # If the next element of the extracted element exists, add it to the heap.
        if j + 1 < len(kArrays[i]):
            
            heapq.heappush( minHeap, (kArrays[i][j + 1], i, j + 1) )
    
            
    # Return the output array.        
    return res
        
    
