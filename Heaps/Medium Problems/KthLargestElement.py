'''

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Intuition
Takes an integer array nums and an integer k as input.
Returns the k-th largest element in the array nums.

Approach
Creates a PriorityQueue named data with a capacity of k + 1. This queue maintains elements in ascending order, meaning the smallest element is always at the front.
The use of k + 1 as the capacity ensures that the top k elements in the queue will always be the largest k elements seen so far.
Iterates through each element i in the array nums:
Adds the current element i to the data queue.
If the queue's size exceeds k (meaning more than k elements have been added):
Removes the smallest element (front of the queue) using data.poll(). This ensures that only the k largest elements remain in the queue.
After iterating through all elements, the queue data will contain the k largest elements seen so far, with the largest element at the front.
Returns the largest element (data.poll()) from the queue, which is the k-th largest element in the input array.

Complexity
Time complexity: O(n * log(k))
Space complexity: O(k)

'''

class Solution:
    def findKthLargest(self, a: List[int], k: int) -> int:
        heap = []
        for i in a:
            heapq.heappush(heap, i)
            # We are popping all the smallest nodes till kth node
            # If the heap len exceeds k we eleiminate the min element from heap
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

