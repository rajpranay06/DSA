'''

Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. 
It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

Approach:
Intuition
Given that the binary is a complete binary tree, we can exploit its properties to optimise the algorithm and achieve a better time complexity. 
In a complete binary tree, the last level may not be completely filled, but the nodes are positioned from left to right. This property allows us to determine the number of nodes using just the height. 
The relationship between the height of the binary tree (h) and the maximum number of nodes it can have, denoted by the formula: Maximum Number of Nodes: 2^h-1

If the last level of a binary tree is perfectly filled, known as a perfect binary tree, the count of nodes can be determined by the formula: 2h-1, where h is the height. 
To check if the last level of the Binary Tree is filled or not we can compare the left and right heights of the tree.

If the left height equals right height, it indicates that the last level is completely filled.
If the left height does not equal right height, the last level is not completely filled.
In the case where left height and right height differ, we can employ a recursive approach. We recursively calculate the number of nodes in the left subtree and in the right subtree , 
and then return the total count as 1 + leftNodes + rightNodes. If the height of the left subtree is equal to the height of the right subtree, we can directly calculate using the 2h-1 formula.

Algorithm:

Step 1: Base Case If the given node is null, we return 0 as there are no nodes to count.

Step 2: Recursive Calls: Recursively find the left height and right height of the Binary Tree.

Step 3: Comparison: If the left height is equal to the right height implies that the tree’s last level is completely filled. Return the count of nodes using the formula: return (1 << lh) - 1, 
where << represents the left shift operator and represents the power of 2.

Step 4: If the left height is not equal to the right height implies that the tree’s last level is not completely filled. 
Recursively call the function to the left and right subtree and return the final number of nodes as 1 + countNodes(root->left) + countNodes(root->right)

Step 5: Implement the find left height and right height functions.

Start with the variable height set to 0.
Use a while loop to traverse the left/right side of the tree incrementing the height until reaching a leaf node.
Return the calculated height.

Complexity Analysis

Time Complexity: O(log N * log N) where N is the number of nodes in the Binary Tree.

The calculation of leftHeight and rightHeight takes O(log N) time.
In the worst case, when encountering the second case (leftHeight != rightHeight), the recursive calls are made at most log N times (the height of the tree).
Therefore, the total time complexity is O(log N * log N).

Space Complexity : O(H) ~ O(N) where N is the number of nodes in the Binary Tree.

The space complexity is determined by the maximum depth of the recursion stack, which is equal to the height of the binary tree.
Since the given tree is a complete binary tree, the height will always be log N.
Therefore, the space complexity is O(log N).

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leftHeight(self, node):
        lh = 0
        while node:
            lh += 1
            node = node.left
        return lh
    
    def rightHeight(self, node):
        rh = 0
        while node:
            rh += 1
            node = node.right
        return rh

    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        lh = self.leftHeight(root)
        rh = self.rightHeight(root)

        # If left and right heights are equal, we can return total nodes in complete binary tree
        if lh == rh:
            return (1 << lh) - 1
        
        # Else to to next childs, and add 1 to it(root node)
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

