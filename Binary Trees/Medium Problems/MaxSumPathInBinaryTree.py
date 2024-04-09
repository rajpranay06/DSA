'''

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. 
Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.

Intuition
To find the diameter of a binary tree, we can think of every node as a potential `Curving Point` of the path along which we find the sum. 
The maximum sum of a path through a turning point (like a curve) can be found by adding the maximum sum achievable in the left subtree, the right subtree, and the value of the turning point.

We can recursively traverse the tree, considering each node as a potential turning point and storing the maximum value (our final answer) in a reference variable. 
The recursive function should be defined in such a way that we consider both the possibilities:

When the current node is the turning point and in this scenario we calculate the maximum path sum taking into sum contributions from both the left and right subtrees along with the value of the current node.
When the current node is not the turning point, we consider only the left or the right subtree. The maximum of the two is returned as the maximum path sum of that subtree.


Time Complexity: O(N) where N is the number of nodes in the Binary Tree. This complexity arises from visiting each node exactly once during the recursive traversal.

Space Complexity: O(1) as no additional space or data structures is created that is proportional to the input size of the tree. 
O(H) Recursive Stack Auxiliary Space : The recursion stack space is determined by the maximum depth of the recursion, which is the height of the binary tree denoted as H. 
In the balanced case it is log2N and in the worst case its N.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf') 
        
        def findMaxSum(root):
            
            if not root:
                return 0
            
            # Find left and right subtree sum
            left_sum = findMaxSum(root.left)
            right_sum = findMaxSum(root.right)
            
            # Set maxSum
            self.maxSum = max(self.maxSum, root.val + left_sum + right_sum)
            
            # Return the current subtree sum
            return max(root.val + max(left_sum,right_sum), 0)
        
        findMaxSum(root)
        return self.maxSum

        
