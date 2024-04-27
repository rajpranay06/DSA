'''

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Approach:

Similar to creating binary tree from preorder and inorder. Just the root node will be at end of post order.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree(self, postorder, postStart, postEnd, inorder, inStart, inEnd, inMap):
        #Base condition
        if postStart > postEnd or inStart > inEnd:
            return 
        
        # Get the root values from last element of postorder
        root = TreeNode(postorder[postEnd])
        # Finding the root index in inorder
        inRoot = inMap[root.val]

        # Calculate the number of elements in the left subtree
        nodesLeft = inRoot - inStart

        # Go to left, by taking numbers before root index in inorder, and numbers from start in postorder
        root.left = self.tree(postorder, postStart, postStart+nodesLeft-1, inorder, inStart, inRoot-1, inMap)
        # Go to right, by taking the remaining nums
        root.right = self.tree(postorder, postStart+nodesLeft, postEnd-1, inorder, inRoot+1, inEnd, inMap)

        return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # HashMap to store inorder values and its indices
        inMap = {}
        for i in range(len(inorder)):
            inMap[inorder[i]] = i
        
        return self.tree(postorder, 0, len(postorder)-1, inorder, 0, len(inorder)-1, inMap)
