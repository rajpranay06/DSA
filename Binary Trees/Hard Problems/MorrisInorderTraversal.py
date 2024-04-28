'''

Problem Statement: Given a Binary Tree, implement Morris Inorder Traversal and return the array containing its inorder sequence.

Morris Inorder Traversal is a tree traversal algorithm aiming to achieve a space complexity of O(1) without recursion or an external data structure. 
The algorithm should efficiently visit each node in the binary tree in inorder sequence, printing or processing the node values as it traverses, without using a stack or recursion.

Intuition

Morris Traversal is a tree traversal algorithm that allows for an in-order traversal of a binary tree without using recursion or a stack. It uses threading to traverse the tree efficiently. 
The key idea is to establish a temporary link between the current node and its in-order successor

The inorder predecessor of a node is the rightmost node in the left subtree. So when we traverse the left subtree, we encounter a node whose right child is null, this is the last node in that subtree.
Hence, we observe a pattern whenever we are at the last node of a subtree such that the right child is pointing to none, we move to the parent of this subtree./p>

When we are currently at a node, the following cases can arise:

Case 1: The current node has no left subtree.

Print the value of the current node.
Then to the right child of the current node.

If there is no left subtree, we simply print the value of the current node because there are no nodes to traverse on the left side. After that, we move to the right child to continue the traversal.

Case 2: There is a left subtree, and the right-most child of this left subtree is pointing to null.

Set the right-most child of the left subtree to point to the current node.
Move to the left child of the current node.

In this case, we haven't visited the left subtree yet. We establish a temporary link from the rightmost node of the left subtree to the current node. 
This link helps us later to identify when we've completed the in-order traversal of the left subtree. After setting the link, we move to the left child to explore the left subtree.

Case 3: There is a left subtree, and the right-most child of this left subtree is already pointing to the current node.

Print the value of the current node.
Revert the temporary link (set it back to null).
Move to the right child of the current node.

This case is crucial for maintaining the integrity of the tree structure. If the right-most child of the left subtree is already pointing to the current node, 
it means we've completed the in-order traversal of the left subtree. We print the value of the current node and then revert the temporary link to restore the original tree structure. 
Finally, we move to the right child to continue the traversal.

Note: The temporary links added in Case 2 are essential for identifying the completion of the left subtree in Case 3. It's critical to revert these links to avoid altering the original structure of the tree.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        inorder = []

        while curr:
            # If no left, add the curr to inorder and go to right
            if not curr.left:
                inorder.append(curr.val)
                curr = curr.right
            else:
                prev = curr.left
                # Finding the right most node
                while prev.right and prev.right != curr:
                    prev = prev.right
                
                if not prev.right:
                    # Add link from right most node to curr
                    prev.right = curr
                    curr = curr.left
                else:
                    # If link already exists, add the curr to inorder and remove the link and go to right
                    inorder.append(curr.val)
                    prev.right = None
                    curr = curr.right
        
        return inorder

'''

Complexity Analysis

Time Complexity: O(2N) where N is the number of nodes in the Binary Tree.

The time complexity is linear, as each node is visited at most twice (once for establishing the temporary link and once for reverting it).
In each step, we perform constant-time operations, such as moving to the left or right child and updating pointers.

Space Complexity: O(1) The space complexity is constant, as the algorithm uses only a constant amount of extra space irrespective of the input size.

Morris Traversal does not use any additional data structures like stacks or recursion, making it an in-place algorithm.
The only space utilised is for a few auxiliary variables, such as pointers to current and in-order predecessor nodes.

'''

