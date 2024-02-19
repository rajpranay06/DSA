'''

Problem statement
You are given an array 'arr' of length 'N'.
You are given 'Q' queries, and for each query, you are given an index(0-based indexing).

Answer to each query is the number of the strictly greater elements to the right of the given index element.
You must return an array 'answer' of length ’N’, where ‘answer[i]’ is the answer to the ‘ith’ query.

Example:
Input:
arr = [5, 2, 10, 4], N=4, Q=2, query = [0, 1]
Output:
1 2

Explanation: The element at index 0 is 5 for the first query. There is only one element greater than 5 towards the right, i.e., 10.
For the second query, the element at index 1 is 2. There are two elements greater than 2 towards the right, i.e., 10 and 4. 
Hence we return [1, 2]

Approach 
The idea behind this approach is Count Inversion(Merge Sort). In Count Inversion we were finding Inversion pair using merge sort. For i<j if arr[i]>arr[j] then that will be an inversion pair. 
Using similar logic we can find those pair for which i<j and arr[i]<arr[j]. So we can find, there are how many “j” for an “i” such that i<j and arr[i]<arr[j]. 
Then that number of j will be the number of the next greater element for i.

So we will simply perform merge sort and in merging we will check this condition -” i<j and arr[i]<arr[j]”

Time Complexity: O(NlogN), because of Merge sort implementation
Auxiliary space: O(N)

'''

from typing import *

def merge(vec, ans, low, mid, high):
    n1 = mid - low + 1
    n2 = high - mid
 
    arr = vec[low:low + n1]
    brr = vec[mid + 1:mid + 1 + n2]
 
    i = 0
    j = 0
    k = low
 
    while i < n1 and j < n2:
        if arr[i][0] < brr[j][0]:
            # Finding Number of next greater element
            ans[arr[i][1]] += n2 - j
            vec[k] = arr[i]
            i += 1
            k += 1
        else:
            vec[k] = brr[j]
            j += 1
            k += 1
 
    while i < n1:
        vec[k] = arr[i]
        i += 1
        k += 1
 
    while j < n2:
        vec[k] = brr[j]
        j += 1
        k += 1
 
# Function for performing Merge Sort
def mergesort(vec, ans, low, high):
    if low < high:
        # Divide them into two different part
        mid = low + (high - low) // 2
        # Calling mergesort function recursively for both
        # the part
        mergesort(vec, ans, low, mid)
        mergesort(vec, ans, mid + 1, high)
        # Merging both and part and calculating Number of
        # Next greater element
        merge(vec, ans, low, mid, high)
 
def countGreater(n: int, q: int, arr: List[int], query: List[int]) -> List[int]:
    # Write your code here
    # Storing elements of list with their index into
    # list of pairs
    vec = [(arr[i], i) for i in range(n)]
 
    # Declaring a list to store Number of next greater
    # element for every element
    ans = [0] * n
    mergesort(vec, ans, 0, n - 1)
 
    # Printing number of next greater element for Q queries
    res = []
    
    for i in query:
        res.append(ans[i])

    return res
