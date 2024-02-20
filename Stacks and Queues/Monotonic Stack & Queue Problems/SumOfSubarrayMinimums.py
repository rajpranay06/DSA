'''

Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.


Intuition
To arrive at the solution, we must track two things for each element arr[i]:
1.	left[i]: the index of the first smaller element to the left of arr[i]
2.	right[i]: the index of the first element that is less than or equal to arr[i] to the right
With left[i] and right[i] determined, the number of subarrays in which arr[i] is the minimum can be calculated by (i - left[i]) * (right[i] - i).

Approach
The implementation leverages two main concepts: the "Monotonic Stack" pattern and the "Prefix Sum" pattern, to efficiently solve the problem without having to evaluate every subarray explicitly. 
Here's the walk-through of the implemented solution, step-by-step:
1.	Initialize two arrays, left and right, of the same length as arr to n, with -1 and n respectively. 
    These arrays will hold for each element the index of the previous smaller element (left) and the next smaller or equal element (right).
2.	Initialize a stack stk which we'll use to iterate over the array to find the left and right indices. The stack approach efficiently maintains a decreasing order of elements and their indices.
3.	Iterate through the elements of arr from left to right. For each element, while the stack is not empty and the top element of the stack is greater than or equal to the current element, 
    pop elements from the stack. This process is maintaining the stack in a strictly decreasing order.
4.	After elements larger than the current one are popped off stk, if the stack is not empty, set left[i] to the index of the top element of stk, which is the closest previous element smaller than arr[i]. 
    Then, push the current index i onto the stack.
5.	Clear the stack and then iterate through the elements of arr from right to left to similarly identify right[i] for each element. 
    The process mirrors step 3 and 4, but in the reversed direction and with the condition that any equal value element could also terminate the loop, maintaining strict decreasing order up to equal values.
6.	Once both left and right arrays are filled with proper indices, calculate the sum. By iterating over all indices i, 
    find the product of the count of subarrays where arr[i] is the minimum ((i - left[i]) * (right[i] - i)) and arr[i]. This represents the sum of arr[i] for all i in its valid subarrays.
7.	Sum these products for all i. As the final sum might be very large, each addition is taken modulo 10^9 + 7 to prevent integer overflow.

By combining the Monotonic Stack to find bounds for each element and the Prefix Sum pattern to calculate each element's contribution to the total sum, the algorithm achieves an efficient solution that operates in O(n) time complexity, where n is the size of the input array arr.
Complexity


Time complexity: The time complexity of the code is O(N + N + N).
Space complexity: The space complexity of the code is O(N).

'''

class Solution:
    def sumSubarrayMins(self, a: List[int]) -> int:
        n = len(a)
        st = []
        mod = 10**9 + 7

        # Prefix arrays to store the count of times index element is min
        left = [-1]*n
        right = [n]*n

        for i in range(n):
            # Pop the stack till no element is >= a[i], >= is for duplicates
            while st and a[st[-1]] >= a[i]:
                st.pop()
            # Set the prev min index to left[i]
            if st:
                left[i] = st[-1]
            st.append(i)
        
        # Empty the stack
        st = []

        for i in range(n-1,-1,-1):
            # Pop the stack till no element is > a[i] 
            while st and a[st[-1]] > a[i]:
                st.pop()
            # Set the next min index to right[i]
            if st:
                right[i] = st[-1]
            st.append(i)
        
        res = 0
        for i in range(n):
            res += ((a[i] * (i - left[i]) * (right[i] - i)) % mod)

        return res % mod

