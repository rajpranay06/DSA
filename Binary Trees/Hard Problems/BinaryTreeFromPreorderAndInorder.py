'''

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Approach

Intuition
Before we dive into the algorithm, it's essential to grasp the significance of inorder and preorder traversals. Inorder traversal allows us to identify a node and its left and right subtrees, 
while preorder traversal ensures we always encounter the root node first. Leveraging these properties, we can uniquely construct a binary tree. 
The core of our approach lies in a recursive algorithm that creates one node at a time. We locate this root node in the inorder traversal, which splits the array into the left and right subtrees.

The inorder array keeps getting divided into left and subtrees hence to avoid unnecessary array duplication, we use variables (inStart, inEnd) and (preStart, preEnd) on the inorder and preorder array respectively. 
These variables effectively define the boundaries of the current subtree within the original inorder and preorder traversals. Everytime we encounter the root of a subtree via preorder traversal, 
we locate its position in the inorder array to get the left and right subtrees. So to save complexity on the linear look up, we employ a hashmap to store the index of each element in the inorder traversal. 
This transforms the search operation into a constant-time lookup.

Complexity Analysis
Time Complexity: O(N) where N is the number of nodes in the Binary Tree. This is because each node of the Binary Tree is visited once.

Space Complexity: O(N) where N is the number of nodes in the Binary Tree. The inorder hashmap to store the inorder array for fast lookup takes up space proportional to the input nodes. 
An auxiliary stack space ~ O(H) where H is the height of the Binary Tree is used. This is the stack space used to build the tree recursively. 
In the case of a skewed tree, the height of the tree will be H ~ N hence the worst case auxiliary space is O(N).

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree(self, preorder, preStart, preEnd, inorder, inStart, inEnd, inMap):
        #Base condition
        if preStart > preEnd or inStart > inEnd:
            return 
        
        # Get the root values from preorder
        root = TreeNode(preorder[preStart])
        # Finding the root index in inorder
        inRoot = inMap[root.val]

        # Calculate the number of elements in the left subtree
        nodesLeft = inRoot - inStart

        # Go to left, by taking numbers before root index in inorder, and numbers after root node in preorder
        root.left = self.tree(preorder, preStart+1, preStart+nodesLeft, inorder, inStart, inRoot-1, inMap)
        # Go to right, by taking the remaining nums
        root.right = self.tree(preorder, preStart+nodesLeft+1, preEnd, inorder, inRoot+1, inEnd, inMap)

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # HashMap to store inorder values and its indices
        inMap = {}
        for i in range(len(inorder)):
            inMap[inorder[i]] = i
        
        return self.tree(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1, inMap)

