'''

Check whether the given Binary Tree is a Balanced Binary Tree or not. A binary tree is balanced if, for all nodes in the tree, the difference between left and right subtree height is not more than 1.

Solution: Post Order Traversal

So, the idea is to use post-order traversal. Since, in postorder traversal, we first traverse the left and right subtrees and then visit the parent node, 
similarly instead of calculating the height of the left subtree and right subtree every time at the root node, use post-order traversal, 
and keep calculating the heights of the left and right subtrees and perform the validation.

Approach : 
Start traversing the tree recursively and do work in Post Order.
For each call, caculate the height of the root node, and return it to previous calls.  
Simultaneously, in the Post Order of every node , Check for condition of balance as information of left and right subtree height is available.
If it is balanced , simply return height of current node and if not then return -1.
Whenever the subtree result is -1 , simply keep on returning -1.


Time Complexity: O(N) 
Space Complexity: O(1) Extra Space + O(H) Recursion Stack space (Where “H”  is the height of binary tree)

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Find left child height
        leftHeight = self.maxDepth(root.left)
        # Find right child height
        rightHeight = self.maxDepth(root.right)

        # If left or right height is -1, tree is imbalanced return -1
        if leftHeight == -1 or rightHeight == -1:
            return -1

        # If the height difference between left and right subtree is greater than 1 return -1
        if abs(leftHeight - rightHeight) > 1:
            return -1
            
        return 1 + max(leftHeight, rightHeight)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.maxDepth(root) != -1
        
