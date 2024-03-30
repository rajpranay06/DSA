'''

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Approach 1: Using Level Order traversal

Time Complexity: O(N) 
Space Complexity: O(N) ( Queue data structure is used )

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
        q = [root]
        height = 1
        while q:
            ans = False
            k = len(q)
            
            # Run a loop for each level, based on queue length
            for i in range(k):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                    ans = True
                if node.right:
                    q.append(node.right)
                    ans = True
                    
            if ans:
                height += 1
            
        return height


'''

Approach 2: 

Intuition: Recursively ( Post Order Traversal )
If we have to do it recursively, then what we can think of is, If I have Maximum Depth of Left subtree and Maximum Depth of Right subtree then what will be the height or depth of the tree?
Exactly,
1 + max(depth of left subtree, depth of right subtree)
So, to calculate the Maximum Depth, we can simply take the maximum of the depths of the left and right subtree and add 1 to it.
Why take Maximum?? Because we need maximum depth so if we know left & right children's maximum depth then we’ll definitely get to the maximum depth of the entire tree.

Time Complexity: O(N) 
Space Complexity: O(1) Extra Space + O(H) Recursion Stack space, where “H”  is the height of the binary tree.

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
            
        return 1 + max(leftHeight, rightHeight)
