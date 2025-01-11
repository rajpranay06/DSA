'''

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1

Intuition
The problem revolves around finding the maximum area formed between two lines in a container with heights represented as an array. 
My first thought is that a two-pointer approach could help efficiently find the solution by systematically narrowing down the search space while keeping track of the maximum area.

Approach
The two-pointer technique starts with one pointer at the beginning and the other at the end of the height array. 
The area is calculated by taking the minimum of the two heights multiplied by the distance between them.

We then update the result if the current area is greater than the previously recorded maximum area. 
Next, we move the pointer that points to the smaller height inward because moving the larger height would not increase the area. This process continues until the two pointers meet.

Complexity
Time complexity - O(n)
Each element in the height array is visited at most once as the two pointers move toward each other.

Space complexity - O(1)
No additional space is used apart from a few variables to store the results and pointers.

'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        maxArea = 0
        maxH = max(height)
        while left < right:
            maxArea = max(maxArea, min(height[left], height[right])*(right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

            if maxH * (right - left) < maxArea:
                return maxArea

        return maxArea

