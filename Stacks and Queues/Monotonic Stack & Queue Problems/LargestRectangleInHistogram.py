'''

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Approach - 1
Use the same approach as sum of subarray minimums, Find the width by using left[i] – right[i] – 1, multiply with a[i] to get area. 

Time Complexity: O(5N) -> 2N for left traversal, 2N for right traversal and N to find max area.

Space Complexity: O(3N) where 3 is for the stack, left small array and a right small array

'''

class Solution:
    def largestRectangleArea(self, a: List[int]) -> int:
        n = len(a)
        st = []
        mod = 10**9 + 7

        # Prefix arrays to store the count of times index element is min
        left = [-1]*n
        right = [n]*n

        for i in range(n-1,-1,-1):
            # Pop the stack till no element is > a[i] 
            while st and a[st[-1]] > a[i]:
                st.pop()
            # Set the next min index to right[i]
            if st:
                right[i] = st[-1]
            st.append(i)

        # Empty the stack
        st = []

        for i in range(n):
            # Pop the stack till no element is >= a[i], >= is for duplicates
            while st and a[st[-1]] >= a[i]:
                st.pop()
            # Set the prev min index to left[i]
            if st:
                left[i] = st[-1]
            st.append(i)

        maxRes = 0
        for i in range(n):
            maxRes = max(maxRes, a[i]*(right[i] - left[i] - 1))
        return maxRes


'''

Approach 2:

Use the same approach as sum of subarray range, but only use to find min index. Find the width by using left – right – 1, multiply with a[curr] to get area. 

Time Complexity: O( N ) + O (N)
Space Complexity: O(N)

'''

class Solution:
    def largestRectangleArea(self, a: List[int]) -> int:
        n = len(a)
        st = []
        maxRes = 0

        for right in range(n+1):
            while st and (right == n or a[st[-1]] >= a[right]):
                # curr is the index of the current element
                # left is the index of prev min 
                # right is the index of next min
                curr = st.pop()
                left = -1 if not st else st[-1]
                maxRes = max( maxRes, a[curr] * (right - left -1))  # finding the area
            st.append(right)

        return maxRes
