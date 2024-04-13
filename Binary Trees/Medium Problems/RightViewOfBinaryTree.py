'''

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Intuition
To get the left and right view of a Binary Tree, we perform a depth-first traversal of the Binary Tree while keeping track of the level of each node. 
For both the left and right view, we’ll ensure that only the first node encountered at each level is added to the result vector.

Algorithm for Right View

Step 1: Initialise an empty vector `res` to store the left view nodes.

Step 2: Implement a recursive depth-first traversal of the binary tree.
Base Case: Check if the current node is null, if true, return the function as we have reached the end of that particular vertical level.
Recursive Function: The recursive function takes in arguments the current node of the Binary Tree, its current level and the result vector.

We check if the size of the result vector is equal to the current level.
If true, it means that we have not yet encountered any node at this level in the result vector. Add the value of the current node to the result vector.
Recursively call the function for the current nodes right then left child with an increased level ie. level + 1.
We call the right child first as we want to traverse the right most nodes. In cases where there is no right child, the recursion function backtracks and explores the left child.

Step 3: The recursion continues until it reaches the base case. Return the result vector at the end.

Complexity Analysis

Time Complexity: O(log2N) where N is the number of nodes in the Binary Tree. This complexity arises as we travel along the height of the Binary Tree. 
For a balanced binary tree, the height is log2N but in the worst case when the tree is skewed, the complexity becomes O(N).

Space Complexity : O(log2N) where N is the number of nodes in the Binary Tree. This complexity arises because we store the leftmost and rightmost nodes in an additional vector. 
The size of this result vector is proportional to the height of the Binary Tree which will be log2N when the tree is balanced and O(N) in the worst case of a skewed tree.

O(H): Recursive Stack Space is used to calculate the height of the tree at each node which is proportional to the height of the tree.
The recursive nature of the getHeight function, which incurs space on the call stack for each recursive call until it reaches the leaf nodes or the height of the tree.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Recursive function to get right side view
    def rightRecursion(self, root, level, res):
        if not root:
            return

        # Only add if res length and level is equal to avoid adding left nodes
        if len(res) == level:
            res.append(root.val)

        # Go to right node, increase the level
        self.rightRecursion(root.right, level+1, res)

        # Go to left node, increase the level. If right is null we need to add left so need to go left
        self.rightRecursion(root.left, level+1, res)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []

        self.rightRecursion(root, 0, res)
            
        return res


