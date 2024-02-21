'''

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. 
Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7


Approach
We address this problem with the help of a data structure that keeps checking whether the incoming element is larger than the already present elements. 
This could be implemented with the help of a de-queue. When shifting our window, we push the new element in from the rear of our de-queue. Following is a sample representation of our dequeue:

Every time before entering a new element, we first need to check whether the element present at the front is out of bounds of our present window size. If so, we need to pop that out. 
Also, we need to check from the rear that the element present is smaller than the incoming element. If yes, there’s no point storing them and hence we pop them out. 
Finally, the element present at the front would be our largest element.

Time Complexity: O(N) + O(N)
Space Complexity: O(K)

'''

from collections import deque 
class Solution:
    def maxSlidingWindow(self, a: List[int], k: int) -> List[int]:
        # Using deque to pop and push from left and right
        q = deque()
        n = len(a)
        res = []

        for i in range(n):
            # If there are more than k indices in deque
            while q and q[0] == i-k:
                q.popleft()
            
            # If the top index val is less than curr val, pop them
            while q and a[q[-1]] <= a[i]:
                q.pop()

            q.append(i)

            # Adding max values to res, we are keeping indices in descending order so front indiex will store max val 
            if i >= k-1:
                res.append(a[q[0]]) 
        
        return res
