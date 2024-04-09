'''

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Intuition

To determine if two binary trees are identical, we can follow a recursive approach. 
We traverse both trees in the preorder manner, meaning that the current node's value is checked before recursively traversing its left and right subtrees.

The idea is to traverse both trees simultaneously, comparing the values of corresponding nodes at each step. 
We need to ensure that the left subtree of each node in the first tree is identical to the left subtree of the corresponding node in the second tree, and similarly for the right subtrees.

Algorithm:

Step 1: Start at the root node of both trees (node1 and node2).
Step 2: Check if the values of the current nodes in both trees are equal. If not return false.
Step 3: Recursively check the left then right subtree of the current node in both trees is identical.
Step 4: If all the recursive checks return true, then return the trees are identical, otherwise they are not.


Time Complexity: O(N+M) where N is the number of nodes in the first Binary Tree and M is the number of nodes in the second Binary Tree. 
This complexity arises from visiting each node of the two binary nodes during their comparison.

Space Complexity: O(1) as no additional space or data structures is created that is proportional to the input size of the tree. 
O(H) Recursive Stack Auxiliary Space : The recursion stack space is determined by the maximum depth of the recursion, which is the height of the binary tree denoted as H. 
In the balanced case it is log2N and in the worst case (its N).

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        # Check if the current nodes have the same data value
        # and recursively check their left and right subtrees
        return (p.val == q.val and 
                    self.isSameTree(p.left, q.left) and 
                    self.isSameTree(p.right, q.right))


