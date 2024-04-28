'''

Problem Statement: Given a Binary Tree, implement Morris Preorder Traversal and return the array containing its preorder sequence.

Morris Preorder Traversal is a tree traversal algorithm aiming to achieve a space complexity of O(1) without recursion or an external data structure. 
The algorithm should efficiently visit each node in the binary tree in preorder sequence, printing or processing the node values as it traverses, without using a stack or recursion.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        preorder = []

        while curr:
            # If no left, add the curr to inorder and go to right
            if not curr.left:
                preorder.append(curr.val)
                curr = curr.right
            else:
                prev = curr.left
                # Finding the right most node
                while prev.right and prev.right != curr:
                    prev = prev.right
                
                if not prev.right:
                    # Add link from right most node to curr and add the curr to inorder
                    prev.right = curr
                    preorder.append(curr.val)
                    curr = curr.left
                else:
                    # If link already exists, remove the link and go to right
                    prev.right = None
                    curr = curr.right
        
        return preorder
