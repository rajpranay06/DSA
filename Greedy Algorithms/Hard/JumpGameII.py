'''

You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
0 <= j <= nums[i] and i + j < n. Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [2,3,0,1,4]
Output: 2

Intuition
To solve the "Jump Game II" problem, we want to find the minimum number of jumps needed to reach the end of an array, starting from the first element. 
Each element in the array tells us the maximum number of steps we can jump from that position.

We start at the first element and keep track of two important things:
The maximum index we can reach from the current position (this is maxend).
The farthest position we can reach in the current jump (this is end).
We then iterate through the array. For each position i, we update maxend to be the maximum of maxend and i + nums[i]. This tells us the farthest position we can reach from i in a single jump.

If we reach the end of the current jump (i == end), it means we need to make another jump. We update end to maxend and increment our jump count (ans) by 1.
We continue this process until we reach the end of the array. At that point, the value of ans will be the minimum number of jumps needed to reach the end.

Approach
  1.	Initialize end and maxend to 0, and ans (the jump count) to 0.
  2.	Iterate through the array from index 0 to len(nums)-1.
  3.	For each index i update maxend to be the maximum of maxend and i + nums[i].
  4.	If i reaches end (i.e., we have reached the end of the current jump):
      •	Update end to maxend.
      •	Increment ans by 1.
  5.	Continue until we reach the end of the array.
  6.	Return ans as the minimum number of jumps needed which is checked at each i when maxend is reaching the end of array.


Complexity
Time complexity: O(n)
Space complexity: O(1)

'''

class Solution:
    def jump(self, a: List[int]) -> int:
        n = len(a)

        # If array length is 1 or 0 no steps are required
        if n < 2:
            return 0

        currEnd = 0   # Current end where the array index can traverse 
        maxEnd = 0    # Max step the array element can go
        res = 0
        i = 0  

        while True:  #Constraint is that every test case is valid for the jump game so this loop has to eventually end by return
            while i <= currEnd:
                maxEnd = max(a[i]+i, maxEnd)
                if maxEnd >= n-1:  # We have reached the end
                    return res+1
                i += 1
            
            if currEnd < maxEnd:
                currEnd = maxEnd
                res += 1   # We need to move a step 
        
        return res




        
        

        
