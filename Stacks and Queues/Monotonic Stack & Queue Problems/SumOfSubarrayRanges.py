'''

You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.
Return the sum of all subarray ranges of nums.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,2,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0 
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.

Approach:

To calculate minTime[i] for every index, we can use a stack to maintain a monotonically increasing sequence during the iteration over nums:
What is the left index left? The element on nums[i]'s left in the stack.
What is the right index right? The element we are using to pop nums[i] from the stack.
In other words, minTime[i] is not calculated when we add nums[i] to the stack, but when we pop nums[i] from the stack, because only then are the left and right indexes clear to us.
Then we can calculate minTime[i] using: minTime[i]=(right−i)⋅(i−left)minTime[i] = (right - i) \cdot (i - left)minTime[i]=(right−i)⋅(i−left). 
As shown in the picture below, when we encounter nums[6] = 1, we should pop nums[3] = 4 from the stack, which is the time to calculate minTime[3].

Algorithm
1.	Initialize an empty stack stack, get the size of nums as n.
2.	Iterate over every index from 0 to n (inclusive). For each index right, if either of the following two condition is met:
•	index = n
•	stack is not empty and nums[mid] >= nums[right], where mid is its top value:
go to step 3.
Otherwise, repeat step 2.
3.	Calculate the number of subarrays with nums[mid] as its minimum value:
•	Pop mid from stack.
•	If stack is empty, set left = -1, otherwise, left equals the top element from stack.
•	Increment answer by (right - mid) * (mid - left).
•	Repeat step 2.

Complexity Analysis
Let nnn be the size of the input array nums.
•	Time complexity: O(n)
  o	To find the total sum of minVal, we only need one iteration over nums, and each number will be added to and popped from stack once, these also apply for finding maxVal.
  o	Therefore the overall time complexity is O(n).
•	Space complexity: O(n)
  o	We use a (monotonic) stack to keep the increasing (decreasing) sequence, in the worst-case scenario, there may be O(n) numbers in the stack, which takes O(n) space.

'''

class Solution:
    def subArrayRanges(self, a: List[int]) -> int:
        n = len(a)
        st = []
        res = 0

        # Approach is to find sum of all maxs - sum of all mins

        # Find the sum of all the minimums
        for right in range(n+1):
            while st and (right == n or a[st[-1]] >= a[right]):
                # curr is the index of the current element
                # left is the index of prev min 
                # right is the index of next min
                curr = st.pop()
                left = -1 if not st else st[-1]
                # We are subtracting the sum of mins from res
                res -= a[curr] * (curr - left) * (right - curr)  # finding the cnt of curr as min in subarrays
            st.append(right)

        st = []
        
        # Find the sum of all the maximum.
        for right in range(n+1):
            while st and (right == n or a[st[-1]] <= a[right]):
                curr = st.pop()
                left = -1 if not st else st[-1]
                # We are adding the sum of mins from res
                res += a[curr] * (curr - left) * (right - curr)  
            st.append(right)

        return res







