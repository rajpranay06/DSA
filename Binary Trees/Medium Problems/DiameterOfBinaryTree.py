'''

iven the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

Brute Force Approach
Intuition
To find the diameter of a binary tree, we can think of every node as a potential `Curving Point` of the diameter path. 
This Curving Point is the node along the diameter path that holds the maximum height and from where the path curves uphill and downhill.

Hence we can see that the diameter at a specific curving point is determined by adding the height of the left subtree to the height of the right subtree and adding 1 to account for the level of the curving point. 
Diameter = 1 + Left Subtree Height + Right Subtree Height Therefore, we can traverse the tree recursively considering each node as a potential Curving Point and calculate the height of the left and right subtrees at each node. 
This will give us the diameter for the current Curving Point. Throughout the traversal, we track the maximum diameter encountered and return it as the overall diameter of the Binary Tree.

Complexity Analysis

Time Complexity: O(N*N) where N is the number of nodes in the Binary Tree.
This arises as we calculate the diameter of each node and to calculate the height of its left and right children, we traverse the tree which is proportional to the number of nodes.
Since this calculation is performed for each node in the tree, the complexity becomes: O(N x N) ~ O(N2).

Space Complexity : O(1) as no additional data structures or memory is allocated.
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
    def __init__(self):
        # Global variable to
        # store the diameter
        self.diameter = 0  

    # Function to calculate
    # the height of a subtree
    def calculateHeight(self, node):
        if node is None:
            return 0

        # Recursively calculate the
        # height of left and right subtrees
        left_height = self.calculateHeight(node.left)
        right_height = self.calculateHeight(node.right)

        # Calculate the diameter at the current
        # node and update the global variable
        # print(left_height, right_height, node.val)
        self.diameter = max(self.diameter, left_height + right_height)

        # Return the height
        # of the current subtree
        return 1 + max(left_height, right_height)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.calculateHeight(root)

        # Return the maximum diameter
        # found during traversal
        return self.diameter

'''

Optimal Approach

Intuition
The O(N2) time complexity of the previous approach can be optimised by eliminating the steps of repeatedly calculating subtree heights. 
The heights of the left and right subtrees are computed multiple times for each node, which leads to redundant calculations. Instead, we can compute these heights in a bottom-up manner. 
The Postorder method allows us to validate balance conditions efficiently during the traversal.

The postorder traversal operates in a bottom-up manner, calculating subtree information before moving to the parent node. 
We efficiently compute the heights of both the subtrees and at the same time calculate the diameter and update the maximum diameter encountered.

Complexity Analysis

Time Complexity: O(N) where N is the number of nodes in the Binary Tree. This complexity arises from visiting each node exactly once during the postorder traversal.

Space Complexity : O(1) as no additional space or data structures is created that is proportional to the input size of the tree. 
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
    def findHeight(self, node, diameter):
        if not node:
            return 0
        
        # Find left and right heights of subtree
        lh = self.findHeight(node.left, diameter)
        rh = self.findHeight(node.right, diameter)
        
        # Set diameter to max value
        diameter[0] = max(diameter[0], lh+rh)

        return 1 + max(lh,rh)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = [0]

        self.findHeight(root, diameter)
        # Return the maximum diameter
        # found during traversal
        return diameter[0]





